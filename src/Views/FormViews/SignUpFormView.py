from src.Classes.Base.ABaseView import ABaseView
from src.ViewModels.FormViewModels.SignUpFormViewModel import SignUpFormViewModel


class SignUpFormView(ABaseView):

    def View(self):

        while self.Choice != len(self.MenuList):

            print("\n\t----- !!! Salam Hindusthan !!! -----")
            print("================================================")
            print("🏠 Sign Up - CineComplex")
            print("-------------------------------------------------")
            self.ShowFormData()
            print("-------------------------------------------------")
            print("\nMenu:")
            print("---------------")

            for instr in self.MenuList:
                print(instr)

            try:
                self.Choice = int(input("🎯 Enter Your Choice: ").strip())
            except:
                print("❌ Invalid choice. Please enter a number.")
                continue

            app = self.Menu.get(self.Choice)

            if app is not None:
                app()


    def __init__(self):
        super().__init__()
        self.MenuList = [
            "1. Enter Name",
            "2. Enter Email",
            "3. Enter Contact",
            "4. Enter Password",
            "5. Sign Up",
            "6. Reset Form ",
            "7. Exit",
        ]

        self.Menu = {
            1: lambda: SignUpFormViewModel().SetUserName(),
            2: lambda: SignUpFormViewModel().SetUserEmail(),
            3: lambda: SignUpFormViewModel().SetUserContact(),
            4: lambda: SignUpFormViewModel().SetUserPassword()
        }


    def ShowFormData(self):
        print(f"Enter Name:{SignUpFormViewModel().Name}")
        print(f"Enter Email:{SignUpFormViewModel().Email}")
        print(f"Enter Contact:{SignUpFormViewModel().Contact}")
        print(f"Enter Password:{SignUpFormViewModel().Password}")
