#Operator overloading and dunder fns
class emp1():
    no_of_leaves = 7
#__init__,__truediv__,__repr__,__str__ are all dunder fns
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary= asalary
        self.role = arole

    def printdet(self):
        return f"The name is {self.name},salary is {self.salary},role is {self.role}"

#this class method will change the initial class variables across any objects at any point of time
    @classmethod
    def new_leaves(cls,newlvs):
        cls.no_of_leaves=newlvs
#now we will see examples of operator overloading ,add will take arguments as specified in dunder add fn
    def __add__(self, other):
        return self.salary+other.salary

    def __str__(self):
        return f"The name is {self.name},salary is {self.salary},role is {self.role}"

    def __repr__(self):
        return f"Employee '{self.name}',{self.salary},'{self.role}'"

e1=emp1("Rahul",450,"Coder")

e2 = emp1("Rohit", 550, "Marketer")

e1.new_leaves(34)

print(e1.no_of_leaves)
print(e1+e2)
print(str(e2))
print(repr(e2))
