class User:
    """A Domain Entity representing a User in the system."""

    def __init__(self, user_id: int, name: str, email: str, password: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(id={self.user_id}, name={self.name}, email={self.email}, password={self.password})"
