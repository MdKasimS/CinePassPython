from sqlalchemy.orm import Session
from Models.User import User
from werkzeug.security import check_password_hash

class SignInViewModel:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def authenticate_user(self, email: str, password: str):
        user = self.db_session.query(User).filter(User.email == email).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None

    def __repr__(self):
        return "SignInViewModel(Handles user authentication operations)"