
class User:
    """A simple attempt to model a webpage user."""
    
    def __init__(self, first, last, age):
        """Initialize the users attributes."""
        self.first = first
        self.last = last
        self.age = age

    def create_username(self):
        """Creates username out of first, last, and age attributes."""
        username = f"{self.first}{self.last}{self.age}"
        return username
    
    def welcome_user(self):
        """Welcomes a user to the webpage."""
        print(f"{self.first.title()}, welcome to the site.")

class Admin(User):
    """A simple attempt to model a webpage admin."""
    
    def __init__(self, first, last, age):
        """Initializes the attributes of the parent class."""
        super().__init__(first, last, age)

    def welcome_admin(self):
        """Welcomes the admin to the webpage."""
        print(f"{self.first.title()}, you are an admin. Welcome!")

class Privileges(Admin):
    """A simple attempt to model the privileges of an admin."""

    def __init__(self, first, last, age):
        """Initializes the attributes of the parent class."""
        super().__init__(first, last, age)

    def inform_privileges(self):
        """Informs certain admins of their privileges."""
        print(f"{self.first.title()}, you are an admin with privileges.")

    def show_privileges(self):
        """Shows an admin a list of privileges that they have."""
        admin_privileges = ['can add a post', 'can delete a post', 'can ban user']
        print(f"Admin Privileges: {admin_privileges}")

user_1 = User('taylor', 'stone', 28)
print(f"User 1: {user_1.create_username()}")
user_1.welcome_user()

user_2 = Admin('regis', 'pelletier', 29)
print(f"User 2: {user_2.create_username()}")
user_2.welcome_admin()

user_3 = Privileges('raul', 'gomez', 56)
print(f"User 3: {user_3.create_username()}")
user_3.inform_privileges()
user_3.show_privileges()