#create a main to access functions from another file
def pyrdf(str):
    return f"Okay so we have:{str}"
def add(a,b):
    return a+b

print("So the name is",__name__)

if __name__=='__main__':
 print(pyrdf("Natasha"))
 print(add(5,7))