# from sqlalchemy import Column, Integer, String
#
# from src.Classes.Base.ABaseModel import ABaseModel
#
#
# class Customer(ABaseModel):
#     __tablename__ = "customers"
#
#     id = Column(Integer, primary_key=True, index=True)
#     customer_name = Column(String, nullable=False)
#     city = Column(String, nullable=False)
#
#     def __repr__(self):
#         return f"Customer(ID={self.id}, Name={self.customer_name}, City={self.city})"
