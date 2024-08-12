import datetime
class Employee:
    def __init__(self, fname, lname, salary):
        self.fname=fname            #class variables
        self.lname=lname
        self.name=self.fname + " " + self.lname
        self.salary=salary
    def display(self):
        print(f"{self.fname}, {self.lname}")
    def fullname(self):
        print(f"{self.name}")

    @property       #Because of this decorator when we change the value of fname or lname it will
    #automatically change the value of name it is a kind of getter
    def name(self):
        return self.fname + ' ' + self.lname

    @name.setter
    def name(self, value):
        self.fname, self.lname = value.split(" ")

    #deletor method
    @name.deleter
    def name(self):
        print("Deleting name!!")
        self.fname=None
        self.lname=None

    def __str__(self):
        return f"Employee('{self.fname}', '{self.lname}', {self.salary})"
    
e=Employee("Maham", "Minhas", 20000)


del e.name
print(e)
