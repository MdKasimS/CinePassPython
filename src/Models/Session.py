# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
# from datetime import datetime, timedelta
#
# from src.Classes.Base.ABaseModel import ABaseModel
#
#
# class Session(ABaseModel):
#     __tablename__ = "sessions"
#
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     token = Column(String, unique=True, nullable=False)
#     login_timestamp = Column(DateTime, default=datetime.utcnow)
#     expiration_timestamp = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=1))
#
#     def __repr__(self):
#         return f"Session(ID={self.id}, UserID={self.user_id}, Token={self.token})"
