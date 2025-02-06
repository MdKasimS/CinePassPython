class Auth:
    def __init__(self, user_id: int, password: str, privilege_level: int):
        self.user_id = user_id
        self.password = password
        self.privilege_level = privilege_level

    def __repr__(self):
        return f"Auth(UserId={self.user_id}, PrivilegeLevel={self.privilege_level})"
