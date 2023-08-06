# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dependably_me', 'dependably_me.cli']

package_data = \
{'': ['*']}

install_requires = \
['croniter>=1.3.7,<2.0.0',
 'humanize>=4.3.0,<5.0.0',
 'pydantic-yaml[ruamel]>=0.8.0,<0.9.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'twilio>=7.13.0,<8.0.0',
 'typer[all]>=0.6.1,<0.7.0',
 'tzlocal>=4.2,<5.0']

entry_points = \
{'console_scripts': ['dependably-me = dependably_me.cli:app',
                     'dpm = dependably_me.cli:app']}

setup_kwargs = {
    'name': 'dependably-me',
    'version': '0.1.0',
    'description': '',
    'long_description': '# dependably.me\n\nSMS reminders for the things that matter.\n\n> Note: dependably.me is new and experimental. Here be dragons 🐉\n\n## Intro\n\ndependably.me helps you keep track of recurring and one-off events by generating and sending SMS messages, via [Twilio](https://www.twilio.com).\nStay on top of birthdays, renewals and chores (like watering your houseplants 🌱) with lowest-common-denominator technology; SMS.\n\n## How it works\n\ndependably.me allows you to save your reminders in YAML documents, and to express the frequency of each event using crontab expressions.\nFor example:\n\n```yaml\n# reminders.yml\n- id: barbossas-birthday\n  title: Captain Barbossas\' Birthday\n  description: Send him the monkey.\n  schedule: "0 0 1 1 *"\n  contacts:\n    - jack-sparrow\n```\n\nThis reminder is for a birthday event that begins every year on the 1st of January at midnight.\nThe contacts who will recieve notifications are `jack-sparrow`.\nContacts are also managed in YAML documents:\n\n```yaml\n# contacts.yml\n- id: jack-sparrow\n  name: Captain Jack Sparrow\n```\n\nContact phone numbers are secret, and are sourced from the capatalised snake-case form of the contact `id`, prefixed with `DPM_`.\nJacks number should be set at `DPM_JACK_SPARROW`, and dependably.me supports sourcing these from a `.env` file at the root of the project directory.\n\nFinally, a `project.yml` laces everything together:\n\n```yaml\nversion: 1\nreminders_files:\n  - reminders.yml\ncontacts_files:\n  - contacts.yml\n```\n\nReminders and Contacts are sourced from all of the files listed (paths relative to the project root), allowing you to organise your reminders and contacts however you choose.\nFor example, you might like to group by kind of reminder:\n\n```yaml\nversion: 1\nreminders_files:\n  - birthdays/family.yml\n  - birthdays/friends.yml\n  - chores/chores.yml\n  - cars/mot.yml\n  - cars/tax.yml\ncontacts_files:\n  - contacts.yml\n```\n\nIn addition to sourcing telephone numbers from env vars, dependably.me also requires Twilio configuration via env vars too.\nThe following are required for dependably.me to send SMS messages:\n\n```\nDPM_TWILIO_ACCOUNT_SID=<twilio account sid>\nDPM_TWILIO_AUTH_TOKEN=<twilio auth token>\nDPM_TWILIO_MESSAGING_SERVICE_SID=<twilio messaging service sid>\n```\n\nSetting up Twilio to send messages is easy. Check out their [Programable SMS Python Quickstart](https://www.twilio.com/docs/sms/quickstart/python)\n\n## Usage\n\nWith some reminders added and you project configured, you can send reminders using:\n\n```shell\ndependably-me reminders remind\n```\n\nTo view the messages generated without sending any messages, try:\n\n```shell\ndependably-me reminders remind --dry-run\n```\n\n## Scheduling messages\n\ndependably.me is designed to be invoked weekly, to notify of events happening in that week, the rest of the month and next month.\nTherefore it is recommended to run dependably.me from your preferred scheduler, such as cron locally or github actions (or similar) in the cloud.\n',
    'author': 'Ken Payne',
    'author_email': 'me@kenpayne.co.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
