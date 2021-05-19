import json 
people1=[{"name":"nitin","website":"gfg.com","from":"delhi"},{"name":"ritika","website":"google.com","from":"lucknow"}]
f=open("data.json","a")
json.dump(people1,f,indent=2)

