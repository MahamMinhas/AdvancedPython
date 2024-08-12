#1) What is a variable 
#A variable is a name of reserved memory space for the data that we want to define and use in our program
#Example:
intro="Hello World" # it is a variable that stores string type of data 
x=5 #This variable stores integer type of data. In python we dont need to specify the type exclusively it gets to know 
#the type of data itself 

#2) What is operator?
#An operator is a symbol that tells the computer to perform certain mathematical or logical operations
#The basic operations that are used in python are: +, -, *, /, //, **, %, !, &, <, >, <=, >=, !=
#There are different types of operators 1. mathematical operators 2. Logical operators
#Example:
a=2
b=9
print("The sum of two numbers: ", a+b)
print("The difference of two numbers: ", a-b)
print("The product of two numbers: ", a*b)
print("The division of two numbers: ", a/b)
print("The exponent of a number: ", a**b)

#3) What is tupple?
#Immutable (data cannot be changed), duplication allowed, ordered(sequence followed)
#declared with courses=()
#Example:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#4) What is List?
#List is ordered collection of items which can be of any data type, including strings, integers,
# floats, and other lists also can store tuples and other data structures like dictionary.
#  Lists are denoted by square brackets [] and are mutable,
#Example:

courses=["Programmingg Fundamentals", "Python", "OOPS"]
print(courses[0])   #retrieving a specific index
print(courses)  #retreiving whole list
print(type(courses)) 

students=["Ali", 1,50,  True]  #can store multiple data types

#5. What is Dictionary
#Dictionary (This is the most frequently used ) [Mutable, No Duplication, ordered] declared with {}
#cannot contain 2 same keys 
#in latest version dictionaries are ordered
#can store string, integer, float, bool and another list
#Example:

student={
    "name":"maham",
    "age": 22,
    "courses":["python", "android"],
    "address": {
        "city": "Lahore",
        "country": "Pakistan"    }
}

print(student["name"])   #same key names cannot be used
print(student["address"]["city"])    # can also be accessed using loops 

#6) Define For loop
#for loop (conter loop)
	#for loop is most commonly used than while loop
##FOR LOOP
for i in range(10): #last number is not included
    print(i)

#for i in range(start, stop, step) if 1 arg. by default its stop value

#7) What is comprehension loop
#The Nested loop is the comprehension loop that means the loop within the loop 
#The "inner loop" will be executed one time for each iteration of the "outer loop"
#Example: The below example uses the nested loop that performs different actions 
# within a certain range of outer loop
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




#8) What is Function
#functional programming is the type of programming that performs its actions through function calls 
#    1. Reusability 
#    2.   Structured Program
#    3. Easy to debug (error finding is easy)
#    4.   Easy to maintain (modification is easy)
# 
def helloworld():
    print("hello world!")

def addition(a, b):         #the values assigned during the definition of function are arguments
    return a+b

