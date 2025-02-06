from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Database Configuration (Replace with actual PostgreSQL credentials)
DATABASE_URL = "postgresql://username:password@localhost/cinepass_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    bookings = relationship("Booking", back_populates="user")

# Movie Model
class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)  # Duration in minutes

    shows = relationship("Show", back_populates="movie")

# Theatre Model
class Theatre(Base):
    __tablename__ = "theatres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    shows = relationship("Show", back_populates="theatre")

# Show Model
class Show(Base):
    __tablename__ = "shows"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    theatre_id = Column(Integer, ForeignKey("theatres.id"), nullable=False)
    
    movie = relationship("Movie", back_populates="shows")
    theatre = relationship("Theatre", back_populates="shows")
    bookings = relationship("Booking", back_populates="show")

# Seat Model (New)
class Seat(Base):
    __tablename__ = "seats"

    id = Column(Integer, primary_key=True, index=True)
    seat_number = Column(String, nullable=False)
    show_id = Column(Integer, ForeignKey("shows.id"), nullable=False)
    is_booked = Column(Boolean, default=False)

    show = relationship("Show", back_populates="seats")

Show.seats = relationship("Seat", back_populates="show")

# Booking Model
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    show_id = Column(Integer, ForeignKey("shows.id"), nullable=False)
    seat_id = Column(Integer, ForeignKey("seats.id"), nullable=False)

    user = relationship("User", back_populates="bookings")
    show = relationship("Show", back_populates="bookings")
    seat = relationship("Seat")

# Bill Model (New)
class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    total_amount = Column(Integer, nullable=False)

    booking = relationship("Booking")

# Create Tables
Base.metadata.create_all(bind=engine)
