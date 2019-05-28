import random

NB_POINTS = 10**5
LENGTH = 10**2

CENTER = [LENGTH/2,LENGTH/2]

def in_circle(p):
    x,y = p
    center_x,center_y= CENTER
    r = LENGTH/2
    return (x-center_x)**2 + (y-center_y)**2 < r**2

def compute_pi(n):
    inside = sum(1 for _ in range(n) if in_circle((random.randint(1,LENGTH),random.randint(1,LENGTH))))
    return (inside/n)*4

if __name__=="__main__":
    print(compute_pi(NB_POINTS))
