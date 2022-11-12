#reduce
from functools import reduce
sa =[2,8,6,4]
g = reduce(lambda x,y:x+y,sa)#one liner function without usage of for loop
print(g)

#using for loop
num=0
for i in sa:
    num=num+i
print(num)
