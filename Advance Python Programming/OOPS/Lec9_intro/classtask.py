#Task 1: 
import math
class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def values_display(self):
        print(f"a= {self.a}, b= {self.b}, c= {self.c}")
    def nature(self):
        formula=(self.b**2)-(4*self.a*self.c)
        if formula>0:
            number=math.sqrt(formula)
            if number.is_integer():  
                print("The number is a perfect square. It is rational")  
            else:  
                print("The number is not a perfect square. It is irrational")
        elif(formula==0):
            print("The root is real and equal")
        else:
            print("The root is complex, Distinct")
    @classmethod
    def fromstring(cls, str):
        a, b, c = str.split(",")
        return cls(int(a), int(b), int(c))


# num1=int(input("Enter a number: "))
# num2=int(input("Enter a number: "))
# num3=int(input("Enter a number: "))

i=input("Enter the numbers: ")

answer=Quadratic.fromstring(i)
answer.values_display()
answer.nature()

# if(i!=0):

# else:
#     print("num1 cannot be 0")
        
