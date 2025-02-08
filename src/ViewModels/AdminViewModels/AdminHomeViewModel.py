from sqlalchemy.orm import Session
from Models.User import User

class AdminHomeViewModel:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all_users(self):
        return self.db_session.query(User).all()

    def delete_user(self, user_id: int):
        user = self.db_session.query(User).filter(User.id == user_id).first()
        if user:
            self.db_session.delete(user)
            self.db_session.commit()
            return True
        return False

    def __repr__(self):
        return "AdminHomeViewModel(Handles user management operations)"