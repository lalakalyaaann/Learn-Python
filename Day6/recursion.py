#prints from given number n to 1 backwards

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1) #show is called inside show. This is recursive function
# show(10)

#recursive function to return the factorial

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(5))

#Write a recursive function to calculate the sum of n natural numbers

# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1)+n
# sum=calc_sum(10)
# print(sum)

#Write a recursive function to print all the elements in a list
 
def print_list(list,index=0):
    if(index== len(list)):
       return
    print(list[index])
    print_list(list, index+1)

list=[1,2,3,4,5,6,7]

print_list(list)