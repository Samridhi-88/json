import json
list1=["neelam","programer","24","2400"]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"]  
list5=["name","designation","age","salary"]
d1={}
d2={}
d3={}
d4={}
dictionary={}
i=0
while i<len(list1):
    j=0
    while j<len(list1):
        d1[list5[i]]=list1[i]
        d2[list5[i]]=list2[i]
        d3[list5[i]]=list3[i]
        d4[list5[i]]=list4[i]
        j=j+1
    dictionary["emp1"]=d1
    dictionary["emp2"]=d2
    dictionary["emp3"]=d3
    dictionary["emp4"]=d4
    i=i+1
print(dictionary)
f=open("course.json","w")
json.dump(dictionary,f,indent=2)



# while i<len(list1):
#     d1[list5[i]]=list1[i]
#     i+=1

# j=0
# while j<len(list2):
#     d2[list5[j]]=list2[j]
#     j+=1
# k=0
# while k<len(list3):
#     d3[list5[k]]=list3[k]
#     k+=1
# l=0
# while l<len(list4):
#     d4[list5[l]]=list4[l]
#     l+=1
# main_key=["emp1","d2","d3","d4"]
# main_value=[d1,d2,d3,d4]
# dic={}
# x=0
# while x<len(main_key):
#     dic=main_key[x]=main_value[x]
#     print(dic)
#     x+=1
#(print(json.dumps(dic)))
# f=open("course.json","w")
# json.dump(dictionary,f,indent=2)


