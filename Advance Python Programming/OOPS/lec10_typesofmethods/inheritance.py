#inheritance is the pillar of oops that means to get the functionalities of superclass(that inherits)
#  into subclass (that gets inherited) the sub class gets all the functionalities in it after it inherits the 
#functions/methods of superclass


class a:
    x=5

    @classmethod
    def display(cls):
        print(cls.x)

class b(a):
    pass

import datetime
class Employee:
    bonus=2000
    def __init__(self, fname, lname, salary):
        self.fname=fname            #class variables
        self.lname=lname
        self.salary=salary
    def display(self):
        print(f"{self.fname}, {self.lname}, {self.salary}")
    def fullname(self):
        print(f"{self.fname} {self.lname}")

    def salary_with_bonus(self):
        return self.salary + self.bonus 
    @classmethod
    def fromstring(cls, emp):
            fname, lname, sal = emp.split('-')
            return cls(fname, lname, sal)
    
    @classmethod
    def setBonus(cls, bonus):
        cls.bonus = bonus
 
# user = 'ali-malik-20000'
# Employee.fromstring(user)            
# Employee.setBonus(8000)
    
class Manager(Employee):
    def __init__(self, fname, lname, salary, emp):
        # self.fname=fname
        # self.lname=lname
        # self.salary=salary
        super().__init__(fname, lname, salary) #in order to handle redendency we use super method to reduce the parameters that are same in all 
        #super classes
        self.emp=emp
        def display(self):
            super().display()
            for e in self.emp:
                e.fullname()

            print("Employee list: ", emp)

    
emp=Employee("Furqan", "Irfan", 60000)
  
emp2=Employee("Ali", "Hamza", 50000)
mng_1 = Manager("Ali", "Azhar", 40000, [emp, emp2])

# print(help(Manager))
mng= Manager("Ali", "Azhar", 40000, [emp, emp2])
mng.display()