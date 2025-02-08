# Refactored main.py with Dummy Data Integration

from database_manager import init_db, get_session
from postgresql_models import User, Admin, Booking, Show, Movie, Theatre, Seat
from main import Program  # Import the main menu system
from datetime import datetime

# Initialize database
init_db()

# Function to check if data exists and insert dummy data if necessary
def insert_dummy_data():
    session = get_session()
    
    # Check if users already exist
    user_exists = session.query(User).first()
    if user_exists:
        print("✅ Dummy data already exists. Skipping insertion.")
        session.close()
        return

    print("🔄 Inserting dummy data...")

    # Users
    user1 = User(username="johndoe", email="john@example.com", password="hashed_password1", role="user")
    user2 = User(username="janedoe", email="jane@example.com", password="hashed_password2", role="user")
    admin1 = User(username="admin", email="admin@example.com", password="hashed_admin", role="admin")

    # Admin linking
    admin_entry = Admin(user_id=3)  # Assuming 'admin' user has ID 3

    # Theatres
    theatre1 = Theatre(name="PVR Cinemas", location="Downtown")
    theatre2 = Theatre(name="INOX", location="City Center")
    theatre3 = Theatre(name="Cinepolis", location="Mall Road")

    # Movies
    movie1 = Movie(title="Inception", genre="Sci-Fi", duration=148)
    movie2 = Movie(title="Interstellar", genre="Sci-Fi", duration=169)
    movie3 = Movie(title="Avengers: Endgame", genre="Action", duration=181)

    # Shows
    show1 = Show(movie_id=1, theatre_id=1, start_time=datetime(2024, 7, 25, 18, 0), end_time=datetime(2024, 7, 25, 20, 30))
    show2 = Show(movie_id=2, theatre_id=2, start_time=datetime(2024, 7, 26, 19, 0), end_time=datetime(2024, 7, 26, 21, 45))
    show3 = Show(movie_id=3, theatre_id=3, start_time=datetime(2024, 7, 27, 20, 0), end_time=datetime(2024, 7, 27, 23, 0))

    # Bookings
    booking1 = Booking(user_id=1, show_id=1, booking_date=datetime(2024, 7, 25, 17, 30))
    booking2 = Booking(user_id=2, show_id=2, booking_date=datetime(2024, 7, 26, 18, 45))

    # Seats
    seat1 = Seat(show_id=1, seat_number="A1", is_reserved=1)
    seat2 = Seat(show_id=1, seat_number="A2", is_reserved=0)
    seat3 = Seat(show_id=2, seat_number="B1", is_reserved=1)
    seat4 = Seat(show_id=3, seat_number="C3", is_reserved=0)

    # Add all to session and commit
    session.add_all([user1, user2, admin1, admin_entry, theatre1, theatre2, theatre3, movie1, movie2, movie3,
                     show1, show2, show3, booking1, booking2, seat1, seat2, seat3, seat4])
    session.commit()
    session.close()
    print("✅ Dummy data inserted successfully!")

if __name__ == "__main__":
    insert_dummy_data()  # Ensure dummy data is present
    program = Program()  # Start the main menu system
    program.view()
