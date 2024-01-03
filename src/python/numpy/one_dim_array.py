# Creating a one dimensional array

import numpy as np

one_dim_array = np.array([1,2,3,4,5,6])
print("one dimensional array is",one_dim_array)

# for getting the dimension of array

print("Dimension of array is ",one_dim_array.ndim)

# type of array

print("Type of array is ",type(one_dim_array))

#shape of array

print("shape of array iss",one_dim_array.shape) #no of elements

#change 1d array to 2d using reshape()

arr2 = one_dim_array.reshape(2,3)

print("2d reshaped array is ",arr2)

print("dimension of rehsaped array is  ",arr2.ndim)


#change 1d array to 3d using reshape()

one_dim_array = np.array([1,2,3,4,5,6,7,8])

arr3 = one_dim_array.reshape(2,2,2)

print("3d reshaped array is ",arr3)

print(" dimension of rehsaped array is \n ",arr3.ndim)

#converting this 3dimensional array to 1D

arr1 = arr3.reshape(-1)

print("converted 1d array isss \n",arr1)


