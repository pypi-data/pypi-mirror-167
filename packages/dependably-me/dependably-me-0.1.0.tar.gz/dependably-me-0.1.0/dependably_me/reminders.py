import calendar
from datetime import date, datetime
from typing import List, Optional

import humanize
from croniter import croniter
from dateutil import relativedelta
from pydantic import BaseModel, ValidationError, validator
from pydantic_yaml import YamlModel
from tzlocal import get_localzone

from dependably_me.contacts import ContactsService
from dependably_me.twilio import TwilioClient

SECTIONS = [
    ("this_week", "This Week"),
    ("this_month", "This Month"),
    ("next_month", "Next Month"),
]


class Reminder(BaseModel):
    id: str
    title: str
    description: Optional[str]
    schedule: Optional[str]
    date: Optional[date]
    contacts: List[str]

    @validator("schedule")
    def schedule_must_be_valid_crontab(cls, schedule):
        if not croniter.is_valid(schedule):
            raise ValidationError("invalid crontab expression")
        return schedule

    @validator("date")
    def check_a_or_b(cls, dt, values):
        if "schedule" in values or dt:
            return dt
        else:
            raise ValueError("either a schedule or a date is required")

    def get_next(self, tz=None, ret_type=datetime):
        if not self.date:
            tz = tz or get_localzone()
            local_date = datetime.now(tz)
            return croniter(self.schedule, local_date).get_next(datetime)
        else:
            return self.date

    @property
    def time_until_next(self, tz=None):
        tz = tz or get_localzone()
        return datetime.now(tz) - self.get_next()


class RemindersFile(YamlModel):
    __root__: List[Reminder]


class RemindersService:
    def __init__(self, project):
        self.project = project
        self.twilio_client = TwilioClient()
        self.contacts_service = ContactsService(project=project)

    def list_reminders(self):
        all_reminders = []
        for reminders_file_path in self.project.config.reminders_files:
            all_reminders.extend(
                RemindersFile.parse_file(
                    self.project.root / reminders_file_path
                ).__root__
            )
        return all_reminders

    def get_contacts_reminders(self, due_before: datetime = None) -> dict:
        """Fetch a dictionary of contacts and their reminders, optionally filtered by a due date."""
        contact_reminders = {}
        for contact in self.contacts_service.get_contacts():
            for reminder in self.list_reminders():
                if due_before is not None:
                    reminder_next_due = reminder.get_next()
                    if reminder_next_due > due_before:
                        continue
                if contact.id in reminder.contacts:
                    if contact not in contact_reminders.keys():
                        contact_reminders[contact] = []
                    contact_reminders[contact].append(reminder)
        return contact_reminders

    @staticmethod
    def _are_same_week(d1: datetime, d2: datetime):
        return d1.isocalendar()[1] == d2.isocalendar()[1] and d1.year == d2.year

    @staticmethod
    def _are_same_month(d1: datetime, d2: datetime):
        return d1.month == d2.month and d1.year == d2.year

    @staticmethod
    def _is_next_month(d1: datetime, d2: datetime):
        return (d1.month + 1) == d2.month and d1.year == d2.year

    @staticmethod
    def _evaluate_reminder(grouped_reminders, key, func, d1, reminder) -> bool:
        if func(d1, reminder.get_next()):
            if key not in grouped_reminders.keys():
                grouped_reminders[key] = []
            grouped_reminders[key].append(reminder)
            return True
        return False

    def _group_contact_reminders(self, contact_reminders: dict, today: datetime):
        grouped_contact_reminders = {}
        for contact, reminders in contact_reminders.items():
            grouped_reminders = {}
            for reminder in reminders:

                if self._evaluate_reminder(
                    grouped_reminders=grouped_reminders,
                    key="this_week",
                    func=self._are_same_week,
                    d1=today,
                    reminder=reminder,
                ):
                    continue

                if self._evaluate_reminder(
                    grouped_reminders=grouped_reminders,
                    key="this_month",
                    func=self._are_same_month,
                    d1=today,
                    reminder=reminder,
                ):
                    continue

                if self._evaluate_reminder(
                    grouped_reminders=grouped_reminders,
                    key="next_month",
                    func=self._is_next_month,
                    d1=today,
                    reminder=reminder,
                ):
                    continue

            if grouped_reminders:
                grouped_contact_reminders[contact] = grouped_reminders

        return grouped_contact_reminders

    def remind(self, dry_run: bool = False):
        """Evaluate reminders and message relevant contacts."""
        tz = get_localzone()
        today = datetime.now(tz)
        next_month = today + relativedelta.relativedelta(months=1)
        last_day_of_next_month = calendar.monthrange(next_month.year, next_month.month)[
            0
        ]
        due_before = datetime(
            next_month.year, next_month.month, last_day_of_next_month, tzinfo=tz
        )
        grouped_contact_reminders = self._group_contact_reminders(
            contact_reminders=self.get_contacts_reminders(due_before=due_before),
            today=today,
        )
        messages = []
        for contact, reminders in grouped_contact_reminders.items():
            # compose message body
            message_body = ""
            for key, title in SECTIONS:
                if key in reminders.keys():
                    message_body += title + "\n"
                    for reminder in reminders[key]:
                        message_body += "\n"
                        message_body += reminder.title
            message = self.twilio_client.send(
                to=contact.number, body=message_body, dry_run=dry_run
            )
            messages.append((contact, message, message_body))

        return messages
