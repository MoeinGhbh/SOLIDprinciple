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


"""
Remarks on the LSP The LSP is fundamental to good object-oriented software design because 
it emphasizes one of its core traits — polymorphism. It is about creating correct hierarchies
 so that classes derived from a base one are polymorphic along with the parent one, with 
 respect to the methods on their interface. 
It is also interesting to notice how this principle relates to the previous one — if we attempt
 to extend a class with a new one that is incompatible, it will fail, the contract with the 
 client will be broken, and as a result, such an extension will not be possible (or, to make 
 it possible, we would have to break the other end of the principle and modify code in the 
 client that should be closed for modification, which is completely undesirable and
  unacceptable).  Carefully thinking about new classes in the way that LSP suggests helps us 
  to extend the hierarchy correctly. We could then say that LSP contributes to the OCP.
"""