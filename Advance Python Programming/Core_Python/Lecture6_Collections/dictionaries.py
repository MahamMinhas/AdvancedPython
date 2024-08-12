#stores data in the form of key, value pair
#(associative, hash_maps)
#Dictionary (This is the most frequently used ) [Mutable, No Duplication, ordered] declared with {}
#cannot contain 2 same keys 
#in latest version dictionaries are ordered
#can store string, integer, float, bool and another list
#C(CREATE) R(READ) U(UPDATE) D(DELETE) MAIN OPERATIONS TO KNOW IN EVERY STRUCTURE

student={
    "name":"maham",
    "age": 22,
    "courses":["python", "android"],
    "address": {
        "city": "Lahore",
        "country": "Pakistan"    }
}

# print(student["name"])   #same key names cannot be used
# print(student["address"]["city"])
# #nested dicionary loop
address=student["address"]

for key, value in address.items():
    print(f"{key} : {value}")



# if "age" in student:
#     print(student["age"])
# else:
#     print("not found")

# print(student.get("roll_no")) #here  second parameter contains what to display if not availability
#if a string contains str=False it means there is no string str=str(False)


#Empty string{
#false
#none
#''
#0
#}

# student["name"]="Zahra"
# print(student)    #overridiing

# #data is added and updated using keys 

# student["phone"]="5555-5555"
# print(student)

# #we can add an item at the end of dictionary by giving the index even if that does not exist
# #update method
# student.update({"name":"maham", "phone":"1234-4676", "age":22})
# print(student)

# #delete method 
# del student["age"]
# print(student)

# #pop method 
# #it also returns the value that is popped

# #to print only keys 
# print(student.keys())

# print(len(student)) #it only counts the keys and not the values 

# #to access thee key value pair both 
# # for key in student:
# #     print(student[key])
# #     print(key , ":", student[key] )

# for key, value in student.items():
#     print(key, value)

# print(student.items())

# #it works on reference base so whwnwver we add and updatethe keys it gets updated no need to call the 
# #function again and again
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change

# #https://www.w3schools.com/python/python_dictionaries.asp

# #nested dictionaries
myfamily = {
    '''
    "child1":
    "name" : "Emil",
    "year" : 2004,

    "child2" 
    "name" : "Tobias",
    "year" : 2007,

    "child3" 
    "name" : "Linus",
    "year" : 2011
'''
  
}

# for key, value in myfamily.items():
#     for x, y in value.items():
#       print(f"{x}: {y}")
print(myfamily)