a = [1,2,3,2,0,65,21,4,2,10]
list=[]
for i in range(len(a)):
    if a[i]==2:
        list.append(i)
print(list)