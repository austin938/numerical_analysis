import numpy as np
from physics import update
from scipy.constants import g
import matplotlib.pyplot as plt
import pandas as pd
path = r"/home/austin/Documents/computer/numerical/lecture/lecture_10/data//" # Ubuntu path

'''
This file mainly write the output data (obtained by different method) into a csv file
'''

print("g = ", g) # m/s^2


angle = 60.0  # degree
angle = angle * np.pi / 180 # degree to rad


velocity = 30 # m/s


velx = velocity * np.cos(angle)
vely = velocity * np.sin(angle)


dt = 0.5 # timestep to advance the solution in sec
time = 0.0 # initial time


posx = 0.0
posy = 0.0


anal_y = 0.0 # analytical solution
vy0    = vely # for computing the analytical solution
err_y  = 0.0


method = 'euler' # select solver ('euler', 'rk2', or 'rk4')


f = open(path+method+'_t=0.5_.csv', 'w')
# csv file don't need space between the comma
f.write('time,posx,posy,velx,vely,anal_y,err_y \n')
f.write(f"{time:e},{posx:e},{posy:e},{velx:e},{vely:e},{anal_y:e},{err_y:e}\n")


while (posy >= 0.0):
    posx, posy, velx, vely = update(time, dt, posx, posy, velx, vely, method)
    time += dt
    anal_y = vy0*time - 0.5*g*time**2
    err_y = abs((posy-anal_y)/anal_y)
    f.write(f"{time:e},{posx:e},{posy:e},{velx:e},{vely:e},{anal_y:e},{err_y:e}\n")


f.close()


print("Done")
