#a baseclass which is inherited from abcmetaclass can rule desired methods to its child classes
from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self): #this abstract method will need to be initialized in every child classes eg rectangle here
        return 0

class Rectangle(shape):
    def __init__(self):
        self.length = 12
        self.breadth= 14

    def printarea(self):
        return self.length*self.breadth

a=Rectangle()
print(a.printarea())

# we cannot instantiate an object from an abstract method

