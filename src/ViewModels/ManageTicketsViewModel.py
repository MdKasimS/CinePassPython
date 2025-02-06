import os

class ManageTicketsViewModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ManageTicketsViewModel, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.tickets = []
            self._initialized = True  # Ensures __init__ runs only once

    def book_tickets(self, user_id, movie_name, seat_number):
        """
        Simulates booking a ticket.
        In a real-world scenario, this would interact with a database.
        """
        ticket = {
            "user_id": user_id,
            "movie_name": movie_name,
            "seat_number": seat_number,
        }
        self.tickets.append(ticket)
        print(f"🎟️ Ticket booked for {movie_name} (Seat: {seat_number})")
        return ticket

    def clear_screen(self):
        """Clears the console screen in a cross-platform way."""
        os.system("cls" if os.name == "nt" else "clear")

# Example usage
if __name__ == "__main__":
    tickets_view_model = ManageTicketsViewModel()
    
    # Book some tickets
    tickets_view_model.book_tickets(user_id=1, movie_name="Inception", seat_number="A10")
    tickets_view_model.book_tickets(user_id=2, movie_name="Avatar", seat_number="B15")

    # Clear screen
    tickets_view_model.clear_screen()
