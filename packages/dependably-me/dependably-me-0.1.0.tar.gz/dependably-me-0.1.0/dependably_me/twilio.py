import os

from rich import print
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client


class TwilioClient:
    """Simple Twilio Client."""

    def __init__(
        self,
        messaging_service_sid: str = None,
        account_sid: str = None,
        auth_token: str = None,
    ):
        account_sid = account_sid or os.getenv("DPM_TWILIO_ACCOUNT_SID")
        auth_token = auth_token or os.getenv("DPM_TWILIO_AUTH_TOKEN")
        self.client = Client(account_sid, auth_token)
        self.messaging_service_sid = messaging_service_sid or os.getenv(
            "DPM_TWILIO_MESSAGING_SERVICE_SID"
        )

    def send(self, to: str, body: str, dry_run: bool = False):
        return (
            None
            if dry_run
            else self.client.messages.create(
                to=to, body=body, messaging_service_sid=self.messaging_service_sid
            )
        )

    def fetch(self, message_sid: str):
        return self.client.messages(message_sid).fetch()

    def list(self, limit: int = 20):
        return self.client.messages.list(limit=limit)
