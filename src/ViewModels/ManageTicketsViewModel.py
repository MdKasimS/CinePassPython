from sqlalchemy.orm import Session
from Models.Booking import Booking

class ManageTicketsViewModel:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all_bookings(self):
        return self.db_session.query(Booking).all()

    def cancel_booking(self, booking_id: int):
        booking = self.db_session.query(Booking).filter(Booking.id == booking_id).first()
        if booking:
            self.db_session.delete(booking)
            self.db_session.commit()
            return True
        return False

    def __repr__(self):
        return "ManageTicketsViewModel(Handles booking management operations)"