#constructor helps passing arguments to a instance
class Milo:
    def __init__(self,aname,asalary):
        self.name = aname
        self.salary = asalary

    #def printdetails(self):  # a method is created asking for argument
     #       return f"Hi! My name is {self.name} and my salary is {self.salary}"


harry = Milo("Harry",200000)
print(harry.name)

