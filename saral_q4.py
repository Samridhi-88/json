dic={'4': 5,'6': 7,'1': 3,'2': 4}
l1=[]
l2=[]
for key in dic:
    l1.append(key)
    l2.append(dic[key])
print(l1)
print(l2)
i=0
while i<len(l1):
    j=0
    while j<len(l1):
        if l1[i]<l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
        if l2[i]<l2[j]:
            l2[i],l2[j]=l2[j],l2[i]
        j+=1
    i+=1
print(l1)
print(l2)
d={}
k=0
while k<len(l1):
    d[l1[k]]=l2[k]
    k+=1
print(d)










#{"1": 3,"2": 4,"4": 5,"6": 7}
