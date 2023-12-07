from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, role):
        self.id = username
        self.role = role
    
    def getRole(self):
        return self.role