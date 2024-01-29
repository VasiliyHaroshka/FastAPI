import os

from dotenv import load_dotenv

load_dotenv()

DATA_BASE = os.environ.get("DATA_BASE")
DATA_BASE_FRAMEWORK = os.environ.get("DATA_BASE_FRAMEWORK")
USER_NAME = os.environ.get("USER_NAME")
USER_PASSWORD = os.environ.get("USER_PASSWORD")
URL = os.environ.get("URL")
PORT = os.environ.get("PORT")
DB_NAME = os.environ.get("DB_NAME")
