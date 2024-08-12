'''
 functional programming 
   1. Reusability 
   2.   Structured Program
   3. Easy to debug (error finding is easy)
   4.   Easy to maintain (modification is easy)
'''
def helloworld():
    print("hello world!")

def addition(a, b):         #the values assigned during the definition of function are arguments
    return a+b

# addition(10, 5)    #the values assigned when calling the function are parameters 
# addition(4, -1)
# addition("hello", "class")
# helloworld()
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
add= addition(num1, num2)
print(add)

#when a function is called it performs its actions and then returns to where the function is called 
#so we can store iit in the variable then print it 


'''
TYPES OF ARGUMENTS:

1. ARBITRARAY ARGUMENTS:
        If you do not know how many arguments that will be passed into your function, add a * before the 
        parameter name in the function definition.This way the function will receive a tuple of arguments,
        and can access the items accordingly:
'''

def my_function(*kids):
#   print("The youngest child is " + kids[2])
    for n in kids:
        print(n)
        

my_function("Emil", "Tobias", "Linus")


'''
2. KEYWORD ARGUMENTS:
    You can also send arguments with the key = value syntax. 
    This way the order of the arguments does not matter.
    The argumment and parameters passed while calling should be same else it will be error (Unexpected keyword 
    arguments)

'''

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

'''
3. ARBITRARY KEYWORD ARGUMENTS:
    If you do not know how many keyword arguments that will be passed into your function, 
    add two asterisk: ** before the parameter name in the function definition.
    This way the function will receive a dictionary of arguments, and can access the items accordingly:

'''

def my_function(**kid): #the **kid here is a dictionary
 # print("His last name is " + kid["lname"])
 for n in kid:
    print(n ,":", kid[n] )
    

my_function(fname = "Tobias", lname = "Refsnes")

'''
4. POSITIONAL ARGUMENTS:
    You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
    To specify that a function can have only positional arguments, add , / after the arguments:

'''

def my_function(x, /):      #here if we add keyword arguments it gives error  
  print(x)

my_function(3)

# Without the , / you are actually allowed to use keyword arguments even 
# if the function expects positional arguments:
# Example
def my_function(x):
  print(x)

my_function(x = 3)

#we can also pass list and dictionary to the function as a parameter

'''
5. KEYWORD-ONLY ARGUMENTS:
    To specify that a function can have only keyword arguments, add *, before the arguments:

'''

def my_function(*, x):
  print(x)

my_function(x = 3)

'''
6. COMBINED POSITIONAL-ONLY AND KEYWORD-ONLY ARGUMENTS:
    You can combine the two argument types in the same function.
     Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

'''

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


#Lambda Function is used to minimize and simplify the functions to one line function

