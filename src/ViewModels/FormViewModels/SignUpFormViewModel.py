from werkzeug.security import generate_password_hash

from src.Classes.Base.ABaseViewModel import ABaseViewModel
from src.Models.SQLInteraction import SQLInteraction
from src.Models.User import User


class SignUpFormViewModel(ABaseViewModel):
    def __init__(self):
        super().__init__()
        self.Name = ""
        self.Email = ""
        self.Contact = ""
        self.Password = ""


    def SignUp(self):

        existing_user = (SQLInteraction()
                         .Db.query(User)
                         .filter(User.email == self.Email).first())

        if existing_user:
            return False  # Email already exists

        new_user = User(
            username = self.Name,
            email = self.Email,
            password = generate_password_hash(self.Password),
            contact = self.Contact
        )

        SQLInteraction().Db.add(new_user)
        SQLInteraction().Db.commit()

        return True

    def SetUserName(self):
        self.Name = input("Enter User Name: ")

    def SetUserEmail(self):
        self.Email = input("Enter Email: ")

    def SetUserPassword(self):
        self.Password = input("Enter Password: ")

    def SetUserContact(self):
        self.Contact = input("Enter Contact: ")

    def ResetFormData(self):
        self.Name = ""
        self.Email = ""
        self.Password = ""
        self.Contact = ""



    def __repr__(self):
        return "SignUpFormViewModel(Handles user registration operations)"
