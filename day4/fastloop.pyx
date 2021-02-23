import numpy as np
from math import exp

# Naive python implementation of a Radial Basis Function (RBF) approximation scheme
# According to the profiler, the for loops and the assignation of the Y is the most time consuming part of applying this function rather than scipy
def rbf_network_cython(X, beta, theta):
    cdef int N = X.shape[0]
    cdef int D = X.shape[1]
    cdef int i,j,d
    cdef float r
    cdef double[:] Y = np.zeros(N)
    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
                r = r**0.5
                Y[i] += beta[j] * exp(-(r * theta)**2)
    return Y
