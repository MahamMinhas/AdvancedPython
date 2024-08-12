# #printing even numbers using while loop
# number=int(input("enter the number"))
# i=0
# while (i<=number):
#     if(i%2==0):
#         print("The even numbers are: ", i)
#     i+=1

# #better performance in this solution
# num=int(input("enter the number"))
# i=0
# while (i<=number):
#     print("The even numbers are: ", i)
#     i+=2

#taking 2 numbers from user and displaying even numbers between those 2 numbers
# num1=int(input("enter the first number"))
# num2=int(input("enter the second number"))

# # i=num1
# # if(i<num2):
# #     while(i<=num2 and i%2==0):
# #         print("The even numbers are: ", i)
# #         i+=1
# # else:
# #     while(i>=num2 and i%2==0):
# #         print("The even numbers are: ", i)
# #         i-=1

# if(num1>=0 and num2>=0):
#     if(num1<num2):
#         if(num1%2!=0):
#             num1+=1
#         while(num1<=num2):
#             print(num1)
#             num1+=2
#     elif(num1>num2):
#         if(num1 % 2 !=0 ):
#             num1-=1
#         while(num1 >=num2):
#             print(num1)
#             num1-=2
#     else:
#         print("Both numbers are equal")
# else:
#     print("Please enter positive numbers")

#printing number sequence from 2^0 to 2^10
# i=0
# while(i<=10):
#     print(2**i)
#     i+=1

#printing sequence by taking number from user
# num=int(input("enter the number"))
# i=0
# if(num>=0):
#     while(i<=num):
#         print(2**i)
#         i+=1
# else:
#     print("Enter a positive number")

#FOR LOOPS 
#printing even numbers using for loop

# number1=int(input("Enter the first number: "))
# number2=int(input("Enter the second number: "))

# if(number1>=0 and number2>=0):
#     if(number1<number2):
#         if(number1%2 !=0):
#              number1+=1
#         for i in range(number1,number2+1,2):
#             print(i)
    
#     elif(number1>number2):
#         if(number1%2 !=0):
#             number1-=1
#         for i in range(number1,number2-1,-2):
#             print(i)
#     else:
#         print("Both numbers are equal")
# else:
#     print("Please enter positive numbers")


#Take a string (hardcode) take input from user for a variable guess (user input). Match the length of the 
# both words if length not equal then wrong else if length is equal then check if string is same character by 
# character if not wrong else the print the characters that are at correct index and are matched and # for those 
# that are  present but not on right index and ~ for those that are toto wrong.

word="hello"
guess=input("Enter the word: ")

if(len(word)==len(guess)):
    guessed=""
    for i in range(len(word)):
        if(guess[i]==word[i]):
           guessed+=guess[i]
        elif(word.find(guess[i]) != -1):
             guessed+="#"
        else:
             guessed+="~"
    print(guessed)
       
else:
    print("OOPS! your guess is wrong")


#Sir's method
# if(len(word)==len(guess)):
#     i=0
#     output=""
#     for x in word:
#         if(x==guess[i]):
#             output+=x
#         elif(word.find(guess[i]) != -1):
#             output+="#"
#         else:
#              output+="~"
#         i+=1
#     print(output)
# else:
#     print("OOPS! your guess is wrong")
