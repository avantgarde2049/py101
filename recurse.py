#Recursion
def func(str1):
    print("The string is:",str1)
func("rudy")

##Iterative approach
def func2(n):
    fac = 1
    for i in range(n):#takes range from 1 to n
        fac = fac*(i+1)#multiply 1*2*---n
    return fac
num=int(input("Enter the number:"))
print("The factorial is:",func2(num))

##Recursive approach
def func3(p):
    if p==1:
        return 1
    else:
        return p*func3(p-1)
num=int(input("Enter no please:"))
print("Factorial :",func3(num))