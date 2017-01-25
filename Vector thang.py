n=2 #number of unique particles

from vectors import Vector3f
from position import Position3f

v1 = Vector3f(Position3f(21,23,9))

v2 = Vector3f(Position3f(9,1,5))


m=0
k=0

vectors=[]
vectors.append(v1)
vectors.append(v2)
x=vectors[k]
y=vectors[m]
for x in vectors:
	for y in vectors:
		if x is y:
			m =+ 1
			if m == n:
				m=0
				k =+ 1
				break
		else:
			r=y-x
			print(r)
			m =+ 1
			if m == n:
				m=0
				k =+ 1
				break