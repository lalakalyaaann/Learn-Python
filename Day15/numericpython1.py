import numpy as np
#Mathematical operations on array

a = np.array([20,40,50,-60])
print(a)

print(a+100) 
print(a-20) 
print(a*3) 
print(a/10) 

b = np.array([1,4,9])
print(b)    
print(np.square(b)) # square of all array elements
print(np.sqrt(b))   # square root of all array elements

print(np.sin(b))
print(np.cosh(b))
print(np.tan(b))

#Mathematical operations on multiple array
a=np.array([1,2,3])
b=np.array([4,5,6])

print(np.add(a,b))          
print(np.subtract(a,b))    
print(np.multiply(a,b))    
print(np.divide(a,b))       

# Dot product: computes the inner product of the two vectors and sum the results
print(np.dot(a,b)) # dot product
print(a.T) # Transpose : Returns an array with axes transposed

#Transpose 
t = np.array([[1,2,3],
              [4,5,6]])

print("Initial \n: ",t)    # initial shape: 2,3
print("Final Transposed : \n",t.T)  # shape after transpose: 3,2



#statistical functions 

a = np.array([[1,2,3], [4,5,6]])
print(a)
print(np.sum(a))
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.min(a))
print(np.max(a))

#Array Comparision 
a = np.array([1,5,3])
b = np.array([4,5,6])
print(a)
print(b)
print(a == b) # comparing each elements of an array
print(np.array_equal(a,b)) # comparing complete array


#Broadcasting 
a = np.array([1,2,3,4])
b = np.array([5])
print(a+b)

c = np.array([[1,2,3], [4,5,6]])
d = np.array([10,20,30])
print(c+d) 
