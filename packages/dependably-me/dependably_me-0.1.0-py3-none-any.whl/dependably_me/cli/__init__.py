import typer

from .reminders import reminders_app
from .twilio import twilio_app

app = typer.Typer()
app.add_typer(twilio_app, name="twilio")
app.add_typer(reminders_app, name="reminders")


if __name__ == "__main__":
    app()
