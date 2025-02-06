import getpass


class Credential:
    """Mock Credential class for storing logged-in user ID."""
    Instance = None  # Singleton pattern (for simplicity)

    def __init__(self, login_id):
        self.LoginId = login_id
        Credential.Instance = self


class AccountView:
    def __init__(self, login_id):
        self.login_id = login_id
        self.user_name = "John Doe"
        self.email = "johndoe@example.com"
        self.contact = "9876543210"
        self.password = "securepassword"
        self.menu_list = [
            "1. View User Name",
            "2. View Email",
            "3. View Contact",
            "4. Change Password",
            "5. Show Bookings",
            "6. Update Details",
            "7. Exit"
        ]

    def show_details(self):
        """Display the stored account details."""
        print(f"\nYour Account - UID {self.login_id}")
        print(f"Name: {self.user_name}")
        print(f"Email: {self.email}")
        print(f"Contact: {self.contact}")

    def change_password(self):
        """Handle password change securely."""
        current_password = getpass.getpass("Enter current password: ")
        if current_password != self.password:
            print("Incorrect password! Try again.")
            return
        new_password = getpass.getpass("Enter new password: ")
        confirm_password = getpass.getpass("Confirm new password: ")
        if new_password == confirm_password:
            self.password = new_password
            print("Password changed successfully!")
        else:
            print("Passwords do not match!")

    def update_details(self):
        """Allow the user to update their details."""
        print("\nUpdate Details:")
        self.user_name = input("Enter new User Name: ").strip() or self.user_name
        self.email = input("Enter new Email: ").strip() or self.email
        self.contact = input("Enter new Contact: ").strip() or self.contact
        print("Details updated successfully!")

    def show_bookings(self):
        """Mock function to display user bookings."""
        print("\nYour Bookings:")
        print("1. Avengers: Endgame - Seat A12")
        print("2. Interstellar - Seat B8")
        print("3. Inception - Seat C15")

    def view(self):
        """Display the account menu and handle user input."""
        while True:
            print("\n=================== Account Menu ===================")
            self.show_details()
            print("\nMenu:\n" + "\n".join(self.menu_list))

            choice = input("\nEnter Your Choice: ").strip()
            if not choice.isdigit():
                print("Invalid choice, please enter a number.")
                continue

            choice = int(choice)

            if choice == 1:
                print(f"User Name: {self.user_name}")

            elif choice == 2:
                print(f"Email: {self.email}")

            elif choice == 3:
                print(f"Contact: {self.contact}")

            elif choice == 4:
                self.change_password()

            elif choice == 5:
                self.show_bookings()

            elif choice == 6:
                self.update_details()

            elif choice == 7:
                print("Exiting Account Menu...")
                break

            else:
                print("Please enter a valid choice...")


# Example usage
if __name__ == "__main__":
    user_id = "U12345"  # Simulated logged-in user ID
    Credential(user_id)  # Store in mock Credential class
    account_view = AccountView(user_id)
    account_view.view()
