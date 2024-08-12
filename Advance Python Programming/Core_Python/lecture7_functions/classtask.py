# def addition(a, b):        
#     print(a+b)

# def subtract(a, b):   #in case user gives lesser parameters we set a value by default liike b=5      
#     print(a-b)


# def division(a, b):         
#     print(a/b)

# def multiplication(a, b):         
#     print(a*b)

# def exponent(a, b):         
#     print(a**b)

# num1=int(input("Enter a numbber: "))
# num2=int(input("Enter a number: "))

# addition(num1, num2)
# subtract(num1, num2)
# multiplication(num1, num2)
# division(num1, num2)
# exponent(num1, num2)


# def square(a):
#     return  a**2

# number=int(input("Enter the number: "))
# answer=square(number)
# print("The square of the number is: ", answer)

#Arguments are often shortened to args in Python documentations.
#https://www.w3schools.com/python/python_functions.asp
#to make an empty function we write pass in the body
def function():
    pass
#this performs no action 

#Write a program that find sum of all the values user enters in a function

# def addition(*values):
#     for i in values:
#         i+=values
#         print("The sum of values is ",i)

# addition(3, 4, 6, 7)

# def addition(*values):
#     total_sum = 0
#     for value in values:
#         total_sum += value
#     print("The sum of values is", total_sum)

# addition(3, 4, 6, 7)

#using list
# def sum(num):
#     s = 0
#     for n in num:
#         s += n
    
#     return s

# numbers = []
# len_list = int(input("Length of list:"))
# for i in range(len_list):
#     num = int(input("Number:"))
#     numbers.append(num)

# # print(numbers)
# add = sum(numbers)

# print("Sum:",add)

#Write a program that will find maximum number out of 3 numbers in a function 
# def greater(a, b, c):
#     if a>b and a>c:
#         print("The greatest number is : ", a)
#     elif b>a and b >c:
#         print("The greatest number is: ", b)
#     else:
#         print("The maximum number is: ", c)
    

# num1=int(input("Enter the 1st number: "))
# num2=int(input("Enter the 2nd number: "))
# num3=int(input("Enter the 3rd number: "))

# greater(num1, num2, num3)

#user can only enter values between 1-12, check how many days in a month but before check if its a leap year
def days_in_month(m, y):
    d=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if(m>=1 and m<=12):
        if(m==2):
            if(is_leap_year(y)):
                d[1]=29
        return d[m-1]
    else:
        print("Invalid month")
        return -1
    
def is_leap_year(y):        #check the year is leap year or not 
    if(y%4==0):
        return True
    else:
        return False


m=int(input("Enter the number of month [1-12]: "))
y=int(input("Enter the year (4=digit number): "))   #User entered values

days=days_in_month(m, y)  #function call

if(days!=-1):
    print(f"No. of days in {m}, {y}: ", days)