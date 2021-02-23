#hello.py
#The webpage does not work so I improvised something
from    mpi4py  import  MPI 
import numpy
import sys

comm    =   MPI.COMM_WORLD  
rank    =   comm.Get_rank()

#size = comm.Get_size()
#initializing variables. mpi4py requires that we pass numpy objects.
integral = numpy.zeros(1)
total = numpy.zeros(1)
#Number in the rank
numn = numpy.ones(1)*int(rank)
integral[0] = numpy.sum(numn)

# communication
# root node receives results with a collective "reduce"
comm.Reduce(integral, total, op=MPI.SUM, root=0)
# root process prints results
if comm.rank == 0:
    print("Sum is : "+str(total))
