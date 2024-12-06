from . import sim
import numpy as np
import os


def output(step, time):
    
    fstr = f"{step:05d}"
    
    filename = sim.outdir+f'/advection_{sim.method}_'+fstr+'.csv'


    if not os.path.isdir(sim.outdir):
        os.mkdir(sim.outdir)
    
    f = open(filename, "w")
    f.write(f"i,x,u(x),ua(x),diff,(t = {time:e})\n")
    
    # find out the analytical solution
    pc = 0.15 + sim.c * time # center of the top hat
    pl = pc - 0.05 # left side of top hat
    pr = pc + 0.05 # right side of top hat
    
    for i in range(sim.istart, sim.iend+1):
        
        # compute analytical solution
        # if sim.x[i] >= pl and sim.x[i] <= pr:
        #     ua = 1.0
        # else:
        #     ua = 0.01

        ua = max(np.exp(-1000 * (sim.x[i] - (0.1 + sim.c * time))**2), sim.epsilon)
        
        f.write(f"{i:d},{sim.x[i]:e},{sim.u[i]:e},{ua:e},{np.abs(sim.u[i]-ua)}\n")
        
    f.close()

