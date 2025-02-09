from Views.StartView import StartView
from src.Models.SQLInteraction import SQLInteraction

class Program:
    def __init__(self):
        self.App = StartView()

# Example usage
if __name__ == "__main__":
    sql = lambda: SQLInteraction()
    program = Program()
    program.App.View()
