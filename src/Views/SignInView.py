# Refactored SignInView.py

import os
from Credential import Credential  # Ensure Credential.py exists


class SignInView:
    def __init__(self):
        self.choice = 0
        self.menu_list = []

    def load_menu_list(self):
        """Loads the menu options."""
        self.menu_list = [
            "1. 🆔 Enter Login ID",
            "2. 🔑 Enter Password",
            "3. ✅ Login",
            "4. 📝 Sign Up",
            "5. 🔄 Forgot Password",
            "6. 🔃 Reset Form",
            "7. 🚪 Exit"
        ]

    def clear_screen(self):
        """Clears the console screen for better UI experience."""
        os.system("cls" if os.name == "nt" else "clear")

    def view(self):
        """Main SignIn menu loop."""
        self.load_menu_list()

        while True:
            self.clear_screen()
            print("\n\t🎬 ----- !!! Salam Hindusthan !!! ----- 🎬")
            print("================================================")
            print("🔑 SignIn View - CineComplex")
            print("-------------------------------------------------")
            print(f"📌 Entered Login ID: {Credential.Instance.LoginId if Credential.Instance.LoginId else 'Not entered'}")
            print(f"📌 Entered Password: {'*' * len(Credential.Instance.Password) if Credential.Instance.Password else 'Not entered'}")
            print("\n📜 Menu:")
            print("---------------")

            for instr in self.menu_list:
                print(instr)

            choice = input("🎯 Enter Your Choice: ").strip()

            if not choice.isdigit():
                print("❌ Invalid choice! Please enter a number.")
                input("🔄 Press Enter to continue...")
                continue

            self.choice = int(choice)

            if self.choice == 1:
                print("🆔 Enter Login ID: ")
                SignInView.Instance.get_sign_in_id()
            elif self.choice == 2:
                print("🔑 Enter Password: ")
                SignInView.Instance.get_sign_in_password()
            elif self.choice == 3:
                print("🔍 Authenticating...")
                authentication_result = SignInView.Instance.sign_in()
                if authentication_result.is_successful:
                    print("✅ Login Successful! Redirecting to Admin Home...")
                    AdminHomeView.Instance.View()
                else:
                    print(f"❌ {authentication_result.message}")
                    input("🔄 Press Enter to continue...")
            elif self.choice == 4:
                print("📝 Redirecting to Sign-Up...")
                SignUpFormView.Instance.View()
            elif self.choice == 5:
                print("🔄 Redirecting to Forgot Password...")
                ForgotPasswordFormView.Instance.View()
            elif self.choice == 6:
                print("🔃 Resetting form...")
                SignInView.Instance.reset_form_command()
            elif self.choice == 7:
                confirm_exit = input("⚠️ Are you sure you want to exit? (yes/no): ").strip().lower()
                if confirm_exit == "yes":
                    print("👋 Exiting... Thank you for using CineComplex!")
                    break
            else:
                print("❌ Please enter a valid choice.")

# Example usage
if __name__ == "__main__":
    sign_in_view = SignInView()
    sign_in_view.view()
