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
        if sim.method == "upwind":
            sim.u[i] = uold[i] - sim.c * sim.dt *(uold[i] - uold[i-1]) / sim.dx # TODO: implement the upwind method
        elif sim.method == "FTCS":
            sim.u[i] =  uold[i] - sim.c * sim.dt *(uold[i+1] - uold[i-1]) / (2* sim.dx) # TODO: implement the FTCS method
        else:
            raise SystemExit("Error: method "+sim.method+" is not supported!")


