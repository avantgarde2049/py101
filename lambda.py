#lambda or anonymous function

#initially we have normal function
def key_first(x):
    return x[1]

x= [[1,8],[2,7],[1,2]]#list of lists
x.sort(key=key_first)#sort fn takes key or position of element to be sorted accordingly
print(x)#prints all elements by first position being sorted

#using lambda function now
key_first1 = lambda x:x[1]
x= [[1,8],[2,7],[1,2]]#list of lists
x.sort(key=key_first1)
print(x)