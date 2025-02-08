# Refactored ForgotPasswordFormView.py

import psycopg2
import bcrypt

# PostgreSQL connection configuration
DB_CONFIG = {
    "dbname": "your_database",
    "user": "your_user",
    "password": "your_password",
    "host": "localhost",
    "port": "5432",
}

class ForgotPasswordFormView:
    def __init__(self):
        self.choice = 0
        self.menu_list = []
        self.user_id = None

    def get_connection(self):
        """Establish and return a PostgreSQL database connection."""
        return psycopg2.connect(**DB_CONFIG)

    def load_menu_list(self):
        """Load the menu options for the Forgot Password screen."""
        self.menu_list = [
            "1. Enter User Id ",
            "2. Enter Email  ",
            "3. Enter Contact ",
            "4. Set New Password ",
            "5. Exit",
        ]

    def view(self):
        """Display the Forgot Password view and handle user choices."""
        self.load_menu_list()

        while True:
            print("\t----- !!! Salam Hindusthan !!! -----")
            print("================================================")
            print("Forgot Password: Enter Any Of The Detail")
            print("-------------------------------------------------")

            print("\nMenu: ")
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
                self.user_id = input("Enter User ID: ")
                if self.validate_user(field="id", value=self.user_id):
                    print("User ID verified.")
                else:
                    print("Invalid User ID. Please try again.")

            elif self.choice == 2:
                email = input("Enter Email: ")
                if self.validate_user(field="email", value=email):
                    print("Email verified.")
                else:
                    print("Invalid Email. Please try again.")

            elif self.choice == 3:
                contact = input("Enter Contact: ")
                if self.validate_user(field="contact", value=contact):
                    print("Contact verified.")
                else:
                    print("Invalid Contact. Please try again.")

            elif self.choice == 4:
                self.set_new_password_form_view()

            elif self.choice == 5:
                break  # Exit the loop and program

            else:
                print("Please enter a valid choice...")

    def validate_user(self, field, value):
        """Check if the user exists in the database based on the given field (id, email, contact)."""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"SELECT id FROM users WHERE {field} = %s", (value,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            if result:
                self.user_id = result[0]  # Store user_id if found
                return True
            return False
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return False

    def set_new_password_form_view(self):
        """Set a new password for the user."""
        if not self.user_id:
            print("Please verify your identity first (User ID, Email, or Contact).")
            return

        print("\nEnter New Password: ")
        new_password = input()
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET password = %s WHERE id = %s", (hashed_password, self.user_id))
            conn.commit()
            cursor.close()
            conn.close()
            print("Password has been successfully updated!")
        except psycopg2.Error as e:
            print(f"Error updating password: {e}")

# Example usage
if __name__ == "__main__":
    forgot_password_view = ForgotPasswordFormView()
    forgot_password_view.view()
