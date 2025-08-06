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

