"""
Linear Insert/Search (Brute Force)
"""

# Classes

class User:
    def __init__(self, username: str, name: str, email: str):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0

        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1

        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

        print('User not found.')

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


# Main

if __name__ == '__main__':

    # Create users

    biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
    vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
    hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
    sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
    jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
    siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
    aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')

    # Create database

    database = UserDatabase()

    # Insert users

    database.insert(aakash)
    database.insert(biraj)
    database.insert(hemanth)
    database.insert(jadhesh)
    database.insert(siddhant)
    database.insert(sonaksh)
    database.insert(vishal)

    # Find user

    user = database.find('siddhant')
    print(user)

    # Update user

    database.update(User('sonaksh', 'Sonaksh Gandhi', 'sonaksh.gandhi@example.com'))
    user = database.find('sonaksh')
    print(user)

    # Show all users

    print(database.list_all())
