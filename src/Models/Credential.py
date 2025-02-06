class Credential:
    _instance = None

    def __init__(self):
        if Credential._instance is not None:
            raise Exception("This class is a singleton! Use get_instance() method.")
        self._login_id = None
        self._password = None
        self._session_token_id = None
        Credential._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Credential()
        return cls._instance

    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def session_token_id(self):
        return self._session_token_id

    @session_token_id.setter
    def session_token_id(self, value):
        self._session_token_id = value

    def __repr__(self):
        return f"Credential(LoginId={self._login_id}, SessionTokenId={self._session_token_id})"

# Example usage:
if __name__ == "__main__":
    cred1 = Credential.get_instance()
    cred1.login_id = "user@example.com"
    cred1.password = "securepassword"
    cred1.session_token_id = "abc123"

    cred2 = Credential.get_instance()  # This will return the same instance
    print(cred1)  # Credential(LoginId=user@example.com, SessionTokenId=abc123)
    print(cred2)  # Same instance as cred1
