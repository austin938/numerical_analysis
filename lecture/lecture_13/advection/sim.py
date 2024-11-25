import numpy as np

c      = 1  # velocity
xmin   = 0.0  # coordinate of left boundary
xmax   = 1.0  # coordinate of right boundary
tend   = 0.7  # final time
# method = "upwind" 
method = "average"

nmax   = 500  # number of points in the x direction
nbuf   = 1    # number of ghost zones for B.C.
ntot   = nmax + 2*nbuf # total number of points including two ghost zones
istart = 1    # index of first point
iend   = nmax # index of last point

cfl    = 0.4  # CFL number
dx     = (xmax-xmin)/nmax 

dt     = cfl * dx / c # TODO: compute the simulation timestep using the CFL criterion

u = np.zeros(ntot) # array for storing the solution u(x), including the ghost zones
x = np.zeros(ntot) # array for storing the x coordinates of data points, including ghost zones

outdir = "data_"+method # name of output directory
io_interval = 10 # parameter for output frequency 