#we can return a fn using a fn
def f1(num):
    if num == 0:
        return print
    if num==1:
        return sum
v = f1(0)
print(v)

#we can pass a fn as an argument to return a fn
def f2(qw):
    qw=("reed")

f2(print)

#decorator
def dec1(func):
    def fine():
        print("executing now")
        func()
        print("executed")
    return fine()

@dec1
def harry():
    print("Hi,how are you")

harry()

