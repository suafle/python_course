# Program to multiply two matrices using nested loops
import numpy as np

N = 250

X = np.random.randint(0,100,size=(N,N))
Y = np.random.randint(0,100,size=(N,N+1))

result = np.matmul(X,Y)

print(result)
