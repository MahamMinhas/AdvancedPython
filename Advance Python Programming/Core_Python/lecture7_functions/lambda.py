def sum(a, b):
    return a+b

x=lambda a,b : a+b

#concise code
# function stored in a variable 

print(x(10,5))  

#lambda function can be returned in a function as a value 


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)   #Here the myFunc returning lambda function the value of n 

print(mydoubler(11))   # the value of a 