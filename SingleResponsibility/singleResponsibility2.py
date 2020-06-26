'''
    creational pattern 
        Singleton
'''

class Singleton(type):
    _instance=None

    def __call__(self):
        if self._instance==None:
            self._instance==super().__call__()
        return self._instance

class DB(metaclass=Singleton):
    pass

dd = DB()
print(id(dd))

dd1 = DB()
print(id(dd1))