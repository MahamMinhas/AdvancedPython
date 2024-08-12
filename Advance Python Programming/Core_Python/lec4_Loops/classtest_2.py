#1. Calculate the sum of all numbers from 1 to a given number entered by user
i=1
sum=0
num=int(input("Enter the number: "))
while (i<=num):
    sum=sum+i
    i=i+1
print("The final sum of all the numbers is: ", sum)

#2. Write a program to print multiplication table of a given number
number=int(input("Enter the number: "))
if(number>0):
    for i in range(1,11):
        print(number,"x",i,"=",number*i)
else:
    print("Invalid Number. Enter a poitive number greater than 0")

#3. Write a program to count the total number of digits in a number using a while loop.
num = int(input("Enter the number to be counted: "))
count = 1
if(num!=0):
    while(count<=num):
        num=num // 10
        count += 1
else:
    print("Invalid input")

print("The number of digits in the number is:", count)

#4. Write a program that check whether the entered number is a prime number or not.

num = int(input("Enter a number: "))

if (num == 1):
    print(num, "is not a prime number")
elif(num==2):
    print(num, "is a prime number")
elif (num > 1):
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")

#5. Write a program to print first 10 numbers in Fibonacci Sequence. The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
#example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.
a=0
b=1
for i in range(10):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

#6. Write a program to use the loop to find the factorial of a given number.

num = int(input("Enter a number: "))
factorial=1
if(num>=1):
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)
else:
    print("Invalid input. Enter a positive number")


#7. Write a program to print the cube of all numbers from 1 to a given number

number=int(input("Enter the number: "))
if(number>0):
    for i in range(1,number+1):
        print(i,"x",i,"x",i,"=",i**3)
else:
    print("Invalid input. Enter a positive number")

#8. Write a program to print the following Pattern
# 1   1   1
# 2   4   16
# 3   9   27
# 4   16 64
# 5   25 125



for number in range(1, 6):
    square = number ** 2
    cube = number ** 3
    print(number, square, cube)
