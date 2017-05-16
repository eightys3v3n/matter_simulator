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


def gravity_effect(mass,displacement):
  """
  mass:         int or float which is the mass of the particle who is being acted on
  displacement: vector3f which is the distance from the particle being acted on to the particle acting on it
  acceleration: vector3f which is the current acceleration of the particle being acted on
  """
  scalar = variables.gravity * (mass / displacement.dot(displacement))
<<<<<<< HEAD
=======
  unit_vector = Vector3f()
>>>>>>> parent of 75354af... I fixed it !!!!!
  unit_vector = displacement / displacement.magnitude
  acceleration = unit_vector * scalar
  acceleration.origin.x = round(acceleration.origin.x,variables.precision)
  acceleration.origin.y = round(acceleration.origin.y,variables.precision)
  acceleration.origin.z = round(acceleration.origin.z,variables.precision)
  acceleration.destination.x = round(acceleration.destination.x,variables.precision)
  acceleration.destination.y = round(acceleration.destination.y,variables.precision)
  acceleration.destination.z = round(acceleration.destination.z,variables.precision)

  return acceleration

def gravity_between_particles(p1,p2):
  displacement = p1.displacement(p2)

  acceleration = gravity_effect(p1.mass,displacement)
  acceleration.origin.x = round(acceleration.origin.x,variables.precision)
  acceleration.origin.y = round(acceleration.origin.y,variables.precision)
  acceleration.origin.z = round(acceleration.origin.z,variables.precision)
  acceleration.destination.x = round(acceleration.destination.x,variables.precision)
  acceleration.destination.y = round(acceleration.destination.y,variables.precision)
  acceleration.destination.z = round(acceleration.destination.z,variables.precision)

  return acceleration
  
#this is supposed to run after the first time step to check the changes. 

	
def gravity_on_particle(p1,particles):
  for particle in particles:
    if particle is p1:
      continue
<<<<<<< HEAD
  
    accel = p1.acceleration
=======

    accel = Vector3f()
>>>>>>> parent of 75354af... I fixed it !!!!!
    print("before",accel)
    accel = gravity_between_particles(p1,particle)
    print("after",accel)

  accel.origin.x = round(accel.origin.x,variables.precision)
  accel.origin.y = round(accel.origin.y,variables.precision)
  accel.origin.z = round(accel.origin.z,variables.precision)
  accel.destination.x = round(accel.destination.x,variables.precision)
  accel.destination.y = round(accel.destination.y,variables.precision)
  accel.destination.z = round(accel.destination.z,variables.precision)



  return accel
def GPE(p1, particles):
  p1.GPE = 0
  for particle in particles:
    if particle is p1:
      continue
    p1.GPE += p1.mass * p1.acceleration.magnitude * p1.displacement(particle).magnitude 
	
def gravity(particles):
  for i in range(len(particles)):
<<<<<<< HEAD
    particles[i].acceleration = gravity_on_particle(particles[i],particles)
def gravitational_effect(particles):
  for i in range(len(particles)):
    particles[i].GPE = GPE(particles[i],particles)
=======
    print(i,end=":")
    particles[i].acceleration = gravity_on_particle(particles[i],particles)
>>>>>>> parent of 75354af... I fixed it !!!!!
