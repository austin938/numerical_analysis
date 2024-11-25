from . import sim

def set_boundary():
    
    # assuming periodic B.C. for the advection problem
    
    # TODO: apply left B.C.
    sim.u[0]  = sim.u[-2]
    # TODO: apply right B.C.    
    sim.u[-1] = sim.u[1]
    