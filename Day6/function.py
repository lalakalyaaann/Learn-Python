def sum (a,b) :
    sum=a+b
    print("The total is ",sum)
    return sum

print(sum(4,5))

def hello_world():
    print("Hello World")

hello_world()
hello_world()
hello_world()

output= hello_world()
print(output)
#function that donot return anything stores none

#calculate average of 3 numbers

def average(a,b,c):
    sum=a+b+c
    avg=sum/3
    print("The average of 3 numbers is : ",avg)

average(6,5,4)

#built in function 

#print function

print("Hello Guys!")
print("Kalyan ","is","here")

#len function
#range function 
#type function

#userdefined function

def cal_prod(a,b):
    return a*b

print(cal_prod(3,4))


#Write a function to print the length of a list

cities=['Pokhara','Kathmandu','Chitwan','Butwal','Lalitpur']

def print_len(list):
    print(len(list))

print(print_len(cities))

#Write a function  to print the elements of the list in a single line.

num=[1,2,3,4,5]

def print_list(list):
    for item in list:
        print(item,end=" ")

print(print_list(num))


#Write a function to find the factorial of a number. 

def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

calc_fact(5)

# #Write a function to convert USD into NPR

def converter(usd_value):
    npr_value=usd_value*140
    print(usd_value, "USD =",npr_value,"NPR")

converter(5)
converter(2)

#check odd or even function
def oddeven(n):
    if(n%2 == 0):
        print("EVEN")
    else:
        print("ODD")
oddeven(5)
oddeven(12)