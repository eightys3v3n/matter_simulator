import variables
from screen_object import ScreenObject
from space import Position3f,Vector3f


# Particle File
# this file is for all the functions and classes that store the information about materials
# these materials will be what move around the screen in clumps (spheres)


class Particle:
  def __init__(self,mass=10,density=1):
    self.mass = mass
    self.density = density
    self.position = Position3f()
    self.velocity = Vector3f()
    self.acceleration = Vector3f()
    self.velocity = 10


  # returns the radius as calculated by mass and density
  @property
  def radius(self):
    v = self.mass * self.density
    r = pow((3.0/(4.0 * variables.pi)) * v,1.0/3.0)
    return r


  # will be called every frame to move the particle
  def update(self):


    # PROBLEM LINE
    self.velocity += self.acceleration


    print("acceleration",self.acceleration)
    print("new velocity",self.velocity)
    self.position += self.velocity.direction.destination


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