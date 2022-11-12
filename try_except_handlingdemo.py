#print the error message as per data type mismatch

print("Enter number 1:")
a=input()

print("Enter number 2:")
b=input()
try:
    print("Sum of the numbers:", int(a) + int(b))
except Exception as e:
    print(e)

