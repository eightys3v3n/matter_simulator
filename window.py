from pyglet import options
from pyglet.graphics import Batch
from pyglet.window import Window
from pyglet.window import key
from pyglet.window import mouse
from pyglet.clock import schedule_interval
from pyglet.clock import set_fps_limit
from pyglet.gl import *
from space import Position3f,Position2f
from view import View
from simulation import Simulation
import variables,screen_object,space


# Window File
# this file is for the classes and functions that deal with drawing things on the window and the window its self
# as well as handling things like keyboard and mouse input


# increase performance by not checking for errors when drawing stuff.
# i don't know how to use these errors to fix stuff so there's no reason
# to have it on
options['debug_gl'] = False


class Window(Window):
  def __init__(self,objects):
    # puts all the stuff in the pyglet.window.Widnow class inside this class
    # so instead of creating a window and calling self.window.function, you can call
    # self.function
    super(Window,self).__init__()

    # initialize the window
    self.set_size(int(variables.screen_size[0]),int(variables.screen_size[1]))

    # to or not to lock the mouse inside this window (true is like minecraft, false is a normal window)
    self.set_exclusive_mouse(False)

    # true limites the framerate to that of your monitor's refresh rate
    self.set_vsync(False)

    # this lets you use a is_this_key_pressed kind of function
    # without it you only get to run code when a key is pressed or released
    # so you would have to write a function to keep track of what keys are being pressed
    self.keys = key.KeyStateHandler()
    self.push_handlers(self.keys)

    # maximum framerate
    set_fps_limit(256)

    # call this function every 1/60th of a second to stop the app from sleeping when
    # the user isn't doing anything. 1/60th of a second seems to be a good number, faster
    # or slower makes the app slower.
    schedule_interval(self.prevent_sleep,1.0/60.0)

    # let the graphics card figure out whether things are on top of each other based on
    # their coordinates
    glEnable(GL_DEPTH_TEST)

    # objects that are closest should be drawn on top of further stuff
    glDepthFunc(GL_LESS)

    # don't draw stuff you can't see anyways
    #glEnable(GL_CULL_FACE)

    # don't draw stuff that is behind something else
    #glCullFace(GL_BACK)

    # when looking at a square you are drawing, the "front" of the 2d square is the side
    # that your looking at when you draw the cube counter-clock-wise
    #glFrontFace(GL_CCW)

    self.objects = objects

    self.view = View()

    self.mouse_locked = False


  # called when the window closes, used to stop threads and stuff
  def quit(self):
    pass


  # this is just to stop pyglet from sleeping the program
  def prevent_sleep(self,dt):
    pass


  # makes the mouse like it is in minecraft
  def lock_mouse(self):
    self.mouse_locked = True
    self.set_exclusive_mouse(True)


  # frees the mouse
  def unlock_mouse(self):
    self.mouse_locked = False
    self.set_exclusive_mouse(False)


  # handles "is the up arrow pressed right now" kind of stuff
  def check_user_input(self):
    view_position = Position3f()
    if self.keys[key.LEFT] or self.keys[key.A]:
      view_position.x += variables.move_speed[0]
    if self.keys[key.RIGHT] or self.keys[key.D]:
      view_position.x -= variables.move_speed[0]
    if self.keys[key.SPACE]:
      view_position.y -= variables.move_speed[1]
    if self.keys[key.LSHIFT]:
      view_position.y += variables.move_speed[1]
    if self.keys[key.UP] or self.keys[key.W]:
      view_position.z += variables.move_speed[2]
    if self.keys[key.DOWN] or self.keys[key.S]:
      view_position.z -= variables.move_speed[2]
    if view_position != Position3f():
      self.view.move(position=view_position)


  # called when a key is pressed
  def on_key_press(self,symbol,modifiers):
    if symbol == key.ESCAPE:
      self.unlock_mouse()


  # called when a key is released
  def on_key_release(self,symbol,modifiers):
    if symbol == key.F:
      print("the F key was released")


  # called when one scrolls the mouse wheel
  def on_mouse_scroll(self,x,y,scroll_x,scroll_y):
    if scroll_y < 0:
      variables.move_speed[0] *= 0.9
      variables.move_speed[1] *= 0.9
      variables.move_speed[2] *= 0.9
    elif scroll_y > 0:
      variables.move_speed[0] *= 1.1
      variables.move_speed[1] *= 1.1
      variables.move_speed[2] *= 1.1
      #print("scrolling top of mouse wheel up")


  # called when the mouse moves
  def on_mouse_motion(self,x,y,dx,dy):
    if self.mouse_locked:
      view_angle = Position2f()
      view_angle.x = -dy*variables.mouse_sensitivity[0]
      view_angle.y = dx*variables.mouse_sensitivity[1]
      self.view.look(view_angle)


  # called when ome clicks
  def on_mouse_press(self,x,y,button,modifiers):
    if button == mouse.LEFT:
      self.lock_mouse()


  # called every frame to actually draw the frame
  def on_draw(self):
    # checks to see if you are pressing say, the left arrow key, and does
    # what should be done when you are pressing it, say moving left
    self.check_user_input()

    self.clear() # clear the screen

    # GL_PROJECTION is used when you want to change how the user looks
    # at the world, but not actually move the stuff. switch to this before
    # changing the users perspective
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    self.view.draw()

    # GL_MODELVIEW is used to actually draw stuff. switch to this before
    # drawing things
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    for obj in self.objects:
      obj.draw()