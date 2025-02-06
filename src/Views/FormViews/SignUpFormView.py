import getpass
import re


class SignUpFormViewModel:
    def __init__(self):
        self.user_name = ""
        self.email = ""
        self.contact = ""
        self.password = ""

    def create_user(self):
        """Simulate user creation process with validation."""
        if not (self.user_name and self.email and self.contact and self.password):
            return {"IsSuccessful": False, "Message": "Please fill all fields!"}

        if not self.validate_email(self.email):
            return {"IsSuccessful": False, "Message": "Invalid email format!"}

        if not self.contact.isdigit() or len(self.contact) < 10:
            return {"IsSuccessful": False, "Message": "Invalid contact number!"}

        return {"IsSuccessful": True, "Message": "User created successfully!"}

    def reset_form(self):
        """Reset the form data."""
        self.__init__()

    @staticmethod
    def validate_email(email):
        """Validate email format."""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email)


class SignUpFormView:
    def __init__(self):
        self.view_model = SignUpFormViewModel()
        self.menu_list = [
            "1. Enter Name",
            "2. Enter Email",
            "3. Enter Contact",
            "4. Enter Password",
            "5. Sign Up",
            "6. Reset",
            "7. Exit",
        ]

    def show_form_data(self):
        """Display the entered form data."""
        print(f"Entered Name: {self.view_model.user_name}")
        print(f"Entered Email: {self.view_model.email}")
        print(f"Entered Contact: {self.view_model.contact}")
        print(f"Entered Password: {'*' * len(self.view_model.password)}")

    def view(self):
        """Display the SignUp form and handle user input."""
        while True:
            print("\n=================== Sign Up - CineComplex ===================")
            self.show_form_data()
            print("\nMenu:\n" + "\n".join(self.menu_list))

            choice = input("\nEnter Your Choice: ").strip()
            if not choice.isdigit():
                print("Invalid choice, please enter a number.")
                continue

            choice = int(choice)

            if choice == 1:
                self.view_model.user_name = input("Enter User Name: ").strip()

            elif choice == 2:
                self.view_model.email = input("Enter Email: ").strip()

            elif choice == 3:
                self.view_model.contact = input("Enter Contact: ").strip()

            elif choice == 4:
                self.view_model.password = getpass.getpass("Enter Password: ")  # Hides input

            elif choice == 5:
                result = self.view_model.create_user()
                print(result["Message"])
                if result["IsSuccessful"]:
                    self.view_model.reset_form()

            elif choice == 6:
                self.view_model.reset_form()
                print("Form data has been reset.")

            elif choice == 7:
                print("Exiting Sign-Up Form...")
                break

            else:
                print("Please enter a valid choice...")


# Example usage
if __name__ == "__main__":
    sign_up_view = SignUpFormView()
    sign_up_view.view()
