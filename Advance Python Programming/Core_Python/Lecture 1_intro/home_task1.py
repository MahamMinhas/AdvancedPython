#task 1: Reversing the 3 digit number
print("Task 1: Reversing the number task")
num=678
print("The number before reversing: ", num)
hundreds=num//100
remainder=num%100
tens=remainder//10
units=remainder%10
print("The first digit is: ", hundreds)
print("The second digit is: ", tens)
print("The third digit is: ", units)
reversed_num=units*100+tens*10+hundreds
print("The number after reversing is: ", reversed_num)

#Task 2: Finding discriminant 
print("Task 2: Finding Discriminant of a number")
a=5
b=5
c=9

discriminant=b**2-4*a*c
print("The discriminant is: ", discriminant)

#Task 3: Finding inverse of a number
print("Task 3: Finding the inverse of a number")
num= -20
print("The original number is: ", num)

inverse=num*-1
print("The inverse of the number is: ", inverse)