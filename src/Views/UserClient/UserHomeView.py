# Refactored UserHomeView.py

import random

class AccountView:
    """Mock AccountView class with user details."""
    
    def __init__(self):
        self.user_name = "John Doe"
        self.email = "johndoe@example.com"
        self.contact = "9876543210"
        self.balance = 1500  # Example balance
        self.bookings = []

    def view(self):
        """Display account details."""
        print("\n===== Your Profile =====")
        print(f"Name: {self.user_name}")
        print(f"Email: {self.email}")
        print(f"Contact: {self.contact}")
        print(f"Balance: ₹{self.balance}")
        print("========================")

class UserHomeView:
    def __init__(self):
        self.choice = 0
        self.account = AccountView()  # Integrate AccountView
        self.menu_list = [
            "1. Book Ticket",
            "2. Show Shows",
            "3. Cancel Tickets",
            "4. Previous Bookings",
            "5. Show Profile",
            "6. Show Balance",
            "7. Exit"
        ]
        self.available_shows = {
            1: "Avengers: Endgame",
            2: "Interstellar",
            3: "Inception",
            4: "Jawan",
            5: "Pathaan"
        }

    def book_ticket(self):
        """Mock ticket booking system."""
        print("\nAvailable Shows:")
        for key, show in self.available_shows.items():
            print(f"{key}. {show}")

        try:
            choice = int(input("Enter the show number to book: "))
            if choice in self.available_shows:
                ticket_id = random.randint(1000, 9999)
                self.account.bookings.append((ticket_id, self.available_shows[choice]))
                print(f"✅ Ticket booked successfully! Ticket ID: {ticket_id}")
            else:
                print("❌ Invalid selection. Try again.")
        except ValueError:
            print("❌ Invalid input. Enter a valid number.")

    def show_shows(self):
        """Display available shows."""
        print("\n🎬 Available Shows:")
        for key, show in self.available_shows.items():
            print(f"{key}. {show}")

    def cancel_ticket(self):
        """Cancel a booked ticket."""
        if not self.account.bookings:
            print("❌ No bookings found!")
            return

        print("\nYour Bookings:")
        for idx, (ticket_id, movie) in enumerate(self.account.bookings, start=1):
            print(f"{idx}. {movie} (Ticket ID: {ticket_id})")

        try:
            choice = int(input("Enter the ticket number to cancel: ")) - 1
            if 0 <= choice < len(self.account.bookings):
                canceled_ticket = self.account.bookings.pop(choice)
                print(f"✅ Ticket {canceled_ticket[1]} (ID: {canceled_ticket[0]}) canceled successfully!")
            else:
                print("❌ Invalid selection. Try again.")
        except ValueError:
            print("❌ Invalid input. Enter a valid number.")

    def previous_bookings(self):
        """Display past bookings."""
        if not self.account.bookings:
            print("❌ No previous bookings found!")
            return

        print("\n📜 Your Previous Bookings:")
        for ticket_id, movie in self.account.bookings:
            print(f"🎟️ {movie} (Ticket ID: {ticket_id})")

    def show_balance(self):
        """Show user balance."""
        print(f"💰 Your current balance: ₹{self.account.balance}")

    def view(self):
        """Main menu loop."""
        while True:
            print("\n=================== Manage Your Tickets ===================")
            for instr in self.menu_list:
                print(instr)

            choice = input("\nEnter Your Choice: ").strip()

            if not choice.isdigit():
                print("❌ Invalid choice. Please enter a number.")
                continue

            choice = int(choice)

            if choice == 1:
                self.book_ticket()

            elif choice == 2:
                self.show_shows()

            elif choice == 3:
                self.cancel_ticket()

            elif choice == 4:
                self.previous_bookings()

            elif choice == 5:
                self.account.view()

            elif choice == 6:
                self.show_balance()

            elif choice == 7:
                print("🚪 Exiting User Home...")
                break

            else:
                print("❌ Please enter a valid choice...")

# Example usage
if __name__ == "__main__":
    user_home_view = UserHomeView()
    user_home_view.view()
