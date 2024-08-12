# class Car:
    
#     # company ="Honda"
#     # model="Civic"

#     def __init__(self, company, model):
#         self.company = company
#         self.model=model                        
# #variable with self. are the defined variables and in the parameters are the one being passed 

import datetime
class Person:
    bonus=2000
    def __init__(self, fname, lname, salary):
        self.fname=fname            #class variables
        self.lname=lname
        self.salary=salary
    def display(self):
        print(f"{self.fname}, {self.lname}, {self.salary}")

    def salary_with_bonus(self):
        return self.salary + self.bonus  #when definewith class it will simply add the value but when used with instance it will add the bonus value on runtime 
    # class variables are shared by all instances of the class

# c= Car("Honda", "Civic")
# c1=Car("Toyota", "Corolla")
# c2=Car("Suzuki", "Swift")

p=Person("Ali", "Anwar", "50000")   #instance variables
# p.display()

# p2=Person("Maham", "Minhas", "40k")
# p2.display()

# print(c.company +" " + c.model)
# print(c1.company +" " + c1.model)
# print(c2.company +" " + c2.model)
# # print(p)

# #To define all instance with different values we need an empty class and define every object separately
# c.company="Honda"
# c.model="Civic"

# #This is a difficult method so we use a method called __init___ also called a constructor in other languagaes

# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2=num2
#     def add(self):
#         return self.num1 + self.num2
#     def subtract(self):
#         return self.num1 - self.num2
#     def divide(self):
#         if self.num2 != 0:
#             return self.num1 / self.num2
#         else:
#             return "Error! Division by zero is not allowed"
#     def power(self):
#         return self.num1**self.num2

# n1=int(input("Enter a number: "))
# n2=int(input("Enter a number: "))

# a= Calculator(n1, n2)
# print("Addition: "+ str(a.add()))
# print("Subtraction: "+ str(a.subtract()))
# print("Power: " + str(a.power()))
# print(Person.__dict__)
# print(p.__dict__)
print(p.bonus)
print(Person.bonus)
print(Person.__dict__)
print(p.__dict__)

Person.bonus=6000
p.bonus=7000

print(Person.bonus)     #when class variables are changed it globally change all instance value 
print(p.bonus)          #This changes only the specific value
        
