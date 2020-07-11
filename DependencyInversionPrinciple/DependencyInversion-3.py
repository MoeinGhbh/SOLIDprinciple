class Manager:
    def __init__(self):
        self.developer=[]
        self.designer=[]
        self.tester=[]

    def adddeveloper(self,dev):
        self.developer.append(dev)

    def adddesigner(self,des):
        self.designer.append(des)

    def addtester(self,tes):
        self.tester.append(tes)

class Developer:
    def __init__(self):
        print("it is developer")

class Designer:
    def __init__(self):
        print("it is designer")

class Tester:
    def __init__(self):
        print("it is tester")


if __name__=='__main__':
    a= Manager()
    a.adddeveloper(Developer())
    a.adddeveloper(Designer())
    a.addtester(Tester())
