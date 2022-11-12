a1=["Yogurt","Curd","Milk","Paneer"]
#now we want to add and after each word ion same line
for item in a1:
 print(item,"and",end=" ")

#using join function
c=",".join(a1)
print(c,"and others")