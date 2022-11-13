#multiple inheritance
class Employee1:
    no_of_leaves = 8
    var = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

class player():
    no_of_games=9

    def __init__(self,name,game):
        self.name =name
        self.game=game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game} "

class coolprog(Employee1,player):# 2 classes inherited by coolprog and hierachy is employye1 followed by player
    pass


shubham = player("Shubham", ["Cricket"])
samir = coolprog("Samir",7878,"Cook")
print(samir.printdetails())
print(shubham.printdetails())