import os
from typing import List

from pydantic import BaseModel
from pydantic_yaml import YamlModel

from dependably_me.project import Project


class Contact(BaseModel):
    id: str
    name: str

    @property
    def number(self):
        return os.getenv(self.env_var_name)

    @property
    def env_var_name(self):
        return f"DPM_{self.id.replace('-', '_').upper()}"

    class Config:
        frozen = True


class ContactsFile(YamlModel):
    __root__: List[Contact]


class ContactsService:
    def __init__(self, project: Project):
        self.project = project

    def get_contacts(self):
        all_contacts = []
        for contacts_file_path in self.project.config.contacts_files:
            all_contacts.extend(
                ContactsFile.parse_file(self.project.root / contacts_file_path).__root__
            )
        return all_contacts
