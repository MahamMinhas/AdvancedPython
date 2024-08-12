#Task 1: Checking greater number
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))

if(num1>num2):
    print(num1, "is greater")
if(num2>num1):
    print(num2, "is greater")
if(num1==num2):
    print( num1, num2, "Both numbers are equal")

#Ttask 2: checking if number is positive, negative or zero
num=int(input("Enter a number: "))
if(num > 0):
    print(num, "The number is positive")

if(num<0):
    print(num, "The number is negative")

if(num==0):
    print(num, "The number is zero")

#Task 3 Calculating fare based on distance
distance= int(input("Enter the distance: "))
if(distance<0):
    print("Invalid distance")

if(distance==0):
    print("Fare is 0")

if(distance>=1):
    if(distance<=5):
      print("The fare is 200 rs/-")

if(distance>5):
    if(distance<=15):
       print("The fare is 500 rs/-")

if(distance>15):
    fare=((distance-15)*50)+500
    print("The fare is", fare, "rs/-")

#calculating fare method 2
if(distance <= 0):
    print("distance cannot be zero or -ve.")
if(distance > 0):
    if(distance <= 5):
        fare = 200
    if(distance > 5):
        if(distance <= 15):
            fare = 500
        if(distance > 15):
            # 20
            extra = distance - 15
            #5
            dis3 = extra * 50
            fare = dis3 + 500
            print("Fare for the distance", distance, "is", fare)
    print("your fare is:", fare)
#else statement
if(distance<=0):
    print("distance cannot be zero or -ve.")
else:
     if(distance<=5):
        print("Fare is 200 rs/-")
#elif statement
if(distance<=0):
    print("distance cannot be zero or -ve.")
elif(distance <=5):
    print("Fare is 200 rs/-")


#Task 4 greater number
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if(num1>num2 and num1>num3):
    print("The greatest number is", num1)

elif(num2>num1 and num2>num3):
    print("The greatest number is", num2)
else:
    print("The greatest number is", num3)

