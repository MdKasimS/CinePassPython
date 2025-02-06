from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import hashlib

Base = declarative_base()

# Assuming a result wrapper is needed for handling responses
class Result:
    def __init__(self, is_successful, value, message):
        self.is_successful = is_successful
        self.value = value
        self.message = message


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)  # This is password_hash, not plain password
    email = Column(String, nullable=False)
    contact = Column(String, nullable=False)

    @staticmethod
    def create_new_user(session, new_user):
        try:
            session.add(new_user)
            session.commit()

            # Add Auth record
            auth = Auth(user_id=new_user.id, password=new_user.password, privilege_level=0)
            session.add(auth)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error creating new user: {e}")

    @staticmethod
    def are_all_fields_for_registration_available(new_user):
        if not all([new_user.username, new_user.password, new_user.email, new_user.contact]):
            return Result(False, False, "All fields are required. Press any key to continue...")
        return Result(True, True, "")

    @staticmethod
    def is_valid_user_registration(session, new_user):
        is_valid_result = User.are_all_fields_for_registration_available(new_user)
        if not is_valid_result.is_successful:
            return is_valid_result

        # Validate email format
        is_valid_result = AuthenticationService.is_valid_email(new_user.email)
        if not is_valid_result.is_successful:
            return is_valid_result

        return AuthenticationService.authorize_new_user(session, new_user)


# Assuming Auth class for creating user authorization records
class Auth(Base):
    __tablename__ = 'auths'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    password = Column(String, nullable=False)
    privilege_level = Column(Integer, nullable=False)

# Assuming AuthenticationService to handle some of the logic
class AuthenticationService:
    @staticmethod
    def is_valid_email(email):
        if '@' not in email:
            return Result(False, False, "Invalid email address format.")
        return Result(True, True, "")

    @staticmethod
    def authorize_new_user(session, new_user):
        # Simulate password hashing and authorization
        hashed_password = hashlib.sha256(new_user.password.encode()).hexdigest()
        new_user.password = hashed_password
        User.create_new_user(session, new_user)
        return Result(True, True, "User successfully registered.")

# Example usage
if __name__ == "__main__":
    engine = create_engine('sqlite:///cinecomplex.db')  # Replace with actual database URL
    Session = sessionmaker(bind=engine)
    session = Session()

    new_user = User(username="john_doe", password="secure_password", email="john@example.com", contact="1234567890")
    
    validation_result = User.is_valid_user_registration(session, new_user)
    if validation_result.is_successful:
        print(validation_result.message)
    else:
        print(validation_result.message)
