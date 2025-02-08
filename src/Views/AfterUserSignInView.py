# Refactored AfterUserSignInView.py

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

            choice = input("Enter Your Choice: ").strip()

            if not choice.isdigit():
                print("❌ Invalid choice. Please enter a number.")
                continue

            choice = int(choice)

            if choice == 1:
                print("🔗 Redirecting to Dashboard...")
                break  # You can integrate UserHomeView here.

            elif choice == 2:
                self.view_profile()

            elif choice == 3:
                print("🚪 Logging out...")
                break  # Ends session

            else:
                print("❌ Invalid selection. Try again.")

# Example Usage
if __name__ == "__main__":
    user_view = AfterUserSignInView("JohnDoe")
    user_view.after_sign_in()
