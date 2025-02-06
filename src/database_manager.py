from sqlalchemy.orm import Session
from Models import User, Booking, Movie, Seat, Bill
from werkzeug.security import generate_password_hash

class DatabaseManager:
    def __init__(self, db_session: Session):
        self.db = db_session

    # ✅ Add a new user
    def add_user(self, username, email, password):
        hashed_pw = generate_password_hash(password)
        user = User(username=username, email=email, password_hash=hashed_pw)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    # ✅ Add a new movie
    def add_movie(self, title, duration, rating):
        movie = Movie(title=title, duration=duration, rating=rating)
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie

    # ✅ Add a new seat
    def add_seat(self, seat_number):
        seat = Seat(seat_number=seat_number, is_booked=False)
        self.db.add(seat)
        self.db.commit()
        self.db.refresh(seat)
        return seat

    # ✅ Book a ticket
    def book_ticket(self, user_id, movie_id, seat_id):
        seat = self.db.query(Seat).filter(Seat.id == seat_id, Seat.is_booked == False).first()
        if not seat:
            return None  # Seat already booked
        
        booking = Booking(user_id=user_id, movie_id=movie_id, seat_id=seat_id)
        seat.is_booked = True  # Mark seat as booked
        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)
        return booking

    # ✅ Generate a bill
    def generate_bill(self, booking_id, total_amount):
        bill = Bill(booking_id=booking_id, total_amount=total_amount, invoice_number=1000 + booking_id)
        self.db.add(bill)
        self.db.commit()
        self.db.refresh(bill)
        return bill

    # ✅ Get all users
    def get_all_users(self):
        return self.db.query(User).all()

    # ✅ Get all bookings
    def get_all_bookings(self):
        return self.db.query(Booking).all()
