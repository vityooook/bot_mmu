import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
ADMIN = os.getenv("ADMIN")
DB_LINK = os.getenv("DB_LINK")
REDIS_LINK = os.getenv('REDIS_LINK')
