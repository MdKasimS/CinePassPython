from sqlalchemy.orm import Session
from Models.User import User
from werkzeug.security import generate_password_hash

class ForgotPasswordFormViewModel:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def reset_password(self, email: str, new_password: str):
        user = self.db_session.query(User).filter(User.email == email).first()
        if user:
            user.password_hash = generate_password_hash(new_password)
            self.db_session.commit()
            return True
        return False

    def __repr__(self):
        return "ForgotPasswordFormViewModel(Handles password reset operations)"
