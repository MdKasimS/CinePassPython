# Refactored main.py

from Views import StartView
from src.Views.FormViews.SignInFormView import SignInFormView


class Program:
    def __init__(self):
        self.App = SignInFormView()

# Example usage
if __name__ == "__main__":
    program = Program()
    program.App.View()
