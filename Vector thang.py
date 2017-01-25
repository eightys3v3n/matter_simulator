n=5

point1 = [2,5,7]
point2 = [8,10,3]
point3 = [7,12,13]
point4 = [1,2,3]
point5 = [7,2,4]

m=0
k=0

points=[point1,point2,point3,point4,point5]
x=points[k]
y=points[m]
for x in points:
	for y in points:
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
	