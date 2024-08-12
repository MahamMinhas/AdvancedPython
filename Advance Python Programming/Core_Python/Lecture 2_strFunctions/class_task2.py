#Activity 1 Counting the characers in the string irrespective of case 
#print(message.upper.count("Python".upper()))
#efficient solution is to solve the problem without using more memory space or variables
message2="You are learning python. Python's Awesome"
new_message=message2.lower()
print(new_message.count("PYTHON".lower()))

#Activity 2 write a program to access the first, middle and last character of the string and concatenate it
text= "world"
print(text[0]+text[len(text)//2]+text[len(text)-1])

#Activity 3 retrieving middle 3 characters of a string
text_2="wonderland"
mid=len(text_2)//2
#next_mid=mid+1
#prev_mid=mid-1
print(text_2[len(text)//2-1]+text_2[len(text)//2]+text_2[len(text)//2+1])
#print(prev_mid+mid+next_mid)
print(text_2[mid-1:mid+2]) #mid+2 to exclude the next value/character that is to be excluded

#Activity 4  Write a program that concatenates the s2 in centre of s1 
s1="live"
s2="show"
mid_s1=len(s1)//2
print(s1[:mid_s1]+s2+s1[mid_s1:])

#Activity 5 
s1="Hello"
s2="World"
begin_s1=s1[0]
begin_s2=s2[0]
mid_s1=s1[len(s1)//2]
mid_s2=s2[len(s2)//2]
end_s1=s1[len(s1)-1]
end_s2=s2[len(s2)-1]

print(begin_s1+begin_s2+mid_s1+mid_s2+end_s1+end_s2)