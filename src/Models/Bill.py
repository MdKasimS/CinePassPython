# from sqlalchemy import Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
#
# from src.Classes.Base.ABaseModel import ABaseModel
#
#
# class Bill(ABaseModel):
#     __tablename__ = "bills"
#
#     id = Column(Integer, primary_key=True, index=True)
#     booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
#     amount = Column(Integer, nullable=False)
#
#     booking = relationship("Booking")
#
#     def __repr__(self):
#         return f"Bill(ID={self.id}, BookingID={self.booking_id}, Amount={self.amount})"
