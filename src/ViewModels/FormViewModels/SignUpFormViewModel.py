class SignUpFormViewModel:
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
        self._user_name = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        self._contact = value

    # Commands
    def create_user_command(self):
        _new_user = User(
            user_name=self.user_name,
            password=self.password,
            email=self.email,
            contact=self.contact
        )

        is_valid_registration = self.is_valid_registration(_new_user)
        if is_valid_registration["IsSuccessful"]:
            User.create_new_user(_new_user)
            is_valid_registration["Message"] = "User Created Successfully. Press Any Key To Continue..."
            return is_valid_registration
        return is_valid_registration

    def is_valid_registration(self, _new_user):
        is_valid_registration = User.is_valid_user_registration(_new_user)

        if is_valid_registration["IsSuccessful"]:
            is_valid_registration["Value"] = True
            is_valid_registration["IsSuccessful"] = True
            return is_valid_registration

        return is_valid_registration

    def reset_form_command(self):
        self.user_name = ""
        self.email = ""
        self.contact = ""
        self.password = ""

    # Static instance for Singleton Pattern (optional)
    @staticmethod
    def instance():
        if not hasattr(SignUpFormViewModel, "_instance"):
            SignUpFormViewModel._instance = SignUpFormViewModel()
        return SignUpFormViewModel._instance


# Assuming User class and methods are already implemented
class User:
    def __init__(self, user_name, password, email, contact):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.contact = contact

    @staticmethod
    def create_new_user(_new_user):
        # Logic to create a new user in the system
        print(f"Creating user: {vars(_new_user)}")

    @staticmethod
    def is_valid_user_registration(_new_user):
        # Logic to validate user registration
        if not _new_user.user_name or not _new_user.password:
            return {"IsSuccessful": False, "Message": "Username or Password cannot be empty."}
        return {"IsSuccessful": True, "Message": "User is valid."}


# Example Usage
if __name__ == "__main__":
    sign_up_view_model = SignUpFormViewModel.instance()
    sign_up_view_model.user_name = "john_doe"
    sign_up_view_model.password = "password123"
    sign_up_view_model.email = "john@example.com"
    sign_up_view_model.contact = "1234567890"

    result = sign_up_view_model.create_user_command()
    print(result["Message"])  # Example output message

    # Reset form
    sign_up_view_model.reset_form_command()
    print(f"Form reset: {sign_up_view_model.user_name}, {sign_up_view_model.email}")
