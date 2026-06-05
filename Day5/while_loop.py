#while loop 

count=1;
while count<=5 :
    print("Hello")
    count +=1

#print first 10 natural numbers

i=1
while i<=10 :
    print(i)
    i+=1

#infinite loop : loop that never ends.

while True:
    print("Infinite Loop")


 #infinite loop 
while i< 6 :
    print(i)
    i-=1

#print numbers from 1 to 100

i=1
while i<=100 :
    print(i)
    i+=1

#print numbers from 100 to 1

i=100
while i>=1 :
    print(i)
    i-=1

#print the multiplication table of number n 

n=int(input("Enter the number"))
i=1
while i<=10:
    print(n*i)
    i+=1

#print the list [  1,4,9,16,25,36,49,64,81,100] using loop (traverse the list)

list = [1,4,9,16,25,36,49,64,81,100]
index=0
while index<len(list):
    print(list[index])
    index+=1

#search for a number X in given tuple using loop

tuple =(1,4,9,16,25,36,49,64,81,100)

j=0
x=int(input("Enter number to search : "))
while j < len(tuple):
    if (tuple[j]==x):
        print("Found at index ", j)
    else: 
        print("Not found at index ",j)
    j+=1

#break and continue

print("Break :")
a=1
while a <= 5 :
    print(a)
    if(a==3):
        break  #breaks the loop when a==3 and doesnot print the number after 3
    a +=1


print("Continue :")
k=1

while k <= 10 :
    if(k%2 == 0):
        k+=1
        continue #skips the even values and prints the odd
    print(k)
    k+=1

