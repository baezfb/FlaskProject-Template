import os

from dotenv import load_dotenv

load_dotenv()

# Flask settings
DEBUG = os.getenv("DEBUG", False)
SECRET_KEY = os.getenv("SECRET_KEY", "test-secret-key")

# Application settings
TIMEZONE = os.getenv("TIMEZONE", "US/Central")
APP_PATH = os.getenv(
    "APP_PATH", os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
)
APP_DIR = os.getenv(
    "APP_DIR",
    os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
)
DB_CONFIGURED = os.getenv("DB_CONFIGURED", False)
APP_RESTARTED = os.getenv("APP_RESTARTED", False)
USER_CONFIGURED = os.getenv("USER_CONFIGURED", False)
APP_CONFIGURED = os.getenv("APP_CONFIGURED", False)
SITE_NAME = os.getenv("SITE_NAME", "Open Web POS")

# Database settings
if DB_CONFIGURED:
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
