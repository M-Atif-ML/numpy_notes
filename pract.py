import numpy as np
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(b)

# get specific element (work outside in)

for i in b:
	for j in i:
		for k in j:
			print(k)

b[0,:,:] = [9,9]

print(b)

# intialization of Different types of array

# all 0s matrix

print(np.zeros((2,3,10),dtype = "int8"))
print("\n")

# all 1s matrix
print(np.ones((2,3,10),dtype = "int8"))
print("\n")

# all full with a certain value 
print(np.full(b.shape,99))
print("\n")

# we can also use full_like to fully initialize an array with shape like anyother array
print(np.full_like(b,-20))

print(np.random.rand(4,5))

print(np.random.randint(4,10,size = (3,3)))

# Repeat 

arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis = 0)
print(r1)



# exersize

new_arr = np.ones((5,5))
new_arr[1:-1,1:-1] = 0
new_arr[2,2] = 9
print(new_arr)

# copying array

a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(a)


# mathematics

# simple arithimatics
a = np.array([1,2,3,4])
# a /= 2
print(a)

# trig functions
print(np.sin(a))
print(np.cos(a))

# linear algerbra 
mat1 = np.ones((2,3))
mat2 = np.full((3,2),2)

print(np.matmul(mat1,mat2))

# find determinant
mat3 = np.identity(3)
print(mat3)
print(np.linalg.det(mat3))




