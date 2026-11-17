import os
from dotenv import load_dotenv


load_dotenv()

DB_CONNECTION = os.getenv("DB_CONNECTION")

if not DB_CONNECTION:
    raise ValueError("Не найден DB_CONNECTION в .env файле!")