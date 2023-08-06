from dotenv import load_dotenv

from dependably_me.project import Project

project = Project()
load_dotenv(dotenv_path=project.dotenv)
