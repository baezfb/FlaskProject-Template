import os

from dotenv import load_dotenv

load_dotenv()

# Flask settings
SECRET_KEY = (
    "TestSecret-26b8cc7c6f7afabf828bf647c898244034c708e0d8513a04976bd561c67d9714"
)

# Application settings
TIMEZONE = "US/Central"
APP_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
APP_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
UUID_NAMESPACE = "www.openwebpos.com"

# Database settings
SQLALCHEMY_DATABASE_URI = f"sqlite:///{APP_DIR}/openwebpos.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

TEST = "Test from default config file"
