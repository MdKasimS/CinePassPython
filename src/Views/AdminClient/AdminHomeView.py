# Import required view models from the views package
from Views.SignInView import SignInView
from Views.UserClient import UserHomeView
from Views.AdminClient import AdminHomeView

class AdminHomeView:
    def __init__(self):
        self.choice = 0
        self.menu_list = []

    def load_menu_list(self):
        """Load the menu options for the Admin Home view."""
        self.menu_list = [
            "1. See Shows",
            "2. Manage Shows",
            "3. Manage Users",
            "4. Manage Admins",
            "5. Manage Tickets",
            "6. Manage CineComplexes",
            "7. Exit"
        ]

    def view(self):
        """Display the Admin Home menu and handle user input."""
        self.load_menu_list()

        while True:  # main loop
            print("\t----- !!! Salam Hindusthan !!! -----")
            print("================================================")
            print("\nHome - CineComplex")
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
                # Show all shows
                print("Displaying all shows...")
                # Implement logic to show shows

            elif self.choice == 2:
                # Manage show view
                print("Managing shows...")
                # Implement logic to manage shows

            elif self.choice == 3:
                # Manage User view
                print("Managing users...")
                # Call to manage users
                UserHomeView().view()

            elif self.choice == 7:
                # Sign out and reset the form
                print("Signing out...")
                AdminHomeView().sign_out()
                SignInView().reset_form_command()
                break  # Exit the loop after sign out

            else:
                print("Please enter a valid choice...")

# Example usage:
if __name__ == "__main__":
    admin_home_view = AdminHomeView()
    admin_home_view.view()
