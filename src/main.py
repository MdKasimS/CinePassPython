# Refactored main.py


from src.Views.FormViews.SignInFormView import SignInFormView
from src.Views.StartView import StartView


class Program:
    def __init__(self):
        self.App = StartView()

# Example usage
if __name__ == "__main__":
    program = Program()
    program.App.View()
