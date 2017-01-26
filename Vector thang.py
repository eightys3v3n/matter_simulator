n=5
from screen_object import ScreenObject
from vectors import Vector3f
from position import Position3f
from particle import Particle 
v1 = Vector3f(self.position)
v2 = Vector3f(self.position)
v3 = Vector3f(self.position)
v4 = Vector3f(self.position)
v5 = Vector3f(self.position)

m=0
k=0

vectors=[]
vectors.append(v1)
vectors.append(v2)
vectors.append(v3)
vectors.append(v4)
vectors.append(v5)


x=vectors[k]
y=vectors[m]
def interactions(vectors, x, y):
	r=[]
	for x in vectors:
		for y in vectors:
			if x is y:
				m =+ 1
				if m == n:
					m=0
					k =+ 1
					break
			else:
				result=y-x
				r.append(result)
				m =+ 1
				if m == n:
					m=0
					k =+ 1
					break
	return(r)