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