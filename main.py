import  numpy as np

"""
=> floats atleast requires 32 bits
=> ints atleast requires 8 bits
"""

a = np.array([1,2,3],dtype = "int8")

print(a)

b = np.array([[9.2,0.3,8.1,0.3,7.4,0.1],[6.4,0.66,5.12,0.3,4.4,0.0]],"float32")

print(b)

# get dimentions

print(b.ndim) 

# shape
# how much rows and columns an array has
print(b.shape)

# get type:

print(a.dtype)

# get size
print(a.itemsize);  

# get total size

# print(a.size*a.itemsize) # or

print(a.nbytes)
print(b.nbytes)

# access multi-dimentional array

print(b[1,-4]) # to get 5.12 or print(b[1,2])

 
# get specific row or col
# row
print(b[0,:])
# col
print(b[:,0])

print(b[0,::-1])
print(b[0,1:-1])

b[1,:] = [1,2]

print(b)


