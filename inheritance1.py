class User :
    name " "
    def __init__(self, name):
        self.name = name
        def printName(self):
            print "Name = " + self.name brian = User ("brian")
            brian.printName()

class Programmer(User):
    def __init__(self, name):
        self.name= name
    def doPython(self):
        print "programming PBO"

brian = User("brian")
brian.printName()
diana = Programmer ("Diana")
diana.printName()
diana.doPython()
