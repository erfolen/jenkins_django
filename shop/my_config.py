import os

from dotenv import load_dotenv

load_dotenv()
login = os.getenv("user_database")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")
host = os.getenv("HOST")

