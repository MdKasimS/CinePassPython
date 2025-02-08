from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from src.Classes.Base.ABaseSingleton import Singleton


class CinePassDb(Singleton):
    """Singleton class to manage PostgreSQL database connection and session."""

    def __init__(self):
        self.engine = create_engine("postgresql://your_user:your_password@localhost/your_db")
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self._session = None

    def get_session(self):
        if self._session is None:
            self._session = self.SessionLocal()
        return self._session