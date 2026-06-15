import numpy as np
print(np.__version__)
# Creating array using list
#one dimensional array

list1 = [1, 2, 3]
arr_list1 = np.array(list1) 
print(arr_list1)
print(type(arr_list1))  #check the type of array
print(arr_list1.ndim)   # check dimension of array

#two dimensional array

list1 = [1,2,3]
list2 = [4,5,6]
arr_list1_2 = np.array([list1, list2])
print(arr_list1_2)
print(arr_list1_2.ndim) 

#three dimensional array

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
arr_list1_3 = np.array([[list1, list2, list3]])
print(arr_list1_3)
print(arr_list1_3.ndim) 

# Attributes of Array (properties of array)
#1d array
arr0=np.array([10,20,30])
print(arr0)
print("shape of array : ", arr0.shape) 
print("data type of array :", arr0.dtype)  
print("dimension of array :", arr0.ndim)   

#2d array
arr1 = np.array([[1,2,3], [4,5,6]])
print(arr1)
print("shape of array : ", arr1.shape) 
print("data type of array :", arr1.dtype)  
print("dimension of array :", arr1.ndim)   

#3d array
L1 = [1,2,3]
L2 = [4,5,6]
L3 = [7,8,9]
arr2 = np.array([[L1, L2, L3]])
print(arr2)
print("shape of array : ", arr2.shape) 
print("data type of array :", arr2.dtype)  
print("dimension of array :", arr2.ndim) 



# Array initialization methods 

# zeros array : all elements are 0
zero_arr = np.zeros((2,3))
print(zero_arr)
# ones array : all elements are 1
one_arr = np.ones((1,5))
print(one_arr)
# Full array : all elements are same based on given valuedimension and value.
full_arr = np.full((3,2), 3)
print(full_arr)
# Identity Matrix 
id_arr = np.eye(3)
print(id_arr)
# empty array
print(np.empty(2))
# evenly spaced array : elements are evenly spaced based on step value
print(np.arange(2,10,2))
# specific number of eqaully spaced values between a range : elements are equally spaced based on step value
print(np.linspace(1,10,4))
# random values array - float
r_arr = np.random.rand(3,2)
print(r_arr)
# random values array - int
rint_arr = np.random.randint(1,100,(3,3))
print(rint_arr)


#Array indexing and slicing 
a = np.array([1,2,3,4,5,6,7])
print(a)
print(a[0])     # first element of array
print(a[4])     # fifth element of array
print(a[-1])      # last element of array

 # Slicing :
# array[start:stop:step]
# stop - index, that is not included in output
print(a[0:3]) # First 3 elements
print(a[-3:]) # Last 3 elements
print(a[1:4]) # Middle 3 elements
print(a[0::3]) # Middle 3 elements with steps

# Indexing on 2 Dimensional Array
arr2 = np.array([[10,20,30], [40,50,60]])
print(arr2)
print(arr2[0]) # first row
print(arr2[1]) # second row

 # Slicing on 2D array
print(arr2[0][0]) # element of first row and first column
print(arr2[0][1]) # element of first row and second column
print(arr2[1][2]) # element of second row and third column
print(arr2[1]) # specific element - 1D
print(arr2[1:]) # slicing part - 2D
print(arr2)

#3d array indexing and slicing 

arr3 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(arr3) 

print(arr3[0])
print(arr3[1])
print(arr3[2])
print(arr3[0][2])
print(arr3[2][2])
print(arr3[:, 0]) # 1st col value
print(arr3[:, 1]) # 2nd col value
print(arr3[:, 2]) # 3rd col value
print(arr3[::, 1:2])  #slicing on columns
print(arr3[2::, 0:2]) #slicing on rows and columns



#Array reshaping and flattening 
# Reshape Array: changing its dimensions (e.g., rows and columns) without altering the actual data
# Flatten Array: transforming a multi-dimensional array into a single-dimensional array

arr1 = np.array([1,2,3,4,5,6])      
print(arr1)
reshaped = arr1.reshape((6,1))      # changed the array of shape (1,6) to (6,1)
print(reshaped)
reshaped2 = arr1.reshape((2,3))     #changed array from  size (1,6) to (2,3)
print(reshaped2)

# #flatten
print(reshaped2.flatten())  



#Array Stack and splitting 
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.vstack((a,b))) 
print(np.hstack((a,b)))

c = np.array([[1,2,3], [4,5,6]])
print(c)

hsplit = np.hsplit(c,3) # horizontal split splits by column
for s in hsplit:    
    print(s)

vsplit = np.vsplit(c,2) # vertical split splits by row
for s in vsplit:
    print(s)

