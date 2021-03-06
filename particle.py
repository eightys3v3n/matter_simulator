import copy
import variables
from screen_object import ScreenObject
from space import Position3f,Vector3f
from utils import Random3f

# Particle File
# this file is for all the functions and classes that store the information about particles
# these particles will be what move around the screen in clumps (spheres)
from random import randint

class Particle:
  def __init__(self,mass=None,density=None,position=None):
    self.mass = randint(10,1000)
    self.density = 10
    self.position = Random3f([-400,400],[-400,400],[-400,400])
    self.velocity_initial = Vector3f(Random3f([-200,200],[-200,200],[-200,200]))
    self.velocity = Vector3f(Position3f(0,0,0)) + self.velocity_initial
    self.acceleration = Vector3f()
    self.GPE = 0
    self.KE = .5*self.mass*self.velocity.dot(self.velocity)
    self.E_total = self.GPE + self.KE
    if mass is not None:
      self.mass == mass
    if density is not None:
      self.density = density
    if position is not None:
      self.position = position

  # returns the radius as calculated by mass and density
  # used like 'r = particle.radius'
  @property
  def radius(self):
    v = self.mass / self.density
    r = pow((3.0/(4.0 * variables.pi)) * v,1.0/3.0)
    return r


  # returns the vector for the displacement between two particles.
  # basically 'a.displacement(b)' returns what you have to do to a
  # to get to b
  def displacement(self,other):
    new = Vector3f()
    new.origin = self.position
    new.destination = other.position - self.position
    new.destination = other.position
    return new

  # is called every unit of time to move the particle according to it's
  # velocity and acceleration
  def update(self):
    #print("AAAAAAAAA:"+str(self.acceleration))
    #print(self.acceleration)
    self.GPE = self.E_total - self.KE
    self.velocity += ((self.acceleration/self.acceleration.magnitude)*((2*self.KE)/self.mass)**(1/2))*0.001
    self.position += self.velocity.direction.destination *.001
    self.KE = 0.5*self.mass*self.velocity.dot(self.velocity)

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
  def __repr__(self):
    string = ""
    #string = "radius:"+str(self.radius)+"\n"
    string += "position:"+str(self.position)+"\n"
    string += "velocity:"+str(self.velocity)+"\n"
    string += "acceleration:"+str(self.acceleration)
    return string