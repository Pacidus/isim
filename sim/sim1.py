# imports
import numpy as np
from isingm.metropolis import algorithm

def sim():
    """
    None -> dict(numpy array or float)

    We study the impact the size of the lattice as on the ising model,
    in the simpliest case (with the default parameters).
    
    Return:
        dictionnary of the data
    """
    # What where gonna change 
    lengths = [8*(2**i)for i in range(0,8)]
    dims = [1, 2, 3]
    mintemp = 0.01
    maxtemp = 300
    Ndata = 1000
    temperature = np.linspace(mintemp, maxtemp, Ndata)
    
    pflip = 0.1
    
    data = {"Kb" : 0., "B" : 0., "Temp" : temperature}
    for dim in dims:
        for length in lengths:
            shape = (length,)*dim
            metropolis = algorithm(shape, all = 1)
            
            M = []
            H = []
            
            size = metropolis.het
            n = pflip
            itt = range(1 + int(1/pflip))

            for t in temperature:

