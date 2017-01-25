import threading,random
from time import sleep,time
from pyglet.clock import schedule_interval
from particle import Particle
from screen_object import ScreenObject
from window import Window
from utils import Random3f
import variables,space


class Simulation:
  def __init__(self,screen_objects):
    self.particles = []
    self.screen_objects = screen_objects
    self.new_particle()
    self.new_particle()
    self.new_particle()
    self.new_particle()
    self.new_particle()

    schedule_interval(self.update,variables.physics_update_time)


  def update(self,last_call_time):
    for i in range(len(self.particles)):
      self.particles[i].update()
      self.screen_objects[i].update_from_particle(self.particles[i])



  def new_particle(self):
    particle = Particle()
    particle.position = Random3f([-5,5],[-5,5],[-5,5])
    particle.velocity = space.Vector3f(Random3f([-0.01,0.01],[-0.01,0.01],[-0.01,0.01]))

    self.particles.append(particle)

    screen_object = ScreenObject("sphere",self.particles[len(self.particles)-1].
      position,radius=self.particles[len(self.particles)-1].radius)
    self.screen_objects.append(screen_object)