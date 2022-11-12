#enumerate function
#i have a list of items of which i want only even pos elements
import enum
l1=["sooji","rice","maida","flour"]
##i=1
#for items in l1:
#    if i%2==0:
#     print(f"Please get me{items}")
##    i=i+1
#enumerate
for index,items in enumerate(l1):
    if index%2 is not 0:
        print(f"Please get me{items}")
    
