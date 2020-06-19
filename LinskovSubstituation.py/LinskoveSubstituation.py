"""
In simpler terms means that a subclass, child or specialization of an object 
or class must be suitable by its Parent or SuperClass.
"""

# befor 

class Bird:
    def __init__(self,name):
        self.name=name

    def fly(self):
        print(f'the {self.name} is fly')

o1 = Bird('eagle')
o1.fly()
o2 = Bird('penguein') 
o2.fly()

# after

class Bird2:
    def __init__(self,name):
        self.name=name

class FlyBird(Bird2):
    def fly(self):
        print(f' the {self.name} is fly')

ob1= Bird2('penguin')
obj2 = FlyBird('eagle')
obj2.fly()