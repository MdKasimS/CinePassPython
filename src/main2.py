class Program:
    def __init__(self):
        self.choice = 0
        self.MenuList = [
            "1. Start View",
            "2. Home View",
            "3. Manage Ticket View",
            "4. SignUp View",
            "5. User Home View",
            "6. User Management View",
            "7. Account View",
            "8. Forgot Password View",
            "9. Exit",
            "10. Admin Home View"
        ]

    def view(self):
        while True:  # Infinite loop until a valid choice is made
            print("\nMenu Options:")
            for menuItem in self.MenuList:
                print(menuItem)

            try:
                self.choice = int(input("Please enter your choice: "))
                if 1 <= self.choice <= 10:
                    print(f"You selected: {self.MenuList[self.choice - 1]}")
                    if self.choice == 9:  # Exit condition
                        print("Exiting program...")
                        break
                else:
                    print("Please enter a number between 1 and 10.")

            except ValueError:
                print("Invalid input. Please enter a valid integer.")

# Example usage
if __name__ == "__main__":
    program = Program()
    program.view()
