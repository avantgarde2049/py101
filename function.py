#function
def func(a,b):
    """this is a function which will calculate average of 2 numbers"""
    average = (a+b)/2
    return (average)
v= func(5,9)
print(func.__doc__)##printing the docstring above
print(v)
