#Text slicing

a="All men must die"
print(a[:])#prints whole of the string
print(a[0:5])#prints from start(0) to character at 4th pos
print(a[1:])#prints from 2nd pos to last
print(a[::2])#prints everything by skipping a charcter in between

#negative slicing
k="MONTY PYTHON"
print(k[6:10])
print(k[-6:-2])
print(type(k))#returns data type

#functions
print(k.isalnum())#not numeric
print(k.isalpha())#not alpha numeric
print(a.endswith("die"))#to check if its ends with desired string
print(a.count('e'))#gives count
print(k.capitalize())#normal case
#same applies with upper() and lower()