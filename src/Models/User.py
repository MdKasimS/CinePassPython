from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean
from werkzeug.security import generate_password_hash, check_password_hash

from src.Classes.Base.ABaseModel import ABaseModel

class User(ABaseModel):
    __tablename__ = "users"

    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)