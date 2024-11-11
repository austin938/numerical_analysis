import numpy as np
from physics import initialize, update
path = f"lecture/lecture_11/data//" 

msun = 2.0e33 
G = 6.67428e-8
au = 1.49598e13 #cm
year = 365.25*86400.0 #s


m1 = 1.0*msun
m2 = 2.0*msun
separation = 3.0 * au 


step  = 0
dt    = 0.0001*year
time  = 0.0
tmax  = 10.0*year
noutput = 500 # number of snapshots
ninterval = tmax/dt/noutput # interval between file outputs


# set initial conditions of the two stars
star1, star2 = initialize(m1, m2, separation)


# open two files for the output data
with open(path+'binary_001.csv','w') as f1:
    with open(path+'binary_002.csv','w') as f2:
        f1.write('time,mass,x,y,vx,vy,ax,ay \n')
        f2.write('time,mass,x,y,vx,vy,ax,ay \n')
        
        while time <= tmax:


            update(dt, star1, star2)
            time += dt
    
            if step % ninterval == 0:
                f1.write(f"{time:e},{star1.mass:e},{star1.x:e},{star1.y:e},{star1.vx:e},{star1.vy:e},{star1.ax:e},{star1.ay:e}\n")   
                f2.write(f"{time:e},{star2.mass:e},{star2.x:e},{star2.y:e},{star2.vx:e},{star2.vy:e},{star2.ax:e},{star2.ay:e}\n")        
    
            step += 1


f1.close()
f2.close()


print("Done")
