
#print a dictionary to take input from the user such that it returns the meani9ng of the input keyword
"""info={"House of Dragon":"https://en.wikipedia.org/wiki/House_of_the_Dragon","Rings of Power":"https://en.wikipedia.org/wiki/The_Lord_of_the_Rings:_The_Rings_of_Power","Game of Thrones":"https://en.wikipedia.org/wiki/Game_of_Thrones","Sopranos":"https://en.wikipedia.org/wiki/The_Sopranos"}
print("Please enter an input:")
inp1=input()
print("The input refers to:" ,info[inp1])"""

#Sets
s = set()
print(type(s))
s_from_list = set([1,3,5,8])
print(s_from_list)
#alternatively
l1 = [1,4,6,2]
l2 = set(l1)
print(l2)
#add elements in set
l2.add(5)
print(l2)
#REMOVE  elements
l2.remove(5)
print(l2)
#intersection of sets
l3 = l2.intersection({1,2})
print(l2,  l3)
#union
l4= l3.union({2,9})
print(l4)
#disjoint
l5= set({4,8,11})
print("Is l4 disjoint with l5:",l5.isdisjoint(l4))