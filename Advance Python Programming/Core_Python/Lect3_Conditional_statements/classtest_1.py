#The number variable below is used in the q 1, 2,3  
number=int(input("Enter a number: "))

# # 1. Write a program to check whether a number entered by user is even or odd.
if(number%2==0):
   print(number, "is even")
else:
   print(number, "is odd")

# # 2. Write a program to check whether a number is divisible by 7 or not.
if(number%7==0):
     print(number, "is divisible by 7")
else:
   print(number, "is not divisible by 7")

# #3. Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print “Bye”
if(number%5==0): 
     print("Hello")
else:
     print("Bye")

# #4.	Write a program to calculate the electricity bill according to the following criteria:
# # Unit                                                     Price  
# # a.	First 100 units                                      no charge
# # b.	Next 100 units                                   Rs 5 per unit
# # c.	After 200 units                                 Rs 10 per unit

units=int(input("Enter the electricity units: "))

if(units<=0):
    print("Invalid Input")  
elif(units>0 and units<=100):
        print("No charge")
elif(units>100 and units<=200):
    Bill=(units-100)*5
    print("Bill is: ",Bill)
else:
    Bill=(100*5)+(units-200)*10
    print("Bill is: ",Bill)

# #5)	Write a program that display the grade if the percentage is given according to the following criteria:
# # Marks                                    Grade
# # > 90                                         A
# # > 80 and <= 90                               B
# # >= 60 and <= 80                              C
# # below 60                                     D

percentage=int(input("Enter the marks percentage: "))
if(percentage<0):
    print("Invalid input")
elif(percentage>=0 and percentage<60):
    print("The grade is D")
elif(percentage>=60 and percentage<=80):
    print("The grade is C")
elif(percentage>80 and percentage<=90):
    print("Thr grade is B")
else:
    print("The grade is A")

# #6)	Write a program that display the road tax to be paid if the cost price is given according to the following criteria:
# # Cost Price				Tax
# # > 100000				15%
# # > 50000 and <= 100000		10%
# # <= 50000				5%

cost_price=int(input("Enter the cost price: "))
if(cost_price<0):
    print("Invalid input")
if(cost_price>=0 and cost_price <=50000):
    tax=(cost_price*5//100)
    print("The road tax to be paid is: ", tax, "rs/-")
elif(cost_price>50000 and cost_price <=100000):
    tax=(cost_price*10//100)
    print("The road tax to be paid is: ", tax, "rs/-")
else:
    tax=(cost_price*15//100)
    print("The road tax to be paid is: ", tax, "rs/-")

# #7. Write a program to check whether a year is leap year or not.
year=int(input("Enter the year: "))
if(year%4==0):
    print("The year is leap year")
else:
    print("The year is not leap year")

# #8. Write a program to check whether a number is positive or negative
num=int(input("Enter the number: "))
if(num>0):
    print("The number is positive")
else:
    print("The number is negative")

# #9.	Write a program to find the largest number out of three numbers
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if(num1>num2 and num1>num3):
    print("The greatest number is", num1)

elif(num2>num1 and num2>num3):
    print("The greatest number is", num2)
else:
    print("The greatest number is", num3)

# #10. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operator=input("Enter the operator")
if(operator=="+"):
    print("The sum is", num1+num2)
elif(operator=="-"):
    print("The difference is", num1-num2)
elif(operator=="*"):
    print("The product is", num1*num2)
elif(operator=="/"):
    if(num2==0):
        print("invalid number")
    print("The quotient is", num1/num2)
elif(operator=="//"):
    if(num2==0):
        print("invalid number")
    print("The integral division is: ", num1//num2)
elif(operator=="**"):
    print("The power is: ", num1**num2)
else:
    print("invalid operator")

# #11. Accept three sides of triangle and check whether the triangle is possible or not.
side1=int(input("Enter the first side: "))
side2=int(input("Enter the second side: "))
side3=int(input("Enter the third side: "))

if((side1+side2)<=side3 )or ((side1+side3)<=side2) or ((side2+side3)<=side1):
    print("Valid")
else:
    print("Invalid")


#12. Accept the kilometers covered and calculate the bill according to the following criteria:
# First 10 KM			Rs 11 / KM
# Next 90 KM			Rs 10 / KM
# After that				Rs 9 / KM
distance = int(input("Enter the distance: "))

if (distance <= 0):
    print("Invalid distance")
else:
    if distance <= 10:
        bill = distance * 11
    elif distance <= 100:
        bill = (10 * 11) + ((distance - 10) * 10)
    else:
        bill = (10 * 11) + (90 * 10) + ((distance - 100) * 9)
    
    print("The fare is", bill, "rs/-")
