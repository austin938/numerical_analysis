import numpy as np


def rk2(yin: list, t: float, h: float, func: callable) -> np.ndarray:
    
    # compute k1
    k1 = func(yin, t)    
    # compute k2
    k2 = func(yin+h*k1, t+h)
    # compute ynext
    ynext = yin + 0.5*h*(k1+k2)
    return ynext