import numpy as np
from . import sim
from .boundary import set_boundary
from .IO import output 

def evolve():
    
    step = 0
    time = 0.0

    while time <= sim.tend:
    
        # reset boundary
        set_boundary()

        # record data to file
        if step % sim.io_interval == 0:
            print(f"step = {step:d}, time = {time:e}")
            output(step, time)
    
        # update solution    
        update()
    
        step += 1
        time += sim.dt

def update():
        
    # TODO: copy sim.u to a new array called uold
    uold = sim.u.copy()

    # update all inner points based on the selected method
    for i in range(sim.istart, sim.iend+1):
        
        FL, FR = flux(i, uold)

        sim.u[i] = uold[i] - sim.dt * (FR - FL) / sim.dx


def flux(i, uold):

    if sim.method == 'upwind':
        FL = sim.c * uold[i-1]
        FR = sim.c * uold[i]
    elif sim.method == 'LF':
        FL = sim.c * (uold[i-1] + uold[i]) / 2 - sim.dx * (uold[i] - uold[i-1]) / (2 * sim.dt)
        FR = sim.c * (uold[i] + uold[i+1]) / 2 - sim.dx * (uold[i+1] - uold[i]) / (2 * sim.dt)
    # elif sim.method == 'LW':
    #     FL = 
    #     FR = 
    elif sim.method == 'average':
        FL = sim.c * (uold[i-1] + uold[i]) / 2
        FR = sim.c * (uold[i] + uold[i+1]) / 2
    else:
        raise SyntaxError(f"Error: method {sim.method} is not supported")
    
    return FL, FR