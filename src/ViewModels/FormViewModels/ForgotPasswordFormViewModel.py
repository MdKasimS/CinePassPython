import re
import hashlib

class ForgotPasswordFormViewModel:
    def __init__(self):
        self._user_name = None
        self._password = None
        self._email = None
        self._contact = None

    # Properties
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        if not value:
            raise ValueError("Username cannot be empty.")
        self._user_name = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not self._validate_password(value):
            raise ValueError("Password must be at least 8 characters long, contain a number and a special character.")
        self._password = self._hash_password(value)  # Store hashed password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not self._validate_email(value):
            raise ValueError("Invalid email format.")
        self._email = value

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        if not self._validate_contact(value):
            raise ValueError("Invalid contact number.")
        self._contact = value

    # Methods
    def set_new_password_for_user_id(self):
        if not self._user_name or not self._password:
            print("Error: Username and password must be set before resetting.")
            return False

        # Here, you would update the user's password in the database.
        # Example: Database.update_user_password(self.user_name, self.password)
        
        print(f"New password set successfully for user {self.user_name}")
        return True

    # Validation Methods
    def _validate_email(self, email):
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

    def _validate_contact(self, contact):
        return contact.isdigit() and len(contact) in [10, 12]

    def _validate_password(self, password):
        return (
            len(password) >= 8 and
            any(char.isdigit() for char in password) and
            any(char in "!@#$%^&*()-_+=" for char in password)
        )

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

# Example usage
if __name__ == "__main__":
    forgot_password_vm = ForgotPasswordFormViewModel()

    try:
        forgot_password_vm.user_name = "john_doe"
        forgot_password_vm.password = "NewPass@123"  # Secure password
        forgot_password_vm.email = "john@example.com"
        forgot_password_vm.contact = "1234567890"

        forgot_password_vm.set_new_password_for_user_id()  # Example method call
    except ValueError as e:
        print(f"Error: {e}")
