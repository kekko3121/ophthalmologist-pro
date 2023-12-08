from flask_login import UserMixin

#A custom class that extends the UserMixin class provided by Flask-Login.
class User(UserMixin):
    def __init__(self, username, role):
        self.__id = username
        self.__role = role
    
    #return a id value to string
    def get_id(self):
        return str(self.__id)
    
    #return a Role value
    def getRole(self):
        return self.__role