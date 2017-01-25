n=2
from vectors import Vector3f
from position import Position3f

v1 = Vector3f(Position3f(2,5,7),Position3f(0,0,0))
vector1 = v1.direction
v2 = Vector3f(Position3f(9,1,5),Position3f(0,0,0))
vector2 = v2.direction

m=0
k=0

vectors=[vector1,vector2]
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
			y-x
			print(r)
			m =+ 1
			if m == n:
				m=0
				k =+ 1
				break
