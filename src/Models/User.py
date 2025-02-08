from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean
from werkzeug.security import generate_password_hash, check_password_hash

from src.Classes.Base.ABaseModel import ABaseModel

class User(ABaseModel):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=False, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    contact = Column(String, unique=True, index=True, nullable=False)

