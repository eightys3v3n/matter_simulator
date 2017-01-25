import variables
from position import Position3f
from vectors import Vector3f


# Particle File
# this file is for all the functions and classes that store the information about materials
# these materials will be what move around the screen in clumps (spheres)


class Particle:
  def __init__(self,mass=0,density=0):
    self.mass = mass
    self.density = density
    self.position = Position3f()
    self.velocity = Vector3f()
    self.acceleration = Vector3f()


  # returns the radius as calculated by mass and density
  @property
  def radius(self):
    v = self.mass * self.density
    r = pow((3.0/(4.0 * variables.pi)) * v,1.0/3.0)
    return r


  # will be called every frame to move the particle
  def update(self):
    self.velocity += self.acceleration #make sure that this is actually acceleration * time
    self.position += self.velocity


  def __eq__(self,other):
    if self.mass != other.mass:
      return False

    if self.density != other.density:
      return False

    if self.position != other.position:
      return False

    if self.velocity != other.velocity:
      return False

    if self.acceleration != other.acceleration:
      return False

    return True