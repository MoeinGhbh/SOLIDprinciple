"""We have a User class which is responsible for both the user properties and user 
database management. If the application changes in a way that it affect database 
management functions. The classes that make use of User properties will have to be
 touched and recompiled to compensate for the new changes. It’s like a domino effect,
 touch one card it affects all other cards in line."""

# befor:

class User1:
    def __init__(self,name:str):
        self.name=name

    def get_name(self)-> str:
        pass

    def save(self,user)->str:
       pass

# after

class User2:
    def __init__(self,name:str):
        self.name=name

    def get_name(self)-> str:
        pass

class UserDB:

    def get_user(self,id)->User2:
        pass 

    def save(self,user:User2)-> str:
        pass
