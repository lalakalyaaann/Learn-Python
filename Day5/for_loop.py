list=[1,2,3,4,5]
tup=(2,4,6,8,10)

#for loop

print("For loop in list")
for val in list :
    print(val)
print("For loop in tuple")
for value in tup :
    print(value)

#for loop with else

str="KALYAN IS A STUDENT"

for char in str:
    print(char)
else:
    print("end of character.")


#print list 

nums=[1,4,9,16,25,36,49,64,81,100]
for i in nums :
    print(i)

#find a number in given list 

ind=0
to_find =49
for el in nums:
    if(to_find == el):
        print("Number found at index ",ind)
    ind+=1


#range function

for el in range(5): #returns from 0 to 5th index... i.e. 0,1,2,3,4
    print(el)

for ele in range(1,5): #returns from 1 to 4. 1 is included and 5 is excluded
    print(ele)

for elem in range (1,5,2): #returns from 1 to 4 with step value 2. 
    print(elem)

#print numbers from 1 to 100

for i in range(1,101):
    print(i)

#print numbers from 100 to 1

for i in range(100,0,-1):
    print(i)

#print the multiplicative table for n 

n =int(input("Enter a number :"))
for i in range (1,11):
    print(n*i)

#pass statement 

#pass is a null statement that does nothing . It is used as a placeholder for future code. 

for i in range(5):
    pass


#WAP to find the sum of first n numbers 

#using for loop

n=int(input("Enter a number 'n' : "))
sum=0
for i in range(1,n+1):
    sum +=i
print("Total sum is ", sum)

# using while loop

num=int(input("Enter a number 'n' : "))
total = 0
i=1
while i <= num : 
    total += i 
    i+=1

print("Total sum is ", total)

#WAP to find the factorial of the number

fact_num= int(input("Enter number to find factorial: "))

fact=1
i=1

#while loop 

while i<=fact_num:
    fact*=i
    i+=1
print("The factorial of", fact_num ,"is ",fact)

#for loop 

for i in range (1,fact_num+1):
    fact*=i
print("The factorial of", fact_num ,"is ",fact)