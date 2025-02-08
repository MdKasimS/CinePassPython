from sqlalchemy import Column, Integer, String
from Database.models import Base

class Credential(Base):
    __tablename__ = "credentials"
    
    id = Column(Integer, primary_key=True, index=True)
    login_id = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    session_token_id = Column(String, unique=True, nullable=True)

    def __repr__(self):
        return f"Credential(ID={self.id}, LoginID={self.login_id}, Token={self.session_token_id})"
