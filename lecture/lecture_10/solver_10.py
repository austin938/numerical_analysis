import numpy as np


def euler(yin: list, t: float, h: float, func: callable) -> np.ndarray:
    
    # call func to obtain the values of dydt
    fun = func(yin, t)
    # compute ynext using the Euler's method
    # y_{n+1} = y_n + h*f(y_n, t_n)
    # dy/dt = f(y,t)
    ynext = yin + (h*fun)
    return ynext


def rk2(yin: list, t: float, h: float, func: callable) -> np.ndarray:
    
    # compute k1
    k1 = func(yin, t)    
    # compute k2
    k2 = func(yin+h*k1, t+h)
    # compute ynext
    ynext = yin + 0.5*h*(k1+k2)
    return ynext


def rk4(yin: list, t: float, h: float, func: callable) -> np.ndarray:
    
    # compute k1
    k1 = func(yin, t)
    # compute k2
    k2 = func(yin+k1*h*0.5, t+0.5*h)
    # compute k3
    k3 = func(yin+k2*h*0.5, t+h*0.5)
    # compute k4
    k4 = func(yin+h*k3, t+h)
    # compute ynext
    ynext = yin + h/6 * (k1 + 2*k2 + 2*k3 + k4)    
    return ynext


