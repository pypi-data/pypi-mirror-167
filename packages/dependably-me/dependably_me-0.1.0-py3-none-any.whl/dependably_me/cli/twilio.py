import os

import typer
from rich import print
from twilio.base.exceptions import TwilioRestException

from dependably_me.twilio import TwilioClient

twilio_client = TwilioClient()

twilio_app = typer.Typer()


@twilio_app.command()
def send(to: str, body: str, dry_run: bool = False):
    if not dry_run:
        try:
            message = twilio_client.send(to=to, body=body, dry_run=dry_run)
            print(f'Sent message "{message.body}" to "{message.to}"')
            print(f"Message SID: {message.sid}")
        except TwilioRestException as e:
            print(e)
    else:
        print("Dry run; no messages will be sent.")
        print(f"Would have sent message '{body}' to '{to}'")


@twilio_app.command()
def fetch(message_sid: str):
    message = twilio_client.fetch(message_sid=message_sid)
    print(message.__dict__)


@twilio_app.command("list")
def list_(limit: int = 20):
    messages = twilio_client.list(limit=limit)
    print([msg.__dict__ for msg in messages])
