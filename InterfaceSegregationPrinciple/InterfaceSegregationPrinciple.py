"""
Another nice trick is that in our business logic, a single class can implement several 
interfaces if needed. So we can provide a single implementation for all the common methods 
between the interfaces. The segregated interfaces will also force us to think of our code 
more from the client’s point of view, which will in turn lead to loose coupling and easy 
testing. So, not only have we made our code better to our clients, we also made it easier 
for ourselves to understand, test and implement.
"""

# befor

from abc import ABC,abstractclassmethod

class Shap():
    def cicle(self):
        pass
    def rectangle(self):
        pass
    def square(self):
        pass

class Cicle(Shap):
    def cicle(self):
        pass
    def rectangle(self):
        pass
    def square(self):
        pass
class square(Shap):
    def cicle(self):
        pass
    def rectangle(self):
        pass
    def square(self):
        pass
class rectangle(Shap):
    def cicle(self):
        pass
    def rectangle(self):
        pass
    def square(self):
        pass

# after 

class Shap2(ABC):
    def draw(self):
        pass
class Cicle2(Shap2):
    def draw(self):
        pass
class  Rectangle2(Shap2):
    def draw(self):
        pass
class square2(Shap2):
    def draw(self):
        pass