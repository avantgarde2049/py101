#class methods used as an alternative constructor
class Milo:
    no_of_leaves = 12
    def __init__(self,aname,asalary):
        self.name = aname
        self.salary = asalary

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod #alternative constructor to pass arguments to an object without using multiple arguments like in object using constructors,self
    def from_str(cls,string):
        params=string.split("-")
        return cls(params[0],params[1])

    def printdetails(self):  # a method is created asking for argument
            return f"Hi! My name is {self.name} and my salary is {self.salary}"


harry = Milo("Harry",200000)
karan = Milo.from_str("Karan-480")
print(harry.name)

harry.change_leaves(56)# using class method to change \n
# class instance variable with an instance without creating a new instance variable
print(harry.no_of_leaves)
print(karan.salary)