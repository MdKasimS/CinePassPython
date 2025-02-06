from datetime import datetime
from decimal import Decimal
from typing import Dict

# Simulate database interaction (you would use an ORM like SQLAlchemy in production)
class SQLInteraction:
    class Db:
        shows = []  # Placeholder to simulate a list of shows
        
        @classmethod
        def add(cls, show):
            cls.shows.append(show)

        @classmethod
        def generate_show_id(cls):
            # Simulating the generation of a unique ShowId, e.g., by incrementing
            return len(cls.shows) + 10001

class Show:
    # Static variable to hold all the shows
    _shows: Dict[int, 'Show'] = {}

    def __init__(self, movie_id: int, theatre_id: int, start_date: datetime, end_date: datetime,
                 platinum_rate: Decimal, gold_rate: Decimal, silver_rate: Decimal):
        self.show_id = SQLInteraction.Db.generate_show_id()  # Automatically set ShowId by DB logic
        self.movie_id = movie_id
        self.theatre_id = theatre_id
        self.start_date = start_date
        self.end_date = end_date
        self.platinum_seat_rate = platinum_rate
        self.gold_seat_rate = gold_rate
        self.silver_seat_rate = silver_rate

    @classmethod
    def get_shows(cls):
        return cls._shows

    @classmethod
    def set_shows(cls, shows):
        cls._shows = shows

    def display_show_details(self):
        print(f"Show ID : {self.show_id}")
        print(f"Movie ID : {self.movie_id}")
        print(f"Theatre ID : {self.theatre_id}")
        print(f"Platinum Seat Rate : {self.platinum_seat_rate}")
        print(f"Gold Seat Rate : {self.gold_seat_rate}")
        print(f"Silver Seat Rate : {self.silver_seat_rate}")

# Example usage:
show = Show(movie_id=1, theatre_id=2, start_date=datetime.now(), end_date=datetime.now(),
            platinum_rate=Decimal('200.00'), gold_rate=Decimal('150.00'), silver_rate=Decimal('100.00'))

# Add to database (simulated)
SQLInteraction.Db.add(show)

# Display show details
show.display_show_details()

# You can add the show to the class-level dictionary
Show.set_shows({show.show_id: show})

# Access the shows stored in the class-level dictionary
print(Show.get_shows())
