#from a list of 3 nos add 1 to the last indexed number
lis = ["2","5","9"]

for i in range(len(lis)):
    lis[i] = int(lis[i])

lis[2]=lis[2]+1
print(lis[2])

#similar using map

lis = list(map(int,lis))

for i in range(len(lis)):
    lis[i] = int(lis[i])

lis[2]=lis[2]+1
print(lis[2])

#a function using map
def sq(a):
    return a*a

num = [2,4,3,1,7,4]
print(list(map(sq,num)))

#same function with lambda

num = [2,4,3,1,7,4]
print(list(map(lambda x:x*x ,num)))

# a cube function
def cu(a):
    return a*a*a

#put the sq and cu in a list

l = [sq,cu]

#run a for loop to print the list for a desired range

for w in range(5):
    val = list(map(lambda x:x(w),l))
    print(val)
