#Types of variables
a, b, c=10, 5, 7
print("The values of variables are: ")
print(a)
print(b)
print(c)
#int
a=4 
print(a)
#Checking type of variables
b=True
print(type(b))
#Studying String literal
message="Python's world"  #single quote outside if double is used inside and vice versa
mssg='python\'s world'
print(mssg)

#For multi-line string
multi_line="""asdfghjk
wertybnm

ertyuim"""

print(multi_line)

#Concatination
line="hello"+"world"
print(line)

#repitition
repp="hello"*3
print(repp)

#finding the length of string
print(len(message))

#index of the character
print(message[2])

#to access last character of the string
print(message[len(message)-1])

#accessing a specific part of the string
print(message[0:6]) #the number after colon means to eliminate the part of string after that

#if we want to know something about a function
print(help(len))

#applying function on specific variable
print(message.lower())
print(message.upper())
print(message.count("world"))#counts how many times a word or character is repeated in a string 
print(message.find("Py"))
print(message[3:].find('l'))
print(message.replace("world", "community"))
print(message)
print(message.lower().replace("world".lower(), "community"))
name="                   maham"
print(name.strip())
print(message.split(" "))
