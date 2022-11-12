#Dictionary
#nothing but key value pairs
dic = {"Group A":"Lyon","Group B":"PSG","Group C":"Roma","Group D":"Chelsea"}
print(dic)
DIC1 ={"Group A":"Lyon","Group B":"PSG","Group C":"Roma","Group D":{"Group E":"Sevilla","Group F":"Arsenal","Group G":"Dortmund"}}
print(DIC1)
print(DIC1["Group D"])
DIC1["Group H"]="Salzburg"
print(DIC1)

#functions
#shallow copy
dcv= DIC1.copy()
print(dcv)
#if we take dcv =DIC1 , it is not a copy
dcv=DIC1
print(dcv)

#delete a value
del dcv["Group A"]
print(dcv)

#update a new value
dcv.update({"Group P":"Inter"})
print(dcv)

print(dcv.keys())
print(dcv.items())

