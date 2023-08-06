from __future__ import annotations

import pathlib
from typing import List

from pydantic import FilePath
from pydantic_yaml import YamlModel


class ProjectConfig(YamlModel):
    version: int = 1
    reminders_files: List[pathlib.Path]
    contacts_files: List[pathlib.Path]

    class Config:
        arbitrary_types_allowed = True


class Project:
    """Prject object."""

    def __init__(self, root: pathlib.Path = None):
        self.root = root or pathlib.Path.cwd()
        self.project_file = self.root / "project.yml"

    def is_valid(self):
        return self.project_file.is_file()

    @property
    def config(self):
        return ProjectConfig.parse_file(self.project_file)

    @property
    def dotenv(self) -> pathlib.Path:
        """Return a fully-qualified path to this project dotenv file."""
        return (self.root / ".env").absolute()
