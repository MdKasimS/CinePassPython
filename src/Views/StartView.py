# Refactored StartView.py

from src.Classes.Base.ABaseView import ABaseView
from src.Views.FormViews.ForgotPasswordFormView import ForgotPasswordFormView
from src.Views.FormViews.SignInFormView import SignInFormView


class StartView(ABaseView):
    def __init__(self):
        super().__init__()
        self.MenuList = [
            "1. Login",
            "2. Sign Up",
            "3. Forgot Password",
            "4. Exit"
        ]
        self.Menu = {
            1: SignInFormView.View,
            # 2: SignUpFormView.View,
            3: ForgotPasswordFormView.View,
        }

    def View(self):

        while self.Choice!= len(self.Menu):
            print("\n\t----- !!! Salam Hindusthan !!! -----")
            print("================================================")
            print("🏠 Home - CineComplex")
            print("-------------------------------------------------")
            print("\nMenu:")
            print("---------------")

            for instr in self.MenuList:
                print(instr)

            choice = input("🎯 Enter Your Choice: ").strip()
            if not choice.isdigit():
                print("❌ Invalid choice. Please enter a number.")
                continue

            self.Choice = int(choice)

            app = self.Menu[self.Choice]
            app()
