from datetime import datetime

class Booking:
    _bookings = {}

    def __init__(self, show_id: int, customer_name: str, number_of_seats: int, seat_type: str, email: str, amount_to_pay: float):
        self.booking_id = self.generate_booking_id()  # Must start from 1000
        self.show_id = show_id
        self.customer_name = customer_name
        self.number_of_seats = number_of_seats
        self.seat_type = seat_type
        self.email = email
        self.amount = amount_to_pay
        self.booking_status = None
        self.booking_date = datetime.now()
        self.seat_numbers = []
    
    @classmethod
    def generate_booking_id(cls):
        """ Generate unique booking ID starting from 1000 """
        return 1000 + len(cls._bookings)

    @classmethod
    def get_bookings(cls):
        return cls._bookings

    @classmethod
    def set_bookings(cls, bookings):
        cls._bookings = bookings

    def __repr__(self):
        return (f"Booking(BookingId={self.booking_id}, ShowId={self.show_id}, "
                f"CustomerName={self.customer_name}, Seats={self.number_of_seats}, "
                f"SeatType={self.seat_type}, Email={self.email}, Amount={self.amount}, "
                f"Status={self.booking_status}, Date={self.booking_date})")
