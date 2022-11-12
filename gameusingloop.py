a= 20
j=1
while(j<=10):
    i=int(input("Please enter your number:"))
    if i<a:
        print("The number is less than the actual one.")
    elif i>a:
        print("The number is greater than the actual one.")
    else:
        print("Yes,the number entered is correct!")
        print("Number of guesses you took:",j)
        break


    print("Number of guesses left:",10-j)
    j=j+1


if j>10:
    print("Game over!")
