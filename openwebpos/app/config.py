import os
from dotenv import load_dotenv

load_dotenv()


DB_CONFIGURED = os.getenv("DB_CONFIGURED", "False") == "True"
