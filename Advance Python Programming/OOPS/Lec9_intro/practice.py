# #1. Write a  Python program to create a class representing a Circle. 
# # Include methods to calculate its area and perimeter
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius=radius
#     def area(self):
#         area=math.pi * (self.radius ** 2)
#         return area
#     def perimeter(self):
#         perimeter= 2*math.pi*self.radius
#         return perimeter

# r=int(input("Enter the radius: "))
# if(r >=0):
#     c=Circle(r)
#     print(f"The area of circle for the radius {r} is: ", c.area())
#     print(f"The perimeter of circle for the radius {r} is: ", c.perimeter())
# else:
#     print("Enter a positive value")

# #2. Write a Python program to create a person class. Include attributes like name, 
# # country and date of birth. Implement a method to determine the person's age.
# import datetime
# class Person:
#     def __init__(self, name, country, birth_date):
#         self.name=name
#         self.country=country
#         self.birth_date=birth_date
#     def find_age(self):
#         today=datetime.date.today()
#         age = today.year - self.birth_date.year 
#         return age

    
    
# user_name=input("Enter your name: ")
# user_country=input("Enter your country: ")
# date_of_birth=input("Enter your date of birth  (dd-mm-yyyy):  ")

# try:

#     format="%d-%m-%Y"
#     birth_date = datetime.datetime.strptime(date_of_birth, format)
#     person=Person(user_name, user_country, birth_date)
#     print(f"Name: {person.name},  Country: {person.country}, Age= {person.find_age()}")
# except ValueError:
#     print("Incorrect date format. Please enter the date in dd-mm-yyyy format.")


    

#3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
# import math

# class Calculator:
#     def __init__(self, op,num1, num2=None):
#         self.num1 = num1
#         self.num2=num2
#         self.o=op
#     def add(self):
#         return self.num1 + self.num2
    
#     def subtract(self):
#         return self.num1 - self.num2
    
#     def divide(self):
#         if self.num2 != 0:
#             return self.num1 / self.num2
#         else:
#             return "Error! Division by zero is not allowed"
        
#     def multiply(self):
#         return self.num1 * self.num2
    
#     def factorial(self):
#         if self.num1 >= 0 and self.num1 == int(self.num1):
#             factorial = 1
#             for i in range(1, self.num1 + 1):
#                 factorial *= i
#             return factorial
#         else:
#             return "Error! Factorial is not defined for negative numbers or non-integers"
#     def squareroot(self):
#         return math.sqrt(self.num1)

#     def power(self):
#         return self.num1**self.num2
    
    
#     def display(self):
#         if self.o == "+":
#             print(f"The addition of {self.num1} and {self.num2} is: ",x.add())
#         elif self.o == "-":
#             print(f"The subtraction of {self.num1} and {self.num2} is: ", x.subtract())
#         elif self.o == "*":
#             print(f"The product of {self.num1} and {self.num2} is: ",x.multiply())
#         elif self.o == "^":
#             if self.num2 == 0.5:
#                 print(f"The square root of {self.num1} is: {x.squareroot()}")
#             else:
#                 print(f"The answer of {self.num1} raise to the power {self.num2} is: ",x.power())
#         elif self.o == "/":
#             print(f"The division of {self.num1} and {self.num2} is: ",x.divide())
#         elif self.o == "!":
#             print(f"The factorial of {self.num1} is: {self.factorial()}")
#         else:
#             print( "Invalid Input")
        

        
#     @classmethod
#     def fromString(cls, str_input):
#         operators= ["+", "-", "*", "/", "^", "!"]

#         for x in operators:
#             if x in str_input:
#                 if x== "!":
#                      num1 = str_input.split(x)[0]
#                      return cls(x, int(num1))   
#                 else:
#                     num1, num2 = str_input.split(x)  
#                     o=x
#                     return cls(o, float(num1), float(num2))
    
         

# value=input("Enter two numbers in the format a(operator)b:  ")
# x=Calculator.fromString(value)
# if x:
#     x.display()
# else:
#     print("Invalid Input")

# print(x.add())
# print(x.subtract())
# print(x.divide())
# print(x.multiply())
# print(x.integral_division())
# print(x.power())
# n1=int(input("Enter a number: "))
# n2=int(input("Enter a number: "))

# a= Calculator(n1, n2)
# print("Addition: "+ str(a.add()))
# print("Subtraction: "+ str(a.subtract()))
# print("Power: " + str(a.power()))
# print("Product: " + str(a.multiply()))
# print("Division: " + str(a.divide()))
# print("Integral Division: " + str(a.integral_division()))

#4. Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price.
# class Cart:
#     def __init__(self):
#         self.items = {}
    
#     def add_items(self, item_name, quantity=1):
#         item_name = item_name.lower()
#         if item_name in items:
#             available_quantity = items[item_name]['quantity']
#             if quantity > available_quantity:
#                 print(f"Only {available_quantity} of {item_name} available. Cannot add {quantity}.")
#                 return
            
#             price = items[item_name]['price']
#             if item_name in self.items:
#                 self.items[item_name]['quantity'] += quantity
#             else:
#                 self.items[item_name] = {'price': price, 'quantity': quantity}
            
#             # Update available quantity in the store after adding to the cart
#             items[item_name]['quantity'] -= quantity
            
#             print(f"Added {quantity} of {item_name} to the cart.")
#         else:
#             print(f"{item_name} is not available.")

#     def remove_items(self, item_name, quantity):
#         item_name = item_name.lower()
#         if item_name in self.items:
#             if self.items[item_name]['quantity'] <= quantity:
#                 # Restore the available quantity in the store
#                 items[item_name]['quantity'] += self.items[item_name]['quantity']
                
#                 del self.items[item_name]
#                 print(f"Removed all {item_name} from the cart.")
#             else:
#                 self.items[item_name]['quantity'] -= quantity
#                 print(f"Removed {quantity} of {item_name} from the cart.")

#                 # Restore the available quantity in the store
#                 items[item_name]['quantity'] += quantity
#                 print(f"Removed {quantity} of {item_name} from the cart.")
#         else:
#             print(f"{item_name} is not in the cart.")

#     def calculate_total(self):
#         total = 0
#         for item in self.items.values():
#             total += item['price'] * item['quantity']
#         return total

#     def show_cart(self):
#         if not self.items:
#             print("Your cart is empty.")
#         else:
#             print("Items in your cart:")
#             for item_name, details in self.items.items():
#                 print(f"{item_name}: ${details['price']} x {details['quantity']}")
#             total = self.calculate_total()
#             print(f"Total: ${total:.2f}")

# items = {
#     'apple': {'price': 0.5, 'quantity': 50},
#     'banana': {'price': 0.3, 'quantity': 100},
#     'orange': {'price': 0.8, 'quantity': 30},
#     'milk': {'price': 1.5, 'quantity': 20},
#     'bread': {'price': 2.0, 'quantity': 15}
# }

# def show_items(items):
#     print("Available items:")
#     for item_name, details in items.items():
#         print(f"{item_name}: ${details['price']} (Quantity available: {details['quantity']})")


# # List to add, remove the item that the user wants
# user_cart = Cart()
# show_items(items)

# while True:
#     u_choice = input('''To buy items type a
#                     To remove from cart type r
#                     To view your cart type c
#                     To quit type q:  ''').lower()
    
#     if u_choice == "a":
#         item_name = input("Enter the item name: ")
#         quantity = int(input("Enter the quantity: "))
#         user_cart.add_items(item_name, quantity)

#     elif u_choice == "r":
#         item_name = input("Enter the item name: ")
#         quantity = int(input("Enter the quantity: "))
#         user_cart.remove_items(item_name, quantity)

#     elif u_choice == "c":
#         user_cart.show_cart()

#     elif u_choice == "q":
#         print("Thanks for shopping!")
#         break

#     else:
#         print("Invalid input. Enter a to add, r to remove, c to view cart, or q to quit.")



#5. Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.customers = {}
        self.account_number = 1000

    def add_customer(self, name, initial_balance=0):
        # Check if the customer name already exists
        for customer in self.customers.values():
            if customer['name'] == name:
                print("Customer already exists.")
                return
        
        acc_number = self.account_number
        self.customers[acc_number] = {'name': name, 'balance': initial_balance}
        self.account_number += 1 

        print(f"Customer {name} added with account number {acc_number} and initial balance ${initial_balance}.")

    def deposit(self, acc_number, amount):
        if acc_number in self.customers:
            self.customers[acc_number]['balance'] += amount
            print(f"Deposited ${amount} to account {acc_number}. New balance: ${self.customers[acc_number]['balance']}")
        else:
            print(f"Account {acc_number} does not exist.")

    def withdraw(self, acc_number, amount):
        if acc_number in self.customers:
            if self.customers[acc_number]['balance'] >= amount:
                self.customers[acc_number]['balance'] -= amount
                print(f"Withdrew ${amount} from account {acc_number}. New balance: ${self.customers[acc_number]['balance']}")
            else:
                print(f"Insufficient balance in account {acc_number}.")
        else:
            print(f"Account {acc_number} does not exist.")

    def get_balance(self, acc_number):
        if acc_number in self.customers:
            return self.customers[acc_number]['balance']
        else:
            print(f"Account {acc_number} does not exist.")
            return None

    def transfer(self, from_account, to_account, amount):
        if from_account in self.customers and to_account in self.customers:
            if self.customers[from_account]['balance'] >= amount:
                self.customers[from_account]['balance'] -= amount
                self.customers[to_account]['balance'] += amount
                print(f"Transferred ${amount} from account {from_account} to account {to_account}.")
            else:
                print(f"Insufficient balance in account {from_account}.")
        else:
            print("One or both account numbers do not exist.")

# Example usage
bank = Bank()

while True:
    print("\n1. Add Customer")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter customer name: ")
        initial_balance = float(input("Enter initial balance: "))
        bank.add_customer(name, initial_balance)
    
    elif choice == '2':
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to deposit: "))
        bank.deposit(account_number, amount)
    
    elif choice == '3':
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to withdraw: "))
        bank.withdraw(account_number, amount)
    
    elif choice == '4':
        from_account = int(input("Enter from account number: "))
        to_account = int(input("Enter to account number: "))
        amount = float(input("Enter amount to transfer: "))
        bank.transfer(from_account, to_account, amount)
    
    elif choice == '5':
        account_number = int(input("Enter account number: "))
        balance = bank.get_balance(account_number)
        if balance is not None:
            print(f"Account {account_number} balance: ${balance}")
    
    elif choice == '6':
        break
    
    else:
        print("Invalid choice. Please try again.")
