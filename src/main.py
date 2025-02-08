# Refactored main.py

from Views import StartView
from Views import HomeView
from Views.ManageTicketsView import ManageTicketsView
from Views.FormViews import SignUpFormView, ForgotPasswordFormView
from Views.UserClient import UserHomeView, AccountView

class Program:
    def __init__(self):
        self.choice = 0
        self.MenuList = [
            "1. Start View",
            "2. Home View",
            "3. Manage Ticket View",
            "4. SignUp View",
            "5. User Home View",
            "6. User Management View",
            "7. Account View",
            "8. Forgot Password View",
            "9. Exit",
            "10. Admin Home View"
        ]

    def view(self):
        while True:  # Infinite loop until exit
            print("\n================ Menu Options ================")
            for menuItem in self.MenuList:
                print(menuItem)

            try:
                self.choice = int(input("Please enter your choice: "))
                if self.choice == 1:
                    StartView().view()
                elif self.choice == 2:
                    HomeView().view()
                elif self.choice == 3:
                    ManageTicketsView().view()
                elif self.choice == 4:
                    SignUpFormView().view()
                elif self.choice == 5:
                    UserHomeView().view()
                elif self.choice == 6:
                    UserManagementView().view()
                elif self.choice == 7:
                    AccountView().view()
                elif self.choice == 8:
                    ForgotPasswordFormView().view()
                elif self.choice == 9:
                    print("👋 Exiting program... Thank you for using CineComplex!")
                    break
                elif self.choice == 10:
                    AdminHomeView().view()
                else:
                    print("❌ Please enter a number between 1 and 10.")

            except ValueError:
                print("❌ Invalid input. Please enter a valid integer.")

# Example usage
if __name__ == "__main__":
    program = Program()
    program.view()
