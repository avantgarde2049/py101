class Employee():
    no_of_leaves=8

    # Lets us create a method
    def printdetails(self):  # a method is created asking for argument
        return f"Hi! My name is {self.name} and my salary is {self.salary}"

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 200000 #example of an instance variable salary of instance harry

print(harry.no_of_leaves) #we can access class variable with an instance

Employee.no_of_leaves =9 #but we can change the variable of the class by the class only

print(rohan.no_of_leaves)#if we try with an instance , a new instance variable is created by that name


print(harry.printdetails())
