from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

# from src.Classes.Base.ABaseModel import ABaseModel

Base = declarative_base()

class User(Base):

    def display_info(self):
        pass

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=False, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    contact = Column(String, unique=True, index=True, nullable=False)

