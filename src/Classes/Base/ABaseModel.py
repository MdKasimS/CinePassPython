from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class ABaseModel(Base):
    __abstract__ = True

    def __init__(self):
        super().__init__()

