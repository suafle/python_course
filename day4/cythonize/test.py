import c_primes
import primes
import time

t0 = time.time()
print(c_primes.primes(5))
print("Cython: ", time.time() - t0)

t0 = time.time()
print(primes.primes(5))
print("Python: ", time.time() - t0)
