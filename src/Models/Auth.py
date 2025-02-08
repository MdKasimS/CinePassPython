# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
#
# from src.Classes.Base.ABaseModel import ABaseModel
#
#
# class Auth(ABaseModel):
#     __tablename__ = "auth"
#
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     password_hash = Column(String, nullable=False)
#     privilege_level = Column(Integer, nullable=False)
#
#     user = relationship("User")
#
#     def __repr__(self):
#         return f"Auth(UserId={self.user_id}, PrivilegeLevel={self.privilege_level})"