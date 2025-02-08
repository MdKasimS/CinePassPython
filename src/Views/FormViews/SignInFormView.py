from abc import ABC

from src.Classes.Base.ABaseView import ABaseView


class SignInFormView(ABaseView):

    def View(self):
        while self.Choice != len(self.MenuList):

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

            # if(self.Menu.keys()choice
            self.Choice = int(choice)


    def __init__(self):
        super().__init__()
        self.MenuList = [
            "1. Enter Login Id ",
            "2. Enter Password ",
            "3. Login ",
            "4. Sign Up ",
            "5. Forgot Password ",
            "6. Reset Form ",
            "7. Exit",
        ]
        self.Menu = {

        }
        self.Choice = 0