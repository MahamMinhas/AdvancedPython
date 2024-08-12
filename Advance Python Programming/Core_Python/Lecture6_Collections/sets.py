#sets are unorederd data structures 
#No duplication allowed

fruits=set(("Banana", "Apple", "Apple"))
print(fruits)

for x in fruits:
    print(x)
#there is no specific index for the values added in the set everytime we print it becomes different index 
#sets cannot store other data structures like lists, tuples

#pop method removes random value because it requires index and set does not have it by deault in list last item is removed
#joining  2 sets 
fruits=set(("Banana", "Apple", "cherry"))
fruits_1=set(("Kiwi", "lichi"))
set2=set(("Kiwi", "lichi"))
set1=set(("Banana", "Apple", "cherry"))
fruits_2= fruits_1.union(fruits)
for x in fruits_2:
    print(x)

#diiference method:
set3=set2.difference(set1)
set3=set1 |set2 #union
set3=set1.intersection(set2)
set3=set1.symmetric_difference(set2) #does not add the common values from both sets 
set3=set2.difference_update(set1) #updates the changes in already present set and dont make new one 

#https://www.w3schools.com/python/python_sets_methods.asp