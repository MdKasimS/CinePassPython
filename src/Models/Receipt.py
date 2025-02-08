# from sqlalchemy import Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
#
# from src.Classes.Base.ABaseModel import ABaseModel
#
#
# class Receipt(ABaseModel):
#     __tablename__ = "receipts"
#
#     id = Column(Integer, primary_key=True, index=True)
#     bill_id = Column(Integer, ForeignKey("bills.id"), nullable=False)
#
#     bill = relationship("Bill")
#
#     def __repr__(self):
#         return f"Receipt(ID={self.id}, BillID={self.bill_id})"
