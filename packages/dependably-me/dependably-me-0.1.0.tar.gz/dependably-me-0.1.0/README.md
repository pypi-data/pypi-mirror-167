# dependably.me

SMS reminders for the things that matter.

> Note: dependably.me is new and experimental. Here be dragons 🐉

## Intro

dependably.me helps you keep track of recurring and one-off events by generating and sending SMS messages, via [Twilio](https://www.twilio.com).
Stay on top of birthdays, renewals and chores (like watering your houseplants 🌱) with lowest-common-denominator technology; SMS.

## How it works

dependably.me allows you to save your reminders in YAML documents, and to express the frequency of each event using crontab expressions.
For example:

```yaml
# reminders.yml
- id: barbossas-birthday
  title: Captain Barbossas' Birthday
  description: Send him the monkey.
  schedule: "0 0 1 1 *"
  contacts:
    - jack-sparrow
```

This reminder is for a birthday event that begins every year on the 1st of January at midnight.
The contacts who will recieve notifications are `jack-sparrow`.
Contacts are also managed in YAML documents:

```yaml
# contacts.yml
- id: jack-sparrow
  name: Captain Jack Sparrow
```

Contact phone numbers are secret, and are sourced from the capatalised snake-case form of the contact `id`, prefixed with `DPM_`.
Jacks number should be set at `DPM_JACK_SPARROW`, and dependably.me supports sourcing these from a `.env` file at the root of the project directory.

Finally, a `project.yml` laces everything together:

```yaml
version: 1
reminders_files:
  - reminders.yml
contacts_files:
  - contacts.yml
```

Reminders and Contacts are sourced from all of the files listed (paths relative to the project root), allowing you to organise your reminders and contacts however you choose.
For example, you might like to group by kind of reminder:

```yaml
version: 1
reminders_files:
  - birthdays/family.yml
  - birthdays/friends.yml
  - chores/chores.yml
  - cars/mot.yml
  - cars/tax.yml
contacts_files:
  - contacts.yml
```

In addition to sourcing telephone numbers from env vars, dependably.me also requires Twilio configuration via env vars too.
The following are required for dependably.me to send SMS messages:

```
DPM_TWILIO_ACCOUNT_SID=<twilio account sid>
DPM_TWILIO_AUTH_TOKEN=<twilio auth token>
DPM_TWILIO_MESSAGING_SERVICE_SID=<twilio messaging service sid>
```

Setting up Twilio to send messages is easy. Check out their [Programable SMS Python Quickstart](https://www.twilio.com/docs/sms/quickstart/python)

## Usage

With some reminders added and you project configured, you can send reminders using:

```shell
dependably-me reminders remind
```

To view the messages generated without sending any messages, try:

```shell
dependably-me reminders remind --dry-run
```

## Scheduling messages

dependably.me is designed to be invoked weekly, to notify of events happening in that week, the rest of the month and next month.
Therefore it is recommended to run dependably.me from your preferred scheduler, such as cron locally or github actions (or similar) in the cloud.
