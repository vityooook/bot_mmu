import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
ADMIN = os.getenv("ADMIN")
DB_PATH = os.path.join("schedule.db")

