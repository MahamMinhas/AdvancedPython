#1. Convert two lists in a dictionary
list1=["name", "age", "score", "course"]
list2=["John", 20, 85, "Math"]
dict1=dict(zip(list1, list2))
print(dict1)

#2. Merge 2 python dictionaries intto one
dict2={"name": "John", "age": 20, "score": 85, "course":"Math"}
dict3={"a":5, "b":6}            #here two different dictionaries will be merged if they are same or contain same keys 
                                #only one dictionary will be returned 

dict4=dict2.copy()
dict4.update(dict3)
print(dict4)

#3. Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])

#4. Initialize dictionary with default values
dict5={"key1", "key2", "key3"}
default_value=0
thisdict=dict.fromkeys(dict5, default_value)
print(thisdict)

#5. Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
res = dict()

for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sample_dict[k]})
print(res)

#6. delete a list of keys from the dictionary 
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)

#7. check if a specific value is present or not
sample_dict = {'a': 100, 'b': 200, 'c': 300}

if "b" in sample_dict:
    print(sample_dict["b"])
else:
    print("Not found")

#8. Rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
key=["city"]
for k in key:
    popped=sample_dict.pop(k)
print("The dictionary after the certain key is popped: ",sample_dict)

s=sample_dict.setdefault("location", "New York")
print(sample_dict)

# sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)

#9. Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict, key=sample_dict.get))

#10. Write a Python program to change Brad’s salary to 8500 in the following dictionary.

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary']=8500

for k in sample_dict:
    print(sample_dict[k])
