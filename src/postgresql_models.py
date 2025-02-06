from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from Database.models import Base  # ✅ Ensure Base is correctly imported
from werkzeug.security import generate_password_hash, check_password_hash

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    bookings = relationship("Booking", back_populates="user")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Booking(Base):
    __tablename__ = "bookings"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    seat_id = Column(Integer, ForeignKey("seats.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="bookings")
    movie = relationship("Movie", back_populates="bookings")
    seat = relationship("Seat", back_populates="booking")

class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)  # Duration in minutes
    rating = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    bookings = relationship("Booking", back_populates="movie")

class Seat(Base):
    __tablename__ = "seats"
    
    id = Column(Integer, primary_key=True, index=True)
    seat_number = Column(String, nullable=False)
    is_booked = Column(Boolean, default=False)
    
    booking = relationship("Booking", uselist=False, back_populates="seat")  # ✅ One-to-One relationship

class Bill(Base):
    __tablename__ = "bills"
    
    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(Integer, unique=True, nullable=False)
    total_amount = Column(Float, nullable=False)
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    booking = relationship("Booking")
