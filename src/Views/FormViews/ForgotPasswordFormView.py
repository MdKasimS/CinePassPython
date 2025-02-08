from src.Classes.Base.ABaseView import ABaseView

class ForgotPasswordFormView(ABaseView):

    def View(self):
        """Display the Forgot Password view and handle user choices."""

        while True:
            print("\t----- !!! Salam Hindusthan !!! -----")
            print("================================================")
            print("Forgot Password: Enter Any Of The Detail")
            print("-------------------------------------------------")

            print("\nMenu: ")
            print("---------------")

            for instr in self.MenuList:
                print(instr)


    def __init__(self):
        super().__init__()
        self.Choice = 0
        self.MenuList = [

        ]
        self.Menu = {

        }



