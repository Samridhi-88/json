#Dump():- Dump() method python objects ko json file mai store karane ke liye use hota hai. Dump() method json files par hi kaam karta hai aur python objects ko ek argument ki tarah store karta hai. *Example:-*python object(dictionary) ko hum json file mai dump.

import json

dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
} 



#Dumps() :- Dumps() method python objects ko json file mai string ke format mai store karene ki liye use hota hai. String format mai hum python objects(dictionary) ko tab store karate hai jab hume bo objects print karane ho ya phir parse karene ho. Example:-

import json

a={"lalalala": 3}
mystring = json.dumps(a)
print(mystring)
 
