# import json
# shopping={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
# f=open("shopping.json","w")
# json.dump(shopping,f,indent=2)
# print(shopping)


# (2)
# import json
# shopping={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
# f=open("shopping.json","w")
# json.dump(shopping,f,indent=2)
# print(shopping)
# item=input("enter the item")
# print(item)

import json
shopping={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
item=input("enter the item")
no=int(input("how many item"))
c=shopping["shopping_list"][item]
rem=int(c)-no
shopping["shopping_list"][item]=rem
b=json.dumps(shopping)
print(b)


