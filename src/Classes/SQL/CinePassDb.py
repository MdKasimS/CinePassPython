from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.Classes.Base.ABaseSingleton import SingletonMeta


class CinePassDb(metaclass=SingletonMeta):
    """Singleton class to manage PostgreSQL database connection and session."""

    def __init__(self):
        super().__init__()
        self.engine = create_engine("postgresql://admin:root@localhost/CinePassDb")
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self._session = None

    def get_session(self):
        if self._session is None:
            self._session = self.SessionLocal()
        return self._session