class AuthenticationError(Exception):
    def __init__(self, message="Authentication failed. Please check your credentials."):
        self.message = message
        super().__init__(self.message)


def login(user, password):
    correctUsername = "admin"
    correctPassword = "password123"

    if user != correctUsername or password != correctPassword:
        raise AuthenticationError("Invalid username or password.")


try:
    user = input("Enter username: ")
    password = input("Enter password: ")
    login(user, password)
    print("Login successful!")
except AuthenticationError as e:
    print(e)