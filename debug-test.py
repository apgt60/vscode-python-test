import numpy as np
import pandas as pd

print("-------------------")

list_mul = ['2','2','2']
list_mul*2
# print("answer:", list_mul*2)

def function(var1=2, var2=4):
    var2 = 6
    var1 = 5
    # print(var1, var2)

function(10, 20)


sports = ['Cricket', 'Football', 'Tennis', 'Golf', 'Baseball']
sports_new = np.array(sports)
# print(sports_new)

mat = np.array([[1,2,1],[4,5,9],[1,8,9]])
# print(mat)

# adding a step size of 5 to create an array
arr3  = np.arange(10, 20, 3)
# print(arr3)

vec = np.linspace(10,20,3)
#print(vec)

vec1 = np.arange(0, 12)
vec2 = vec1.reshape(4, 3)
#print(vec2)

vec = np.arange(0,5) 
# print(vec.reshape((2,3)))

vec1 = [10,15,20]
vec2 = [15,25,35]
# print(vec1+vec2)

vec1 = np.linspace(20,50,4)
# print("vec1:", vec1)
vec2 = np.linspace(100,120,3)
# print("vec2:", vec2)
# print(vec1 + vec2)

vec = np.arange(2,5,1)
# print("vec:", vec)
# print(1/vec)
# print(vec**2)

mat1 = np.arange(1,5).reshape(2,2)
# print("mat1:", mat1)
mat2 = np.eye(2)
# print("mat2:", mat2)
# print(mat1/mat2)

r1 = np.random.rand(5)
# print("r1:", r1)
r2 = np.random.randint(5) #gives random value between 0 and 5
# print("r2:", r2)

mat1 = np.arange(-9,0,1).reshape(3,3)
# print("mat1:", mat1)
# print("min:", np.min(mat1))
# print("max:", np.max(mat1))

rand = np.random.rand()


rand = np.random.randn()
#print("rand:", rand)

arrange = np.arange(8)
#print("arrange:", arrange)

np_array = np.arange(6)
# print("np_array:", np_array)
np_array_mod = np_array[np_array==5]
# print("np_array_mod:", np_array_mod)
np_array_mod2 = np_array[np_array>3]=99
# print("np_array_mod2", np_array_mod2)

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix[1][1])

vec = np.array([4,7,8,9,10,6,1])
# print(vec[vec>6])

vec1 = np.array([4, 7, 8, 9, 10, 6, 1])
vec1[vec1>6] = 2
# print(vec1)

matrix = np.arange(1,10).reshape(3,3)
matrix[0:2,1:2] = 0
# print(matrix)

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array2 = array1.copy()
array2[array2>5] = 0
print("array1",array1)
print("array2",array2)
