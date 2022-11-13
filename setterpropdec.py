#Setter and property decorators
class Emp():

    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email= f"{fname}.{lname}@gmail.com"

    def printdet(self):
        return f"The name of the individual is {self.fname} {self.lname}"

  #setter_1
    @property
    def email(self):
        if self.fname== None or self.lname== None :
          return "Email is not set.Please set it using setter."
        return f"{self.fname}.{self.lname}@gmail.com"

  #setter_2
    @email.setter
    def email(self,string):
        print("Setting now..")
        name=string.split("@")[0]
        self.fname =name.split(".")[0]
        self.lname = name.split(".")[1]

#similarly to delete the setter we use a deleter
    @email.deleter
    def email(self):
        self.fname= None
        self.lname = None

inp1 = Emp("sagnik","patra")
print(inp1.printdet())
print(inp1.email)

#now suppose we wish to change say fname ,we cannot do
#inp1.fname= "agnik"
#so we use a setter_1 as the constructor during runtime did not receive the updated fname
#first commenting the self.email attribute in init constructor

#now lets us change fname

inp1.fname= "agnik"
print(inp1.email)

#based on the theory of encapsulation we do not wish to show full classes and instances in our code
#so here we pass function inside a function , can we pass as an argument
#property decorator,just add @property before the setter_1,now remove the () from line 19 as email is now passed as an attribute

#suppose,now we wish to set fname and lmame from input of email
#by doing.
#inp1.email="dhrubo.ghosh@gmail.com"
#will throw error AttributeError: can't set attribute,hence we set a setter_2


inp1.email="dhrubo.ghosh@gmail.com"
print(inp1.fname)
print(inp1.lname)

del inp1.email #if we only use this to delete it would not know what arguments to delete,so we need a deleter
print(inp1.email)