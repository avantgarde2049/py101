#filter application
y=[1,9,7,3,2,4]

def func(a):
    return a>3

grt=list(filter(func,y))
print(grt)