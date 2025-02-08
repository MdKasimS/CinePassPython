# Refactored ManageTicketsView.py

class ManageTicketsView:
    def __init__(self):
        self._choice = 0
        self.menu_list = []

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, value):
        self._choice = value

    def load_menu_list(self):
        """Loads the menu options."""
        self.menu_list = [
            "1. 🎟️ Book Ticket",
            "2. 🎭 Show Shows",
            "3. ❌ Cancel Tickets",
            "4. 📋 Previous Bookings",
            "5. 👤 Account",
            "6. 🚪 Exit"
        ]

    def book_ticket(self):
        """Handles ticket booking logic."""
        print("\n🎟️ Booking a Ticket...")
        # Implement ticket booking functionality

    def show_shows(self):
        """Displays available shows."""
        print("\n🎭 Available Shows:")
        # Implement show listing functionality

    def cancel_ticket(self):
        """Handles ticket cancellation."""
        print("\n❌ Cancelling a Ticket...")
        # Implement cancellation logic

    def previous_bookings(self):
        """Displays previous bookings."""
        print("\n📋 Viewing Previous Bookings...")
        # Implement previous bookings retrieval

    def account_details(self):
        """Displays user account details."""
        print("\n👤 Viewing Account Details...")
        # Implement account-related functionalities

    def view(self):
        """Main menu loop."""
        self.load_menu_list()

        while True:
            print("\n\t🎬 ----- !!! Salam Hindusthan !!! ----- 🎬")
            print("================================================")
            print("📌 Manage Tickets")
            print("-------------------------------------------------")
            print("\n📜 Menu:")
            print("---------------")

            for instr in self.menu_list:
                print(instr)

            choice = input("🎯 Enter Your Choice: ").strip()
            if not choice.isdigit():
                print("❌ Invalid input! Please enter a number.")
                continue

            self.choice = int(choice)

            if self.choice == 1:
                self.book_ticket()
            elif self.choice == 2:
                self.show_shows()
            elif self.choice == 3:
                self.cancel_ticket()
            elif self.choice == 4:
                self.previous_bookings()
            elif self.choice == 5:
                self.account_details()
            elif self.choice == 6:
                confirm_exit = input("⚠️ Are you sure you want to exit? (yes/no): ").strip().lower()
                if confirm_exit == "yes":
                    print("👋 Exiting... Thank you for using CineComplex!")
                    break
                else:
                    print("🔄 Returning to menu...")
            else:
                print("❌ Please enter a valid choice.")

# Example Usage:
if __name__ == "__main__":
    manage_tickets_view = ManageTicketsView()
    manage_tickets_view.view()
