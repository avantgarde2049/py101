#IF else
"""print("Please enter you age:")
a = int(input())
if a>18:
    print("You are eligible for a drivers license")
elif a==18:
    print("Please visit at the centre for qualifying the test in person")
else:
    print("You are not eligible for a drivers license")"""

#age range 7-100


#print("Please enter you age:")
#a = int(input())
#if 101>a>18:
#    print("You are eligible for a drivers license")
#elif a==18:
#    print("Please visit at the centre for qualifying the test in person")
#elif 6<a<18:
#    print("You are not eligible for a drivers license")
#else:
#    print("Please enter a valid age")


#calculator quiz
print("Enter first number:")
a= int(input())
print("Enter second number:")
b= int(input())
print("Enter operation:")
c= input()

if a==43 and b==3 and c=="*":
    print("Answer is:",555)
elif a==56 and b==9 and c=="+":
    print("Answer is:", 77)
elif a==56 and b==6 and c=="/":
    print("Answer is:", 4)
elif c=="+":
    print("Answer is:",a+b)
elif c=="-":
    print("Answer is:",a-b)
elif c=="*":
    print("Answer is:",a*b)
elif c=="/":
    print("Answer is:",a/b)
else:
    print("Enter a valid operator")

