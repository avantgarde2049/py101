#normal function
#i have a list of items of which i want only even pos elements


l1=["sooji","rice","maida","flour"]

#i=1
#for items in l1:
#    if i%2==0:
#     print(f"Please get me{items}")
#    i=i+1

#i have a list of items of which i want only even pos elements
#using enumerate function
for index,item in enumerate(l1):
    if index%2 is not 0:
        print(f"Please get me ,{item}")

