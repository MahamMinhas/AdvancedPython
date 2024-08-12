# # 1)Write a function called km_to_miles 
# # that takes kilometers as a parameter, converts it into miles and returns the result.
# def km_to_miles(Distance):
#     return Distance *0.621371
# d=int(input("Enter the distance in kilometers: "))

# km_to_miles(d)
# print("The distance in miles is: ",km_to_miles(d))  

# #2)	Write a function called is_divisable_by_11 that 
# #takes an integer as an parameter and returns whether it is divisible by 11 or not.
# def is_divisible_by_11(number):
#     if(number%11==0):
#         print(f"The number {number} is divisible by 11 ")
#     else:
#         print(f"The number {number} is not divisible by 11 ")
    

# num=int(input("Enter the number: "))

# is_divisible_by_11(num)

# #3)	Create a function called is_palindrone that checks to see if a given string is a palindrome or not.
# def is_palindrome(string):
#     reversed=string[::-1]
#     if(string==reversed):
#         return True
#     else:
#         return False

# txt=input("Enter the string: ")
# is_palindrome(txt)
# print("The given string is palindrome!", is_palindrome(txt))

# #4)	Write a function called fuel_cost that takes a distance as a required argument, 
# # mpg (default 50 mpg) and fuel cost (default $1 a litre) as optional arguments. 
# # The function should return the cost in dollars.
# def fuel_cost(distance, mpg=50, cost=1):
#     gallons_used = distance / mpg
#     gallons_to_liters = gallons_used * 3.78541
#     total_cost = cost * gallons_to_liters
#     return total_cost

# distance = float(input("Enter the distance (in miles): "))
# mpg_input = input("Enter the mpg (leave blank to use default 50 mpg): ")
# cost_input = input("Enter the cost per litre (leave blank to use default $1): ")

# mpg = float(mpg_input) if mpg_input else 50
# cost = float(cost_input) if cost_input else 1

# result = fuel_cost(distance, mpg, cost)

# print(f"The fuel cost for a distance of {distance} miles is ${result:.2f}.")

# #5)	Create a function called most_common_char that takes a string as a argument 
# # and the returns the most common character in that string.
# def most_common_char(string):
#     char_count = {}
#     for char in string:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
    
#     # Find the maximum count
#     max_count = max(char_count.values())
    
#     # Find all characters with the maximum count
#     most_common_chars = [char for char, count in char_count.items() if count == max_count]

#     #to find if there is no character used more than once 
#     if max_count==1:
#         return "No common character!"
    
#     return most_common_chars

# text = input("Enter the string: ")
# result = most_common_char(text)
    
# print(f"The most common character(s) is/are: {', '.join(result)}")

# def most_common_char(string):
#     char_count = {}
#     for char in string:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
    
#     # Find the maximum count
#     max_count = max(char_count.values())
    
#     # Find all characters with the maximum count
#     most_common_chars = [char for char, count in char_count.items() if count == max_count]
    
#     # If the maximum count is 1, no character is repeated
#     if max_count == 1:
#         return "No common character"
    
#     return most_common_chars

# text = input("Enter the string: ")
# result = most_common_char(text)
# if isinstance(result, list):
#     print(f"The most common character(s) is/are: {', '.join(result)}")
# else:
#     print(result)

def most_common_char(str):
    check = []
    char = []
    data = {}

    for i in str:
        data[i] = str.count(i)
        
    max_val = max(data.values())

    for key, value in data.items():
        if value == max_val:
            char.append(key)
    print('The most common character is:- ',char, ':', max_val)
str = input("Enter a string:")
most_common_char(str)

# #6)	Write a function called primes that takes an integer 
# # value as an argument and returns a list of all prime numbers up to that number

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def primes(number):
#     prime_list = []
#     for num in range(2, number + 1):
#         if is_prime(num):
#             prime_list.append(num)
#     return prime_list

# integer = int(input("Enter the number: "))
# prime_numbers = primes(integer)
# print("The list of prime numbers is:", prime_numbers)

# #7)	Write a function called hcf that takes 2 integer values and returns the highest common factor 
# # of the numbers
# def hcf(n1, n2):
#     factors_a = prime_factors(n1)
#     factors_b = prime_factors(n2)
#     common_factors = set(factors_a).intersection(factors_b)
#     print(common_factors)
#     hcf = 1
#     for factor in common_factors:
#         hcf *= factor
#     return hcf

# def prime_factors(a):
#     factors = []
#     divisor = 2

#     while divisor <= a:
#         if a % divisor == 0:
#             factors.append(divisor)
#             a = a / divisor
#         else:
#             divisor += 1

#     return factors

# num1=int(input("Enter a number: "))
# num2=int(input("Enter another number: "))

# result=hcf(num1, num2)
# print(f"The hcf of {num1} and {num2} is: ", result)

# #8)	Write a function called is_valid_email  that takes an email address as an argument and returns 
# # True/False depending on whether it is a valid email address.
# # Check rules:
# # a.	Must contain at least 1 character before the at symbol
# # b.	Must contain an @ symbol
# # c.	Must have at-least 1 character after the @ symbol and before the period(.)
# # d.	Must contain at least 1 character after the last period(.).
# # e.	Maximum 256 characters
# # f.	Must start with a letter or a number

# def is_valid_email(email_address):
#     if len(email_address) > 254:
#         return False
    
#     if not (email_address[0].isalpha() or email_address[0].isdigit()):
#         return False
    
#     # Check for exactly one '@' symbol
#     at_index = email_address.find('@')
#     if at_index == -1 or email_address.count('@') != 1:
#         return False
    
#     # Split the email address into local and domain parts
#     local = email_address[:at_index]
#     domain = email_address[at_index + 1:]
    
#     # Check the length of the local part
#     if len(local) < 1 or len(local) > 64:
#         return False
    
#     # Check if there's at least one character after '@' and before the last '.'
#     if '.' not in domain:
#         return False
    
#     # Split the domain into parts by period
#     domain_parts = domain.split('.')
    
#     # Check if there's at least one character after the last '.'
#     if len(domain_parts[-1]) < 1:
#         return False
    
#     # Check if each part of the domain before the last '.' has at least one character
#     for part in domain_parts[:-1]:
#         if len(part) < 1:
#             return False
    
#     return True

# email = input("Enter your email address (Example: abcd@gmail.com): ")
# if is_valid_email(email):
#     print("The email address is valid.")
# else:
#     print("The email address is not valid.")


