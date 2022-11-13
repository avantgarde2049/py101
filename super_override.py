class mainc():
    var1 = "Im a class variable in class A"
    def __init__(self):
        self.var1="Im inside class A's constructor"
        self.classvar="Instance variable in class A"
        self.special="pan"
class sub(mainc):
    var1 = "Im class variable in class in class B"
    def __init__(self):
        super().__init__()#at the start so prints var1 and classvar instance variablesof b and then goes to constructor of a
        self.var1="Im inside class B's constructor"
        self.classvar="Instance variable in class B"

a=mainc()
b=sub()
print(b.var1)
print(b.classvar)

print(b.special)
#now constructor of A is override by b so cannot print the above print statement,so we user sper above

