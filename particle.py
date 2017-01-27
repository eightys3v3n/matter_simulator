import copy
import variables
from screen_object import ScreenObject
from space import Position3f,Vector3f

# Particle File
# this file is for all the functions and classes that store the information about particles
# these particles will be what move around the screen in clumps (spheres)


class Particle:
  def __init__(self,mass=100,density=2):
    self.mass = mass
    self.density = density
    self.position = Position3f()
    self.velocity = Vector3f(Position3f(0,0,0))
    self.acceleration = Vector3f(Position3f(0,0,0))


  # returns the radius as calculated by mass and density
  # used like 'r = particle.radius'
  @property
  def radius(self):
    v = self.mass * self.density
    r = pow((3.0/(4.0 * variables.pi)) * v,1.0/3.0)
    return r


  # returns the vector for the displacement between two particles.
  # basically 'a.displacement(b)' returns what you have to do to a
  # to get to b
  def displacement(self,other):
    new = Vector3f()
    new.origin = self.position
    new.destination = other.position
    return new


  # is called every unit of time to move the particle according to it's
  # velocity and acceleration
  def update(self):
    self.velocity += self.acceleration
    self.position += self.velocity.direction.destination


  # when you use 'if a == b' it calls 'if a.__eq__(b)'
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