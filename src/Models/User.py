from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean
from werkzeug.security import generate_password_hash, check_password_hash

from src.Classes.Base.ABaseModel import ABaseModel

class User(ABaseModel):

    def __init__(self):
        super().__init__()

    __tablename__ = "users"

    username = Column(String, unique=False, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    contact = Column(String, unique=True, index=True, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)