# Refactored Credential.py (Singleton Pattern)

class Credential:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Credential, cls).__new__(cls)
            cls._instance.LoginId = ""  # Store login ID
            cls._instance.Password = ""  # Store password
        return cls._instance

# Create Singleton Instance
Credential.Instance = Credential()
