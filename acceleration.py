
from particle import Particle
from space import Position3f,Vector3f
import variables
#from Displace import interactions
#v1 = Vector3f(self.position)
#v2 = Vector3f(self.position)
#v3 = Vector3f(self.position)
#v4 = Vector3f(self.position)
#v5 = Vector3f(self.position)

#m=0
#k=0

#vectors=[]
#vectors.append(v1)
#vectors.append(v2)
#vectors.append(v3)
#vectors.append(v4)
#vectors.append(v5)

# okay so what needs to happen is that position which is the vector towards the parent particle needs to have that particles mass associated with it, and then gravity will work
def gravitaitonal_Fields(mass, G, acceleration, position):
  scalar = G*mass / position.dot(position)
  unit_vector = Vector3f(Position3f(1,1,1))
  acc = Vector3f(Position3f(1,1,1)) * scalar
  acceleration += acc
  return acceleration



def gravity_of_p2_on_p1(p1,p2):

  # mass of parent particle
  mass = p1.mass

  # gravitational constant
  g = variables.gravity

  # current acceleration of parent particle
  acceleration = p1.acceleration

  # displacement between parent and child particle
  displacement = p1.displacement(p2)

  new_acceleration = gravitaitonal_Fields(mass,g,acceleration,displacement)
  return new_acceleration


if __name__ == '__main__':
  parent = Particle()
  child = Particle()
  child.position = Position3f(10,10,10)

  new_acceleration = gravity_of_p2_on_p1(parent,child)
  print(new_acceleration)