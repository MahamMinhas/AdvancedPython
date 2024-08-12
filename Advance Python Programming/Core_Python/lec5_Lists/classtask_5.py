#Task 1 Write a program that will ask user to enter the number of subjects and then input values of marks 
#Program will output sum, average and percentage of student marks and find the highest and lowest marks

student_marks=[]
num_subjects=int(input("Enter the number of subjects: "))
sum=0 

for  i in range(num_subjects):
    marks=int(input("Enter The marks of students: "))
    student_marks.append(marks)
    sum=sum+student_marks[i]                                   
    student_marks.append(marks)
print(student_marks)
print("The sum of all marks is: ", sum)      #This can be done in single loop using sum method
total_marks=num_subjects*100
percentage=int((sum/total_marks)*100)
print("The percentage of student marks is: ", percentage)
average=int(sum/num_subjects)
print("The average of student marks is: ", average)


highest_marks=student_marks[0]
lowest_marks=student_marks[0]

for i in student_marks:
    if(i>highest_marks):
        highes_marks=i
    if(i<lowest_marks):
        lowest_marks=i

print("The Highest marks are: ", highes_marks)
print("The lowest marks are: ", lowest_marks)

#Task 2 write a program that takes no. of values from user then add it in the list and then separate even and odd list

num=int(input("Enter the number of values: "))
List=[]

for x in range(num):
    elements=int(input("Enter the numbers: "))
    List.append(elements)

print(List)

#separate even and odd list
even_list=[]
odd_list=[]
for i in List:
    if(i%2==0):
        if i not in even_list:
            even_list.append(i)
    else:
        if i not in odd_list:   
            odd_list.append(i)
print("The list of even numbers: ", even_list)
print("The list of odd numbers: ", odd_list)




