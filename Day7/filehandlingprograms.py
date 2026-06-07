# #WAP to create a new file in python practice.txt and add 
# """
# Hi everyone 
# We are learning File I/O
# using Java. 
# I like programming in Java 
# """

# with open("practice.txt","w") as f:

#     f.write("Hi everyone \n We are learning File I/O\n")
#     f.write("using Java \n I like programming in Java.")

# #replace the java with python

# with open("practice.txt","r") as f:
#     data=f.read()
# new_data=data.replace("Java","Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)


#search if word learning exists or not
word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("Not found")
  