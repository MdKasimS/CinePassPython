from src.Classes.Base.ABaseView import ABaseView
from src.Views.FormViews.SignInFormView import SignInFormView
from src.Views.FormViews.SignUpFormView import SignUpFormView
import os
import sys


class StartView(ABaseView):
    def __init__(self):
        super().__init__()
        self.MenuList = ["1. Login", "2. Sign Up", "3. Forgot Password", "4. Exit"]
        self.Menu = {
            1: lambda: SignInFormView().View(),
            2: lambda: SignUpFormView().View(),
            # 3: lambda: ForgotPasswordFormView().View(),
        }

    def View(self):

        while self.Choice != len(self.MenuList):
            # os.system("cls")
            print("\n\t----- !!! Salam Hindusthan !!! -----")
            print("================================================")
            print("🏠 Home - CineComplex")
            print("-------------------------------------------------")
            print("\nMenu:")
            print("---------------")

            for instr in self.MenuList:
                print(instr)

            try:
                self.Choice = int(input("🎯 Enter Your Choice: ").strip())
            except Exception as e:
                print(f"Error : {e}")
                print("❌ Invalid choice. Please enter a number.")
                continue

            app = self.Menu.get(self.Choice)

            if app is not None:
                app()
