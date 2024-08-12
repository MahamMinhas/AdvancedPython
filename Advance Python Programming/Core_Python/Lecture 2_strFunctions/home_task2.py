#Implementing Python String Functions
#Capitalize() method 
sentence="this is python class"
print("After Capitalize method: ", sentence.capitalize())

#casefold() method
text="THIS IS PYTHON CLASS"
print("After casefold method: ", text.casefold())

#centre() method
txt="center"
print("After Centralize method: ", txt.center(15, "$"))

#encode() method
txt = "My name is Mah@m"
print("Encode method: ", txt.encode(encoding="ascii",errors="replace"))
print("example2 for encode: ", sentence.encode())

#endswith() method
txt = "Hello, welcome to my world."
print("Endswith method: ", txt.endswith("."))
print("Endswith method exapmle 2: ", txt.endswith("my world."))
print("Endswith method exapmle 3: ", txt.endswith("my world.", 18, 26))

#expandndtabs() method
txt="this\t is\tpython\tclass"
print("Expandtabs method: ", txt.expandtabs(5))

#format() method
txt_f="My name is {fname}, I'm {age}".format(fname="Maham", age=22)
print(txt_f)

#index() method
txt = "Hello, welcome to my world."
print("Index method: ", txt.index("to"))

#isalnum() method
txt = "Hello123"
print("Isalnum method: ", txt.isalnum())

#isalpha() method
txt = "Helloworld"
print("Isalpha method: ", txt.isalpha())

#isascii() method 
txt = "@ /ello 12"
print("Isascii method: ", txt.isascii())

#is decimal() method
txt = "1.23"
print("Isdecimal method 1: ", txt.isdecimal())
txt = "123%"
print("Isdecimal method 2: ", txt.isdecimal())
txt = "123"
print("Isdecimal method 3: ", txt.isdecimal())
txt = "123A"
print("Isdecimal method 4: ", txt.isdecimal())

#isdigit() method
digit="5543"
print("isdigit method: ", digit.isdigit())  #does not take direct integers but in the form of strings

#isidentifier() method
string = "Hello123"
print("isidentifier method 1: ", string.isidentifier())
string2 = "6Hello1$"
print("isidentifier method 2: ", string2.isidentifier())
string3 = "-Hello123"
print("isidentifier method 3: ", string3.isidentifier())
string4 = "_Hello123"
print("isidentifier method 4: ", string4.isidentifier())

#islower() method
string = "hello world"
print("islower method 1: ", string.islower())

#isupper() method 
string = "HELLO WORLD"
print("isupper method 1: ", string.isupper())

#isnumeric() method
string = "123"
print("isnumeric method 1: ", string.isnumeric())

#isspace() method
string = "Hello123"
print("isspace method: ", string.isspace())

#isprintable() method
string = "Hello123"
print("isprintable method: ", string.isprintable())

#istitle() method
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print("istitle method 1: ", a.istitle())
print("istitle method 2: ",b.istitle())
print("istitle method 3: ",c.istitle())
print("istitle method 4: ",d.istitle())

#join() method
a = "Hello"
b = "World"
print("join method 1: ", a.join(b))

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print("Join method 2: ", x)

#ljust() method
a = "Hello"
print("ljust method 1: ", a.ljust(10, "O"))

#lstrip() method
txt = "     banana     "

x = txt.lstrip()

print("lstrip method: ","of all fruits", x, "is my favorite")

#maketrans() method
txt = "Hello Sam!"
mytable = str.maketrans("S", "M")
print("translate method: ", txt.translate(mytable))

#partition() method
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print("partition method: ", x)

#rfind() method
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print("rfind method: ",x)

#rindex() method
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print("rindex method: ",x)

#rjust() method
txt = "banana"
x = txt.rjust(20)
print("rjust method: ",x, "is my favorite fruit.")

#rpartition() method
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print("rpartition method: ",x)

#rsplit() method
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print("rsplit method: ",x)

#rstrip() method
txt = "     banana     "
x = txt.rstrip()
print("rstrip method: ","of all fruits", x, "is my favorite")

#splitlines() method
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print("splitlines method: ", x)

#startwith() method
txt="Hello to the Python class"
print("startwith method: ",txt.startswith("Hello"))

#swapcase() method'
string_swap="Hello My name is MAHAM"
print("swapcase method: ",string_swap.swapcase())

#title() method
string_title="hello my name is maham"
print("title method: ",string_title.title())

#translate() method
string_translate="Hello My name is MAHAM"
print("translate method: ",string_translate.translate({ord(i): None for i in "aeiou"}))
mydict = {83:  80}
txt = "Hello Sam!"
print("translate method 2: ",txt.translate(mydict))

#zfill() method
txt = "50"
x = txt.zfill(10)
print("zfill method: ",x)
