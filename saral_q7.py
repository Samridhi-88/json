import json
a_dictionary = {}
a_file = open("sam.json","r")
for line in a_file:
    key, value = line.strip().split(None,1)
    a_dictionary[key] = value.strip()
print(a_dictionary)