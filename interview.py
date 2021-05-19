# (dump)
# import json
# shopping={1:{"chaco":15,"Biscuits":50,"Diary_milk":30,"ice_cream":20,}}
# print(type(shopping),"kkkkkk")
# f=open("dic.json","w")
# json.dumps(shopping)
# print(shopping)
# print(type(shopping))



# #(dump)
# import json
# student_list=["ram","seeta","geeta","reena","kabita","somi"]
# s=open("list.json","w")
# json.dump(student_list,s,indent=2)
# print(student_list)


# #(load)
# import json
# print("Started Reading JSON file")
# p={2:["ram","seeta","geeta"]}
# s=open("dic.json", "r") 
# developer = json.load(s)
# print(type(developer))



#(load)
# import json
# p={"ram":2,"seeta":4,"reeta":8}
# # j=open("dic.json","r")
# with open("dic.json","r") as f1:
#     dic1=json.load(f1)
#     print(dic1)



# import json 
# dic={"ram":2,"manvi":3,"mahi":5}
# a=json.load(dic)
# # print(a)
# f1=open("my.json","w+")
# data=f1.write(a)
# for i in f1:
#     f1.write(a)
# f1.close(

import json
s=open("as.json")
data=json.load(s)
for i in data:
    print(data[i])

