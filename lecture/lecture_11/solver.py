import numpy as np
def euler(yin, star1, star2, time, dt, func):
    # call func to obtain the values of dydt
    fun = func(yin, star1, star2, time)
    # compute ynext using the Euler's method
    # y_{n+1} = y_n + h*f(y_n, t_n)
    # dy/dt = f(y,t)
    ynext = yin + (dt*fun)
    return ynext

def rk2(yin, star1, star2, time, dt, func):
    # compute k1
    k1 = func(yin, star1, star2, time)    
    # compute k2
    k2 = func(yin+dt*k1, star1, star2, time+dt)
    # compute ynext
    ynext = yin + 0.5*dt*(k1+k2)
    return ynext

def rk4(yin, star1, star2, time, dt, func):
    # compute k1
    k1 = func(yin, star1, star2, time)
    # compute k2
    k2 = func(yin+k1*dt*0.5, star1, star2, time+0.5*dt)
    # compute k3
    k3 = func(yin+k2*dt*0.5, star1, star2, time+dt*0.5)
    # compute k4
    k4 = func(yin+dt*k3, star1, star2, time+dt)
    # compute ynext
    ynext = yin + dt/6 * (k1 + 2*k2 + 2*k3 + k4)    
    return ynext