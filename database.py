from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv()

password = urllib.parse.quote_plus(os.getenv("DB_PASSWD"))
engine = create_engine(
    f"mysql+pymysql://root:{password}@192.168.1.7/website?charset=utf8mb4"
)

def insert_user(name, email):
    with engine.begin() as conn:  # begins a transaction and auto-commits
        query = text("INSERT INTO user_details (name, email) VALUES (:name, :email)")
        conn.execute(query, {"name": name, "email": email})
