#loads() method ek json string leta hai or use json objects mai convert ker deta hai.
#lods() method json data python me convert krne ke liye 

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) 
print(y)

#load():- load() method ek json object or json file ko json data ke sath python object(dictionaries) mai karta hai.
#json data ko pythonme 