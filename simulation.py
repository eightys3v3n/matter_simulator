import threading,random
from time import sleep,time
from pyglet.clock import schedule_interval
from particle import Particle
from screen_object import ScreenObject
from window import Window
from utils import Random3f
from gravity import gravity
import variables,space


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
    #self.screen_objects[0].colour = variables.cool_colour
    #self.particles[0].mass = 1000
    #self.particles[0].density = 100
    #self.particles[0].position = space.Position3f(0,0,0)
   
    
    #self.new_particle()
    #self.new_particle()
    #self.new_particle()
    #self.new_particle()
    #self.new_particle()
    #self.new_particle()
       
    schedule_interval(self.update,variables.physics_update_time)
  # do all the physics calculations and move the particles
  def update(self,last_call_time):
    for i in range(0,len(self.particles)):

      # do collisions
      self.collide()

      # do gravity here
      gravity(self.particles)

      self.reset_out_of_bounds()

      # move the particle
      self.particles[i].update()

      #if i == 0:
        #print(self.particles[i],end="\n\n")

      # update the shape on screen
      self.screen_objects[i].update_from_particle(self.particles[i])


  # create a new particle and start drawing it
  def new_particle(self):
    particle = Particle()
    self.reset_particle(particle)

    # save the new particle
    self.particles.append(particle)

    # create a ScreenObject for drawing the new particle
    screen_object = ScreenObject("sphere",self.particles[len(self.particles)-1].
      position,radius=self.particles[len(self.particles)-1].radius)

    # save the screen object
    self.screen_objects.append(screen_object)


  def collide(self):
    for a in range(len(self.particles)):
      p1 = self.particles[a]
      for p2 in self.particles:
        if p1 != p2:
          if p1.displacement(p2).magnitude <= p1.radius + p2.radius:
            print("collided")
            self.reset_particle(p1)


  def reset_particle(self,particle):
    print("resetting particle")
    # random position between -5,-5,-5 and 5,5,5
    particle.position = Random3f([-10,10],
                                 [-10,10],
                                 [-10,10])

    #random velocity between -0.01,-0.01,-0.01 and 0.01,0.01,0.01
    particle.velocity = space.Vector3f(Random3f([-0.000001,0.000001],[-0.000001,0.000001],[-0.000001,0.000001]))

    particle.acceleration = space.Vector3f()


  def reset_out_of_bounds(self):
    for i in range(len(self.particles)):
      p = self.particles[i]
      if p.position.x > variables.simulation_bounds[0] or p.position.x < -variables.simulation_bounds[0]:
        self.reset_particle(p)
      if p.position.y > variables.simulation_bounds[1] or p.position.y < -variables.simulation_bounds[1]:
        self.reset_particle(p)
      if p.position.z > variables.simulation_bounds[2] or p.position.z < -variables.simulation_bounds[2]:
        self.reset_particle(p)
  
