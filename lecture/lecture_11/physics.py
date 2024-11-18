import numpy as np
from solver import euler, rk2, rk4

msun = 2.0e33 
G = 6.67428e-8
au = 1.49598e13
year = 365.25*86400.0


def initialize(m1, m2, separation):


    # compute period    
    period = (4*np.pi**2*separation**3/(G*(m1+m2)))**0.5


    # compute force between m1 and m2   
    force = G*m1*m2/separation**2


    # compute x, y, vx, vy, ax, ay of the two stars
    x1  = -separation*(m2/(m1+m2))
    y1  = 0.0
    vx1 = 0.0
    vy1 = -2*np.pi*x1/period # v=2*pi*r/T
    ax1 = force/m1
    ay1 = 0.0
    x2  = separation*(m1/(m1+m2))
    y2  = 0.0
    vx2 = 0.0
    vy2 = -2*np.pi*x2/period
    ax2 = -force/m2
    ay2 = 0.0
    
    # initialize two Star objects
    star1 = Star(1, m1, x1, y1, vx1, vy1, ax1, ay1)
    star2 = Star(2, m2, x2, y2, vx2, vy2, ax2, ay2)


    return star1, star2
    
def update(time, dt, star1, star2, method):
    yin = [star1.x, star1.y, star1.vx, star1.vy, star2.x, star2.y, star2.vx, star2.vy]

    
    if method == 'euler':
        yout = euler(yin, star1, star2, time, dt, func)
    elif method == 'rk2':
        yout = rk2(yin, star1, star2, time, dt, func)
    elif method == 'rk4':
        yout = rk4(yin, star1, star2, time, dt, func)
    else:
        raise SystemExit("Error: method "+method+" is not supported!")

    star1.x = yout[0]
    star1.y = yout[1]
    star1.vx = yout[2]
    star1.vy = yout[3]
    star2.x = yout[4]
    star2.y = yout[5]
    star2.vx = yout[6]
    star2.vy = yout[7]


def func(yin, star1, star2, time):
    # From the updated coordinates, compute the new force between star1 and star2
    # Then calculate the x- and y- components of the force 
 
    force = G*star1.mass*star2.mass/((star2.x-star1.x)**2+(star2.y-star1.y)**2)
    angle = np.arctan2(star2.y-star1.y, star2.x-star1.x)
    fx = force * np.cos(angle)
    fy = force * np.sin(angle)
    
    # Update ax and ay of the two stars
    star1.ax = fx/star1.mass
    star1.ay = fy/star1.mass
    star2.ax = -fx/star2.mass
    star2.ay = -fy/star2.mass


    N = np.size(yin)
    k = np.zeros(N)
    k[0] = yin[2] # vx1
    k[1] = yin[3] # vy1
    k[2] = star1.ax
    k[3] = star1.ay
    k[4] = yin[6] # vx2
    k[5] = yin[7] # vy2
    k[6] = star2.ax
    k[7] = star2.ay
    return k


class Star:


    # define properties in a Star class
    id: int
    mass: float
    x: float
    y: float
    vx: float
    vy: float
    ax: float
    ay: float
    
    # function used for initializing the Star class
    def __init__(self, id: int, mass: float, x: float, y: float, 
                 vx: float, vy: float, ax: float, ay: float) -> None:
        self.id = id
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
    
