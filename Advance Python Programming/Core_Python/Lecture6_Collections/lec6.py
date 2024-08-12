##Tuples	(Immutable, duplication allowed, ordered)	declared with courses=()
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#duplicates possible 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#if we have to store only 1 item in the tuple we have to add comma at the end it will be tuple
thistuple = ("apple",)
print(thistuple)

#tuple can also store multile data structures like lists but that list will be unchangeable

fruits = ("apple", "banana", "cherry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)      #this will make the variables that contains the values in the tuple and it becomes the list 
#if we dont know how many values in the list then we add Esteric with last variable that will add all rest of values in last 
#variable
