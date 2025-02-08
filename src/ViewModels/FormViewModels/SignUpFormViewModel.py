from sqlalchemy.orm import Session
from Models.User import User
from werkzeug.security import generate_password_hash

class SignUpFormViewModel:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def register_user(self, username: str, email: str, password: str, contact: str):
        existing_user = self.db_session.query(User).filter(User.email == email).first()
        if existing_user:
            return False  # Email already exists

        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            contact=contact
        )
        self.db_session.add(new_user)
        self.db_session.commit()
        return True

    def __repr__(self):
        return "SignUpFormViewModel(Handles user registration operations)"
