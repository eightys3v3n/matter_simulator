# creates a field for every particle
# mass is the mass of the particle emiting the field
# s is the speparation vector between the particle that is being observed
# essentially this will give acceleration of every particle
# G is the gravitational constant 6.67408 * (10**-11)
#sum the fields of every particle on 1 particle to determine acceleration
#then do this for every particle
from random import randint
#s is just the vector and s_m can be replaced with the dot product
#mass can be related to the particular particle
#this function returns acceleration acting on particle B from A,it does not return force, to obtain force simply add all accelerations on B and multiply by Mass of B
def gravitaitonal_Fields(mass, s , s_m):
	a=[]
	a1 = (((-6.67408 * (10**-11))*mass)/(s_m)) * (s[0]/s_m)
	a.append(a1)
	a2 = ((-6.67408 * (10**-11))*mass/(s_m)) * (s[1]/s_m)
	a.append(a2)
	a3 = ((-6.67408 * (10**-11))*mass/(s_m)) * (s[2]/s_m)
	a.append(a3)
	return a

mass = randint(1,700000000)
s = [randint(0,50000),randint(0,50000),randint(0,50000)]
s_m = (s[0]**2 +s[1]**2+s[2]**2)
a = gravitaitonal_Fields(mass,s,s_m)
print (a)

input ("press enter to end")


#for every frame:
	#for all masses compared to all other masses:
		#gravitaitonal_Fields(mass,s)

