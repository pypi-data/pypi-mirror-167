import humanize
import typer
from rich import print

from dependably_me.project import Project
from dependably_me.reminders import RemindersService

reminders_app = typer.Typer()


@reminders_app.command(name="list")
def list_(ctx: typer.Context):
    reminders_service = ctx.obj["reminders_service"]
    for reminder in reminders_service.list_reminders():
        print("\n----")
        print("Title: " + reminder.title)
        print(
            "Description: "
            + reminder.description.format(
                when=humanize.naturaltime(reminder.time_until_next)
            )
        )
        print("----")


@reminders_app.command()
def remind(ctx: typer.Context, dry_run: bool = False):
    reminders_service = ctx.obj["reminders_service"]
    print(reminders_service.remind(dry_run=dry_run))


@reminders_app.callback()
def main(ctx: typer.Context):
    """Manage users in the awesome CLI app."""
    ctx.ensure_object(dict)
    project = Project()
    if project.is_valid():
        ctx.obj["project"] = project
        ctx.obj["reminders_service"] = RemindersService(project=project)
    else:
        print("No project found in current directory.")
        raise typer.Exit(code=1)
