
class Animal:
    def __init__(self,name):
        self.name=name

    def sound_animal(self):
        if self.name=="dog":
            print("woof")
        elif self.name=="cat":
            print("meow")

mydog = Animal("cat")
mydog.sound_animal()


class Animal2:
    def __init__(self,name):
        self.name=name
    def sound(self):
        pass

class Cat(Animal2):
    def sound(self):
        print( self.name+ ' has meow sound')

class Dog(Animal2):
    def sound(self):
        print(self.name + ' has woof sound')

mydog = Dog("dog")
mydog.sound()

myCat = Cat('pishi')
myCat.sound()