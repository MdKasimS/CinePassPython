# from sqlalchemy import Column, Integer, String, ForeignKey
#
# from src.Classes.Base.ABaseModel import ABaseModel
#
#
# class Seat(ABaseModel):
#     __tablename__ = "seats"
#
#     id = Column(Integer, primary_key=True, index=True)
#     seat_number = Column(String, nullable=False)
#     is_reserved = Column(Integer, default=0)
#     show_id = Column(Integer, ForeignKey("shows.id"), nullable=False)
#
#     def __repr__(self):
#         return f"Seat(ID={self.id}, SeatNumber={self.seat_number}, Reserved={self.is_reserved})"
