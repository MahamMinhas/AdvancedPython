#regular methods that have their first parameter as their own instance  (self)
'''
class methods:
    it has the @symbol called as decorator at the start
    it is used to define a special method in a class


'''
class Person:
    bonus=2000
    def __init__(self, fname, lname, salary):
        self.fname=fname            #class variables
        self.lname=lname
        self.salary=salary
    def display(self):
        print(f"{self.fname}, {self.lname}, {self.salary}")

    def salary_with_bonus(self):
        return self.salary + self.bonus
    @classmethod
    def fromstring(cls, emp):
            fname, lname, sal = emp.split('-')
            return cls(fname, lname, sal)
    
    @classmethod
    def setBonus(cls, bonus):
        cls.bonus = bonus

    @classmethod            #alternative constructors that make an object start the name with from
    def class_method(cls, bonus):
        cls.bonus=bonus
    def changebonus(cls, bonus):
        Person.bonus=bonus     #wrong way

user = 'ali-malik-20000'
Person.fromstring(user)            
Person.setBonus(8000)

