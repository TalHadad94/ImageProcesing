import numpy as np
import math

def  image_rotation( sim, a, x, y ):
	rim  = np.zeros_like(sim)
	w = sim.shape[0]
	h = sim.shape[1]
	for i in range(w):
		y = i +0.5
		for j in range(h):
			x = j + 0.5
			u, v = T_inverse(x,y)
			u = int(u)
			v = int(v)
			
			if(u < 0 or u >= sim.shape[0]):
				continue
			if(v<0 or v >= sim.shape[1]):
				continue
			rim[i][j] = sim[v][u]

	return( rim )


a = 20
u0 = 40
v0 = 100
x0 = 40
y0 = 100


def T(u,v):
	ca = math.cos(a)
	sa = math.sin(a)
	u1 = u - u0
	v1 = v - v0
	x = ca*u1 - sa*v1 + u
	y = sa*u1 + ca*v1 + v

	return(x, y)

def T_inverse(x,y):
	ca = math.cos(a)
	sa = math.sin(a)
	x1= x -x0
	y1= y-y0
	u= ca*x1 + sa*y1 +u0
	v= -sa*x1 + ca*y1 + v0

	return (u,v)