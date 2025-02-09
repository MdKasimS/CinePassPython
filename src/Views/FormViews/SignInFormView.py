from src.Classes.Base.ABaseView import ABaseView


class SignInFormView(ABaseView):

    def View(self):

        while self.Choice != len(self.MenuList):

            print("\n\t----- !!! Salam Hindusthan !!! -----")
            print("================================================")
            print("🏠 Sign In - CineComplex")
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

        self.Menu = {}

        self.Choice = 0
