#write a program of class named shape. Include the methods area and peimeter. Implement 
#subclasses for the shapes like circle, square and triangle 
# import math
# class Shape:
#     def __init__(self, length):
#         self.length=length


# class Square(Shape):
#     def __init__(self, length):
#         super().__init__(length)

#     def areaofSquare(self):
#         a= self.length**2
#         return a
    
#     def perimeterofSquare(self):
#         p=4*self.length
#         return p

# class Triangle(Shape):
#     def __init__(self, base, height, side, length):
#         super().__init__(length)
#         self.base=base
#         self.height=height
#         self.side=side

#     def areaoftriangle(self):
#         area_T= 0.5*self.base* self.height
#         return area_T
#     def perimeteroftriangle(self):
#         perimeter_T=self.side + self.side + self.base
#         return perimeter_T
#     def __repr__(self):
#         return f"Base: {self.base}, Height: {self.height}, sides= {self.side}"
#     def __str__(self):
#          return f"Base: {self.base}, Height: {self.height}, sides= {self.side}"

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius=radius
#     def area_circle(self):
#         c= math.pi * (self.radius**2)
#         return c
#     def circumference(self):
#         p=2*math.pi*self.radius
#         return p
#     def __repr__(self):
#         return f"Circle(radius={self.radius})"
    
# u_choice= input('''select the shape you want to find the area and perimeter: 
#                 for circle type c
#                 for square type s
#                 for triangle type t
#                 to quit type q:   ''').lower()
# if u_choice=="c":
#     # r=int(input("Enter the radius: "))
#     circle=Circle(12)
#     print(circle.__repr__())
#     # print("Area of circle is: ", circle.area_circle())
#     # print("Perimeter of circle is: ", circle.circumference())
# elif u_choice == "s":
#     l=int(input("Enter the length: "))
#     square=Square(l)
#     print("The area of square is: ", square.areaofSquare())
#     print("The perimeter of square is: ", square.perimeterofSquare())
# elif u_choice=="t":
#     b=int(input("Enter the base: "))
#     h=int(input("Enter the height: "))
#     l=int(input("Enter the length: "))
#     s=int(input("Enter the side: "))
#     triangle=Triangle(b, h, l, s)
#     print("The area of triangle is: ", triangle.areaoftriangle())
#     print("The perimeter of triangle is: ", triangle.perimeteroftriangle())
# elif u_choice == "q":
#     print("Thank you for using the program")
#     quit()
# else:
#     print("Invalid input")

#finding distance, quadrant, slope and relation between lines
#  for the point having x and y axis
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return "Ist Quadrant"
        elif self.x < 0 and self.y > 0:
            return "IInd Quadrant"
        elif self.x < 0 and self.y < 0:
            return "IIIrd Quadrant"
        elif self.x > 0 and self.y < 0:
            return "IVth Quadrant"
        elif self.x == 0 and self.y != 0:
            return "Y-axis"
        elif self.y == 0 and self.x != 0:
            return "X-axis"
        else:
            return "Origin"
        
    def slope(self, other):
        if other.x == self.x:
            return "Vertical Line, undefined slope"
        else:
            m = (other.y - self.y)/(other.x- self.x)
            return m

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.slope = p1.slope(p2)
        
    def isParallel(self, other):
        return self.slope == other.slope

    def isPerpendicular(self, other):
        if self.slope == 0 and other.slope == float('inf'):
            return True
        elif self.slope == float('inf') and other.slope == 0:
            return True
        return self.slope * other.slope == -1
    
# Values for point p1
x1 = int(input("Enter the x-value for point p1: "))
y1 = int(input("Enter the y-value for point p1: "))

# Values for point p2
x2 = int(input("Enter the x-value for point p2: "))
y2 = int(input("Enter the y-value for point p2: "))

# Values for point p3
x3 = int(input("Enter the x-value for point p3: "))
y3 = int(input("Enter the y-value for point p3: "))

# Values for point p4
x4 = int(input("Enter the x-value for point p4: "))
y4 = int(input("Enter the y-value for point p4: "))


# Point p1
p1 = Point(x1, y1)
print("The given point p1 lies in/on: ", p1.quadrant())

# Point p2
p2 = Point(x2, y2)
print("The given point p2 lies in/on: ", p2.quadrant())

# Point p3
p3 = Point(x3, y3)
print("The given point p3 lies in/on: ", p3.quadrant())

# Point p4
p4 = Point(x4, y4)
print("The given point p4 lies in/on: ", p4.quadrant())

#distance between points p1 and p2
print("The distance between both points p1 and p2 is: ", p1.distance(p2))

#slope between points p1 and p2
print("The slope between both points p1 and p2 is: ", p1.slope(p2))

#distance between points p3 and p4
print("The distance between both points p3 and p4 is: ", p3.distance(p4))

#slope between points p3 and p4
print("The slope between both points p3 and p4 is: ", p3.slope(p4))

line_1=Line(p1, p2)
line_2=Line(p3, p4)

# Check if the lines are parallel or perpendicular
print("Are the lines parallel? ", line_1.isParallel(line_2))
print("Are the lines perpendicular? ", line_1.isPerpendicular(line_2))




