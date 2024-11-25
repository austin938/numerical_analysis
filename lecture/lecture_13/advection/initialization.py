import numpy as np
from . import sim

def initialize():
    
    # initialize the x array
    sim.x = [sim.xmin+(i-0.5)*sim.dx for i in range(sim.ntot+1)]

    # initialize the u array
    for i in range(sim.istart, sim.iend+1):
    
        # top hat function 
        if sim.x[i] >= 0.1 and sim.x[i] <= 0.2:
            sim.u[i] = 1.0
        else:
            sim.u[i] = 0.01