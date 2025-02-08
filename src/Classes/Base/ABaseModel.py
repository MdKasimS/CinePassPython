from abc import abstractmethod, ABC

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class ABaseModel(ABC, Base):
    """Abstract base class for common model functionality."""
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)

    @abstractmethod
    def display_info(self):
        pass
