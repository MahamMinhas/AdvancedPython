#1)	Write a Python program to input values in list and then find product of all the items in a list.
num=int(input("Enter the number of values you want to enter: "))
list=[]
product=1
for i in range(num):
    values=int(input("Enter the values: "))
    product=product*values
    list.append(values)
print(list)
print("The product of values in list is: ",product)

#2)	Write a Python program to input string values in list and output a list 
#containing no of letters of each string

string_value=int(input("Enter the no. of strings: "))
list=[]

for i in range(string_value):
    value=input("Enter the strings: ")
    list.append(len(value))
print(list)

#3)	Write a Python program to check if a list is empty or not

list=["maham", "zahra"]
check_list=True
if(len(list)<=0):
    print("The list is not empty=  ", not check_list)
else:
    print("The list is not empty= ",check_list)

#4)	Write a Python program to remove duplicates from a list.
num=int(input("Enter the number of values: "))
original_list=[]
d_list=[]
for i in range(num):
    values=int(input("Enter the values: "))
    original_list.append(values)
    if values not in d_list:
        d_list.append(values)
print(original_list)
print(d_list)


#5)	Write a Python program that will input string values in a list and ask user to enter one length value. 
# Program will output a list containing words that are equal to length variable.

num_words = int(input("Enter the number of words: "))
words_list = []

for _ in range(num_words):
    word = input("Enter a word: ")
    words_list.append(word)
length_value = int(input("Enter the length value: "))

# Create a list containing words that are equal to the length value that user entered
filtered_words = []
for word in words_list:
    if len(word) == length_value:
        filtered_words.append(word)
print("Words with length", length_value, ":", filtered_words)



#6)	Write a Python function that takes two lists and returns True if they have at least one common member.
list1=[]
list2=[]
number=int(input("Enter the number of values in both list: "))
for i in range(number):
    values=int(input(f"[LIST-1] Enter the values {i+1}: "))
    list1.append(values)
for j in range (number):
    value=int(input(f"[LIST-2] Enter the values {j+1}: "))
    list2.append(value)
print(list1)
print(list2)

for i in range(values):
    for x in range(value):
        if(list1[i]==list2[x]):
            match=True
print(match)

# 7)	Write a Python program to input numbers from user and print a list of number which are prime.
num = int(input("Enter the number of values: "))
values_list = []
prime_list = []

for i in range(num):
    value = int(input("Enter the value: "))
    values_list.append(value)
    
    if value > 1:
        is_prime = True
        for j in range(2, value):
            if value % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(value)

print("List of numbers:", values_list)
print("List of prime numbers:", prime_list)

    
            
# # 8)	Write a Python program to get unique values from a list input by user.
int(input("Enter the number of values: "))
original_list=[]
d_list=[]
for i in range(num):
    values=int(input("Enter the values: "))
    original_list.append(values)
    if values not in d_list:
        d_list.append(values)
print(original_list)
print(d_list)

# 9)	Write a Python program to get the frequency of elements in a list.

num = int(input("Enter the number of values: "))
values_list = []
unique_values = []
frequency = []

for i in range(num):    
    values = input("Enter the values: ")
    values_list.append(values)

for value in values_list:
    if value not in unique_values:
        unique_values.append(value)
        frequency.append(values_list.count(value))

# Print the list of values and their frequencies
print("Values List:", values_list)
print("Frequency of unique values:")

for i in range(len(unique_values)):
    list=[f"{unique_values[i]}: {frequency[i]}"]
    print(*list, sep = "\n")


# 10)	Write a Python program to input a list of numbers from user and print square 
# and cube of each number in the list

num=int(input("Enter the number of values: "))
list=[]
squares=[]
cubes=[]

for i in range(num):
    values=int(input("Enter the values: "))
    list.append(values)
    squares.append(values**2)
    cubes.append(values**3)
print(list)
print(squares)
print(cubes)


