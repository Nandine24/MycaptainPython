#positive numbers of a list
list_1=[]
list_2=[]
n=int(input("number of elements?"))
for i in range(1,n+1):
    val=int(input("enter element:"))
    list_1.append(val)
    if val>0:
        list_2.append(val)
print("input:",list_1)
print("output:",list_2)
