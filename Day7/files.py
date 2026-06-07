#read mode

f=open("textfile.txt","r")
data= f.read()
print(data)
print(type(data))
f.close()

# #read line
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)

#write to a file

f=open("textfile.txt","w")

f.write("Hi, This is write mode. I am learning file handling ")
f.close()

#append mode 

f=open("textfile.txt","a")
f.write("today is day7. Lets learn!")
f.close()

#with syntax

with open("textfile.txt","r") as f:
    data= f.read()
    print(data)


#delete a file 

import os
os.remove("filedel.txt")