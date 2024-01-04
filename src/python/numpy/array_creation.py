''' Array Creation Methods ..........'''

import numpy as np

# 1. np.array()  : create an array using list or tuple

arr1 = np.array([1,2,3,4])

print("array is ", arr1)

#2. np.zeros() : create an array full of zeros

arr1 = np.zeros(5) # 1D

arr2 = np.zeros((2,2)) #2D

arr3 = np.zeros((3,3,2)) #3D

print("zero matrices are ",arr1)

print("2d zero matrices are ",arr2)

print("3d zero matrices are ",arr3)

#3. np.ones() : create an array full of ones

arr1 = np.ones(5) # 1D

arr2 = np.ones((2,2)) #2D

arr3 = np.ones((3,3,2)) #3D

print("ones matrices are ",arr1)

print("2d ones matrices are ",arr2)

print("3d ones matrices are ",arr3)

#4. np.arrange() : create an array with regularly incrementing values

arr1 = np.arange(10)

arr2 = np.arange(1,10)

arr3 = np.arange(0,10,2)

print("first arange method : ",arr1)

print("second arange method : ",arr2)

print("third arange method : ",arr3)

#5. np.linspace() : create an array with equally spaced numbers

arr1 = np.linspace(1,10)

print("linspaced array iss", arr1)

#6. np.eye() : create an array where main diagonals are 0 and 1

arr1 = np.eye(4)

print("eye method array is\n",arr1)

#7. np.full() : create an array filled with specific value

arr1 = np.full((3,2,2),1)

print("full method array is\n",arr1)

#8. np.random.randint : create an array with random numbers

arr1 = np.random.randint(1,5,(3,2,2))

print("random list is \n",arr1)

#9. np.random.random : create an array with random float values

arr1 = np.random.random(5)

print("random floar values are\n",arr1)