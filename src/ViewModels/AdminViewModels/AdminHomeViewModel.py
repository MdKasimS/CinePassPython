class AdminHomeViewModel:
    def __init__(self):
        # Ensure session_token_id is initialized properly
        credential_instance = Credential.instance()
        self._session_token_id = credential_instance.session_token_id if credential_instance.session_token_id else None

    def sign_out(self):
        if self._session_token_id:
            SessionService.terminate_session(self._session_token_id)
            self._session_token_id = None  # Invalidate session locally
        else:
            print("No active session to terminate.")

# Singleton class for Credential Management
class Credential:
    _instance = None

    def __init__(self):
        self.session_token_id = None

    @staticmethod
    def instance():
        if Credential._instance is None:
            Credential._instance = Credential()
        return Credential._instance

    def set_session_token(self, token_id):
        """Set a new session token when a user logs in."""
        self.session_token_id = token_id

    def clear_session_token(self):
        """Clear session token when user logs out."""
        self.session_token_id = None

class SessionService:
    @staticmethod
    def terminate_session(session_token_id):
        if session_token_id:
            print(f"Session with token {session_token_id} has been terminated.")
            Credential.instance().clear_session_token()
        else:
            print("No valid session found to terminate.")
