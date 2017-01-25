n=5

vector1 = [2,5,7]
vector2 = [8,10,3]
vector3 = [7,12,13]
vector4 = [1,2,3]
vector5 = [7,2,4]

m=0
k=0

vectors=[vector1,vector2,vector3,vector4,vector5]
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
			r = []
			ri = y[0] - x[0]
			r.append(ri)
			rj = y[1] - x[1]
			r.append(rj)
			rk = y[2] - x[2]
			r.append(rk)
			print(r)
			m =+ 1
			if m == n:
				m=0
				k =+ 1
				break
