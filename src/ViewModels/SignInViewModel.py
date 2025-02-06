import re


# Singleton Credential Class
class Credential:
    _instance = None  # Private instance for Singleton pattern

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Credential, cls).__new__(cls)
            cls._instance._login_id = ""
            cls._instance._password = ""
        return cls._instance

    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value


# Result Class (For Authentication Response)
class Result:
    def __init__(self, is_successful, message):
        self.is_successful = is_successful
        self.message = message

    def __repr__(self):
        return f"Result(success={self.is_successful}, message='{self.message}')"


# AuthenticationService Class
class AuthenticationService:

    @staticmethod
    def authenticate_user_for_given_credential():
        """
        Authenticate the user with the provided login credentials.
        Replace this with actual database verification logic.
        """
        if Credential().login_id == "user@example.com" and Credential().password == "password123":
            return Result(True, "✅ Authentication successful")
        else:
            return Result(False, "❌ Invalid credentials")

    @staticmethod
    def is_valid_email(email):
        """Validate the email format using regex."""
        if not email:
            return Result(False, "❌ Email is required")

        # Fixed Regular Expression for valid emails
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return Result(True, "✅ Valid email format")
        else:
            return Result(False, "❌ Invalid email format")


# SignInViewModel Class
class SignInViewModel:
    def __init__(self):
        self.credential = Credential()

    def set_sign_in_id(self, email):
        """Set login ID (email)."""
        self.credential.login_id = email

    def set_sign_in_password(self, password):
        """Set user password."""
        self.credential.password = password

    def forgot_password(self):
        """Stub for forgot password functionality."""
        print("🔄 Forgot password functionality is not implemented yet.")

    def sign_in(self):
        """Authenticate user."""
        return AuthenticationService.authenticate_user_for_given_credential()

    def reset_form_command(self):
        """Reset login credentials."""
        self.credential.login_id = ""
        self.credential.password = ""

    def are_all_credentials_available(self):
        """Check if all credentials are entered and valid."""
        if not self.credential.login_id or not self.credential.password:
            print("⚠️ All fields are required.")
            return False

        email_validation = AuthenticationService.is_valid_email(self.credential.login_id)
        if not email_validation.is_successful:
            print(email_validation.message)
            return False

        return True


# Example usage
if __name__ == "__main__":
    sign_in_view_model = SignInViewModel()

    # Example Credentials
    sign_in_view_model.set_sign_in_id("user@example.com")
    sign_in_view_model.set_sign_in_password("password123")

    if sign_in_view_model.are_all_credentials_available():
        result = sign_in_view_model.sign_in()
        print(result)
    else:
        sign_in_view_model.reset_form_command()
