#while loop
i=1         #lop control variable that handles working of the loop
while(i<=10):
    if(i==10):
        break;  #loop control statement that control the termination of loop 
    print(i)
    # print("helo world")
    i += 1    #i=i+1

i=10         #lop control variable that handles working of the loop
while(i>=1):
    print(i)
    # print("helo world")
    i -= 1    #i=i-1

num=int(input("Enter the number: "))
i=1
while(i<=num):
    print(i)
    i += 1

#FOR LOOP
for i in range(10): #last number is not included
    print(i)

#for i in range(start, stop, step) if 1 arg. by default its stop value

#Difference between while and for example
#While loop
message=input("Enter your name: ")
i=0
while(i<len(message)):
    print(message[i])
    i+=1

#for loop

message=input("Enter your name: ")

for i in message:
    print(i)