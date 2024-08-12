cars=["Honda", "Toyota", "Suzuki"]

# for cars in cars:
#     print(cars)
# print(cars)
print(cars)

str_cars=""
for car in cars:
    str_cars+=car
print(str_cars)

cars.append(["Volvo", "Ford"])
print(cars)

cars.insert(1, ["Volvo", "Ford"])
print(cars[1][1])           #to access list within list we have to access its index dirctly is not possible 
#but pop method will remove the whole list when we try to remove an index 

cars_1=[x for x in cars]
print(cars_1)
#https://www.w3schools.com/python/python_lists.asp

