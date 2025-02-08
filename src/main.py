from Views.StartView import StartView

class Program:
    def __init__(self):
        self.App = StartView()

# Example usage
if __name__ == "__main__":
    program = Program()
    print("Hello")
    program.App.View()
