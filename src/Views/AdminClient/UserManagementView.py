from tabulate import tabulate
import psycopg2
from typing import List

# PostgreSQL connection configuration
DB_CONFIG = {
    "dbname": "your_database",
    "user": "your_user",
    "password": "your_password",
    "host": "localhost",
    "port": "5432",
}

class User:
    def __init__(self, user_id, username, contact, email):
        self.user_id = user_id
        self.username = username
        self.contact = contact
        self.email = email

class UserManagementView:
    def __init__(self):
        self.choice = 0
        self.menu_list = []

    def get_connection(self):
        """Establish and return a PostgreSQL database connection."""
        return psycopg2.connect(**DB_CONFIG)

    def load_menu_list(self):
        """Load the menu options for user management."""
        self.menu_list = [
            "1. Show Users",
            "2. Create User",
            "3. Update User",
            "4. Block User",
            "5. Delete User",
            "6. Show User Bookings",
            "7. Exit"
        ]

    def view(self):
        """Display the User Management menu and handle user input."""
        self.load_menu_list()

        while True:
            print("\t----- !!! Salam Hindusthan !!! -----")
            print("================================================")
            print("\nManage Users - CineComplex")
            print("-------------------------------------------------")

            print("\nMenu:")
            print("---------------")

            for instr in self.menu_list:
                print(instr)

            choice = input("Enter Your Choice: ")
            try:
                self.choice = int(choice)
            except ValueError:
                print("Invalid choice, please try again.")
                continue

            if self.choice == 1:
                self.display_all_users()

            elif self.choice == 2:
                print("Creating user...")
                # Implement user creation logic

            elif self.choice == 3:
                print("Updating user...")
                # Implement user update logic

            elif self.choice == 4:
                print("Blocking user...")
                # Implement block user logic

            elif self.choice == 5:
                print("Deleting user...")
                # Implement delete user logic

            elif self.choice == 6:
                print("Displaying user bookings...")
                # Implement user bookings display logic

            elif self.choice == 7:
                print("Exiting User Management...")
                break

            else:
                print("Please enter a valid choice...")

    def display_all_users(self):
        """Display all users from the database in a paginated format."""
        users = self.get_users_from_db()

        if users:
            page_size = 10
            current_page = 0
            has_more_pages = True
            while has_more_pages:
                print("\nPage", current_page + 1)
                table_data = []
                paged_users = users[current_page * page_size:(current_page + 1) * page_size]

                for user in paged_users:
                    table_data.append([user.user_id, user.username, user.contact, user.email])

                print(tabulate(table_data, headers=["Id", "UserName", "Contact", "Email"], tablefmt="grid"))
                print(f"\nShowing {len(table_data)} users out of {len(users)}")

                if len(paged_users) < page_size:
                    has_more_pages = False

                if has_more_pages:
                    print("\n1. Press Enter to view the next page")
                    print("2. Enter Id for Record Selection")
                    print("3. Type 3 to exit")
                    choice = input("Your choice: ")

                    if choice == "3":
                        break
                    elif choice == "2":
                        record_id = input("Enter the User ID to select the record: ")
                        # Logic to handle the selected record
                    else:
                        current_page += 1
                else:
                    break
        else:
            print("No users found.")

    def get_users_from_db(self) -> List[User]:
        """Fetch users dynamically from PostgreSQL database."""
        users = []
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, contact, email FROM users;")
            rows = cursor.fetchall()
            for row in rows:
                users.append(User(*row))
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(f"Database error: {e}")
        return users

# Example usage:
if __name__ == "__main__":
    user_management_view = UserManagementView()
    user_management_view.view()
