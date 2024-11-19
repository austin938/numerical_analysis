from . import sim


def set_boundary():
    
    # assuming periodic B.C. for the advection problem
    
    # TODO: apply left B.C.
    sim.x[-1] = sim.x[sim.nmax]
    
    # TODO: apply right B.C.   
    sim.x[sim.nmax + 1] = sim.x[1]