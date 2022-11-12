x=89
def harry():
    x=20 #will consider this value from now on,local variable
    def rohan():
        global x
        x=88
    print("before calling:",x)
    rohan()
    print("after calling",x)
harry() #now both fns are called,global value  can take over
print(x)
