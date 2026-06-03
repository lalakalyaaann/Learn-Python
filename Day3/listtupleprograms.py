#WAP that asks the user to enter names of their 3 favourite movies and store them in a list. 
input1=input("Enter your first favourite movie :")
input2=input("Enter your second favourite movie :")
input3=input("Enter your third favourite movie :")

fav_movie=[]
fav_movie.append(input1)
fav_movie.append(input2)
fav_movie.append(input3)
print(fav_movie)


#WAP to check if a list contains a palindrome of elements. 

list1=[1,2,3,4,3,2,1]
list2=[1,4,2,4,6,6,3]
copylist1=list1.copy()
copylist2=list2.copy()
copylist1.reverse()
copylist2.reverse()

if(list1 == copylist1):
    print("Elements in list are in palindrome")
else:
    print("Elements in list are not palindrome")

if(list2 == copylist2):
    print("Elements in list are in palindrome")
else:
    print("Elements in list are not palindrome")


#WAP to count the numbers of students with grade "A" in the given tuple
result=("C","D","A","A","B","B","A")

print(result.count("A"))

#WAP that sorts the list of the above values and sorts them from A to D

resultlist=["C","D","A","A","B","B","A"]
resultlist.sort()
print(resultlist)