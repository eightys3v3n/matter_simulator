
from particle import Particle 
from space import Postion3f, Vector3f
import variables 
from Displace import interactions
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

# okay so what needs to happen is that position which is the vector towards the parent particle needs to have that particles mass associated with it, and then gravity will work
def gravitaitonal_Fields(self.mass, G, self.acceleration, position):
  scalar = G*self.mass / dot.position(position)
  unit_vector = Vector3f(Postion3f(1,1,1))
  acceleration = unit_vector.scalar_mult
  self.acceleration =+ acceleration
  return self.acceleration



