# Refactored StartView.py

from HomeView import HomeView  # ✅ Import HomeView

class StartView:
    def __init__(self):
        self.choice = 0
        self.menu_list = []

    def load_menu_list(self):
        self.menu_list = [
            "1. Login",
            "2. Register",
            "3. Forgot Password",
            "4. Create View And ViewModel Files",
            "5. Exit"
        ]

    def view(self):
        self.load_menu_list()

        while True:  # main loop
            print("\t----- !!! Salam Hindusthan !!! -----")
            print("================================================")
            print("\nStart - CineComplex")
            print("-------------------------------------------------")
            print("\nMenu : ")
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
                home_view = HomeView()  # ✅ Corrected initialization
                home_view.view()

            elif self.choice == 2:
                forgot_password_view = ForgotPasswordFormView()  # ✅ Corrected initialization
                forgot_password_view.view()

            elif self.choice == 3:
                print("Forgot Password logic to be implemented.")

            elif self.choice == 4:
                print("Create View and ViewModel Files logic to be implemented.")

            elif self.choice == 5:
                break  # Exit the loop and program

            else:
                print("Please enter a valid choice...")

# Example usage
if __name__ == "__main__":
    start_view = StartView()
    start_view.view()
