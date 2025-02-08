from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from src.Classes.Base.ABaseModel import ABaseModel


class Booking(ABaseModel):
    __tablename__ = "bookings"
    
    id = Column(Integer, primary_key=True, index=True)
    show_id = Column(Integer, ForeignKey("shows.id"), nullable=False)
    customer_name = Column(String, nullable=False)
    number_of_seats = Column(Integer, nullable=False)
    seat_type = Column(String, nullable=False)
    email = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    booking_date = Column(DateTime, default=datetime.utcnow)

    show = relationship("Show")

    def __repr__(self):
        return f"Booking(ID={self.id}, ShowID={self.show_id}, Customer={self.customer_name}, Seats={self.number_of_seats})"


