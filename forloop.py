#for loop in quiz
list1 = [1,2,3,6,8,9,"Ron"]
for item in list1:
    if str(item).isnumeric() and item>=6:
        print(item)

#with list in lists to dictionary
list2 =[["KEY1",7],["KEY2",8],["KEY3",9]]
DIC = dict(list2)
for item in DIC.items():
    print(item)
