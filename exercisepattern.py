##Print a star pattern with * and 2 inputs
##one input corresponds to number of rows for the pattern
##second one returns a boolean between true and false
##if true :star is printed . else: reverse pattern
print("Please enter your input:")
a= int(input())
print("Please enter boolean input 0 or 1:")
b= int(input())
boole= bool(b)
if boole==True:
   for i in range(1,a+1):
       for j in range(1,i+1):
           print("*",end="")
       print()
elif boole==False:
    for i in range(a,0,-1):
        for j in range(1,i-1):
            print("*",end="")
        print()