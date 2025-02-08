from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///cinecomplex.db"  # Replace with actual DB URL
Base = declarative_base()

def get_engine():
    return create_engine(DATABASE_URL, echo=True)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Theatre(Base):
    __tablename__ = "theatres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Show(Base):
    __tablename__ = "shows"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    show_id = Column(Integer, nullable=False)

if __name__ == "__main__":
    engine = get_engine()
    Base.metadata.create_all(engine)
