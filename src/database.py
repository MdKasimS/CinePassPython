# database.py (PostgreSQL Version)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://your_user:your_password@localhost:5432/your_database"

Base = declarative_base()

def get_engine():
    return create_engine(DATABASE_URL, echo=True)
