#ARGS and KWARGS
def args1(nor,*arg1,**kwar1):
    print(nor)
    for items in arg1:
        print(items)

    print("\nThe heroes in their dept are:")
    for key,value in kwar1.items():
        print(f"{key} is a {value}")

nor = "I am a programmer"
har =["Ron","Wesley","Cate"]
kw={"Ron":"Cook","Wesley":"Pilot","Cate":"Architect"}
args1(nor,*har,**kw)