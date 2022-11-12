#lISTS
grocery=['Harpic','Vim bar','Maggi','Eggs','Garam masala']
print(grocery)
#To access each entry in the list
print(grocery[1])
#Let us have a numbers list
number =[1,4,2,6,3,9,12,11]
#let us sort them
number.sort()
print(number)
#reverse sort
number.reverse()
print(number)
print(number[1:4])#slicing is done as per reverse sort applied lastly
#print(number[::2])#skips by 2 numbers
#To add more numbers in the list
number.append(13)
print(number)
#To insert number at say 2nd position
number.insert(1,23)
print(number)
number.remove(2)#removes desired value
print(number)
number.pop()#removes the last element
print(number)

number[1]= 98
print(number)#mutable property


##Tuple
##Tuples are immutable

tp =(1,4,7,9,13,15)
print(tp)