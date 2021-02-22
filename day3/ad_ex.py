import numpy as np

mat = np.array([[1.0, 2.0, 10],[3.0, 4.0, 20],[5.0, 6.0, 30],[7.0, 8.0, 40]])
print(mat)

#Ex a
z = mat[:,-1]
print('Ex a')
print(mat/z[:,np.newaxis])
print('\n')

#Ex b
mat = np.array([[1,0,0],[0,1,0],[0,0,1]])
diag = [mat[i][i] for i in range(len(mat))]
print('Ex b')
print(diag)
print('\n')

#Ex c
ran = np.random.random((10,3))
index = []
for i in range(len(ran[0,:])):
    index.append(np.argmin(np.abs(ran[:,i]-0.75)))
print('Ex c')
print('Indices:',index)
#print(ran[:,0])
#print(np.abs(ran[:,0]-0.75))
#print(np.argmin(np.abs(ran[:,0]-0.75)))
#print(index)
#print(ran[:,0][index[0]])
print('Value closest to 0.75 first column',ran[:,0][index[0]])#,ran[index[1]],ran[index[2]])
print('Value closest to 0.75 secon column',ran[:,1][index[1]])#,ran[index[1]],ran[index[2]])
print('Value closest to 0.75 third column',ran[:,2][index[2]])#,ran[index[1]],ran[index[2]])
print('\n')

#Ex d
x = np.empty((10, 8, 6))

idx0 = np.zeros((3, 8)).astype(int) 
idx1 = np.zeros((3, 1)).astype(int)
idx2 = np.zeros((1, 1)).astype(int)

print('Ex d')
print(x[idx0, idx1, idx2])
print('The final array is 3x8 since idx0 is the first use')
print('\n')

#Ex e

