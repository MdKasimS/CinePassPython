# Refactored HomeView.py

from Views.UserClient import UserHomeView

class HomeView:
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
        self.menu_list = [
            "1. User Login",
            "2. Admin Login",
            "3. CineComplex Login",
            "4. Exit"
        ]

    def view(self):
        self.load_menu_list()

        while True:  # main loop
            print("\n\t----- !!! Salam Hindusthan !!! -----")
            print("================================================")
            print("🏠 Home - CineComplex")
            print("-------------------------------------------------")
            print("\nMenu:")
            print("---------------")

            for instr in self.menu_list:
                print(instr)

            choice = input("🎯 Enter Your Choice: ").strip()
            if not choice.isdigit():
                print("❌ Invalid choice. Please enter a number.")
                continue

            self.choice = int(choice)

            if self.choice == 1:
                # Handle User Login
                username = SignInView().view("User")
                if username:
                    AfterUserSignInView(username).after_sign_in()

            elif self.choice == 2:
                # Handle Admin Login
                admin_name = SignInView().view("Admin")
                if admin_name:
                    print(f"✅ Welcome Admin: {admin_name}")  # Redirect to Admin Panel

            elif self.choice == 3:
                # Handle CineComplex Login
                owner_name = SignInView().view("CineComplex")
                if owner_name:
                    print(f"✅ Welcome Theatre Owner: {owner_name}")  # Redirect to CineComplex Panel

            elif self.choice == 4:
                print("👋 Exiting... Thank you for using CineComplex!")
                break

            else:
                print("❌ Please enter a valid choice.")


class SignInView:
    def view(self, user_type):
        """
        Handles sign-in logic for different user types.
        Returns username if login is successful, else None.
        """
        print(f"\n🔐 {user_type} Login")
        print("===========================")
        username = input("👤 Enter Username: ").strip()
        password = input("🔑 Enter Password: ").strip()

        # Simulating authentication
        if username and password:  # Add proper authentication later
            print(f"✅ {user_type} Login Successful!")
            return username
        else:
            print("❌ Invalid credentials. Please try again.")
            return None


class AfterUserSignInView:
    def __init__(self, username):
        """Initialize the view after user sign-in."""
        self.username = username
        self.menu_list = [
            "1. Continue to Dashboard",
            "2. View Profile",
            "3. Logout"
        ]

    def view_profile(self):
        """Mock function to display user profile."""
        print("\n===== Your Profile =====")
        print(f"👤 Username: {self.username}")
        print("📧 Email: user@example.com")
        print("📞 Contact: 9876543210")
        print("========================")

    def after_sign_in(self):
        """Display the options available after signing in."""
        while True:
            print(f"\n🎉 Welcome, {self.username}!")
            print("==============================")
            for option in self.menu_list:
                print(option)

            choice = input("🎯 Enter Your Choice: ").strip()

            if not choice.isdigit():
                print("❌ Invalid choice. Please enter a number.")
                continue

            choice = int(choice)

            if choice == 1:
                print("🔗 Redirecting to Dashboard...")
                UserHomeView().view()  # Assume UserHomeView exists

            elif choice == 2:
                self.view_profile()

            elif choice == 3:
                print("🚪 Logging out...")
                break  # Ends session

            else:
                print("❌ Invalid selection. Try again.")


# Example Usage
if __name__ == "__main__":
    home_view = HomeView()
    home_view.view()
