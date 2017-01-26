import threading,random
from time import sleep,time
from pyglet.clock import schedule_interval
from particle import Particle
from screen_object import ScreenObject
from window import Window
from utils import Random3f
import variables,space,acceleration


# Simulation File
# this file handles calling physics to be done, and creating
# and moving the screen objects for every particle


class Simulation:
  def __init__(self,screen_objects):

    # an array of the particles
    self.particles = []

    # an array of the ScreenObjects for all the particles
    self.screen_objects = screen_objects


    self.new_particle()
    self.new_particle()
    self.new_particle()
    self.new_particle()
    self.new_particle()

    schedule_interval(self.update,variables.physics_update_time)


  # do all the physics calculations and move the particles
  def update(self,last_call_time):
    for i in range(len(self.particles)):

      # do gravity here
      #gravity(particles)

      # move the particle
      self.particles[i].update()
      # update the shape on screen
      self.screen_objects[i].update_from_particle(self.particles[i])


  # create a new particle and start drawing it
  def new_particle(self):
    particle = Particle()

    # random position between -5,-5,-5 and 5,5,5
    particle.position = Random3f([-5,5],[-5,5],[-5,5])

    # random velocity between -0.01,-0.01,-0.01 and 0.01,0.01,0.01
    particle.velocity = space.Vector3f(Random3f([-0.01,0.01],[-0.01,0.01],[-0.01,0.01]))

    # save the new particle
    self.particles.append(particle)

    # create a ScreenObject for drawing the new particle
    screen_object = ScreenObject("sphere",self.particles[len(self.particles)-1].
      position,radius=self.particles[len(self.particles)-1].radius)

    # save the screen object
    self.screen_objects.append(screen_object)