# Refactored database_manager.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base

DATABASE_URL = "postgresql://your_user:your_password@localhost:5432/your_database"

def get_engine():
    return create_engine(DATABASE_URL, echo=True)

def get_session():
    engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()

def init_db():
    """Initialize the database and create tables."""
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully!")

if __name__ == "__main__":
    init_db()
