from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create database engine (SQLite example, change as needed)
DATABASE_URL = "sqlite:///cinema_booking.db"
engine = create_engine(DATABASE_URL, echo=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model
Base = declarative_base()

# Create tables
def init_db():
    Base.metadata.create_all(engine)
