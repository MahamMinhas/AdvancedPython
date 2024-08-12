#List
#tuple
#set
#dictionary are the 4 ways to store data in Python

#List is ordered collection of items which can be of any data type, including strings, integers,
# floats, and other lists also can store tuples and other data structures like dictionary.
#  Lists are denoted by square brackets [] and are mutable,

courses=["Programmingg Fundamentals", "Python", "OOPS"]
print(courses[0])   #retrieving a specific index
print(courses)  #retreiving whole list
print(type(courses)) 

students=["Ali", 1,50,  True]  #can store multiple data types

#purpose of list is to store data that is not to be channged like no new data can be addedbut now this is also possible
#list is mutable

list=["Apple", "Mango", "Banana"]
print(len(list))

list.append("cherries") #by default inserts element at last
print(list)
list.insert(1, "grapes")
print(list)  #inserts value at selected index and dont even remove the previous value

list.clear()
print(list)

#Taking input from user
values=int(input("Enter the no. of values: "))
List=[]

for x in range(values):
    name=input("Enter student name: ")
    List.append(name)

print(List)

#copy() method
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()       #This will create the copy of list that means we have 2 lists (deep copy)
x = fruits              #This will not create the second list that means we have 1 list with 2 names (shallow copy)
print(x)

#count() method
fruits = ["apple", "banana", "cherry", "Cherry"]
lowerfruits=[]
for fruit in fruits:
    lowerfruits.append(fruit.lower())

x = fruits.count("cherry")

print(x)

#extend method

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
mobiles=[]

cars.extend(fruits)
fruits.extend(cars)
mobiles.extend(fruits)

print(fruits)
print(cars)
print(mobiles)

#index() method
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")          #error because of case sensitivity if not matched
print(x)

#pop() method
fruits = ['apple', 'banana', 'cherry']
#if(len(fruits)-1 >= 3):
    #fruits.pop(3)

if("banana"in fruits):
    fruits.pop()
fruits.pop(1)               #popped = fruits.pop(1) this will store the popped value in a variable and make 
print(fruits)                #it suitable to access it later

#remove() method
#sort() method
# cars=["Ford", "BMW", "Volvo"]
#gives error 
# sorted=cars.copy().sort()
# sorted.sort()

# print(cars)
# print(sorted)

