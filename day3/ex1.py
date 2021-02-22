import numpy as np

#Ex a
null = np.zeros(10)
null[4] = 1

print('\n')
print('Output exercise 1a')
print(null)
print('\n')

#Ex b
vector = np.arange(10,50)

print('Output exercise 1b')
print(vector)
print('\n')

#Ex c
#Priting null and vector reverted
print('Output exercise 1c')
print(null[::-1])
print(vector[::-1])
print('\n')

#Ex d
mat = np.arange(0,9).reshape(3,3)
print('Output exercise 1d')
print(mat)
print('\n')

#Ex e
array = np.array([1,2,0,0,4,0])
#loc = array!=0 #this gives an array of booleans
loc = np.where(array!=0)
print('Output exercise 1e')
print(loc[0])
print('\n')

#Ex f
rand = np.random.random(30)
mean = np.mean(rand)
print('Output exercise 1f')
print(rand)
print('Mean = ',mean)
print('\n')

#Ex g
weird_mat = np.zeros((5,5))
weird_mat[0,:] = 1
weird_mat[-1,:] = 1
weird_mat[:,0] = 1
weird_mat[:,-1] = 1
print('Output exercise 1g')
print(weird_mat)
print('\n')

#Ex h
checkboard = np.zeros((8,8))
for i in range(len(checkboard)):
    if i%2==0:
        checkboard[i][::2] = 1
    else:
        checkboard[i][1::2] = 1
print('Output exercise 1h')
print(checkboard)
print('\n')

#Ex i
a = np.array([[1,0],[0,1]])
tile = np.tile(a,(4,4))
print('Output exercise 1i')
print(tile)
print('\n')

#Ex j
Z = np.arange(11)
Z[3:9] = -1*Z[3:9]
print('Output exercise 1j')
print(Z)
print('\n')

#Ex k
Z = np.random.random(10)
Z = np.sort(Z)
print('Output exercise 1k')
print(Z)
print('\n')

#Ex l
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A,B)
print('Output exercise 1l')
print(equal)
print('\n')

#Ex m
Z = np.arange(10, dtype=np.int32)
print('Output exercise 1m')
print(Z.dtype)
Z = np.float32(Z)
print(Z.dtype)
print('\n')

#Ex n
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print('Output exercise 1n')
print(D)
print('\n')
