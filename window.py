from pyglet import options
from pyglet.graphics import Batch
from pyglet.window import Window
from pyglet.window import key
from pyglet.window import mouse
from pyglet.clock import schedule_interval
from pyglet.clock import set_fps_limit
from pyglet.gl import *
import variables,screen_object,space


# increase performance by not checking for errors when drawing stuff.
# i don't know how to use these errors to fix stuff so there's no reason
# to have it on
options['debug_gl'] = False


class Window(Window):
  def __init__(self):
    # puts all the stuff in the pyglet.window.Widnow class inside this class
    # so instead of creating a window and calling self.window.function, you can call
    # self.function
    super(Window,self).__init__()

    # initialize the window
    self.set_size(variables.screen_size.x,variables.screen_size.y)

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
    glEnable(GL_CULL_FACE)

    # don't draw stuff that is behind something else
    glCullFace(GL_BACK)

    # when looking at a square you are drawing, the "front" of the 2d square is the side
    # that your looking at when you draw the cube counter-clock-wise
    glFrontFace(GL_CCW)

    # an array of things to draw
    self.batch = Batch()
    self.changed_batch = False


  # called when the window closes, used to stop threads and stuff
  def quit(self):
    pass


  # this is just to stop pyglet from sleeping the program
  def prevent_sleep(self,dt):
    pass


  # handles "is the up arrow pressed right now" kind of stuff
  def check_user_input(self):
    if self.keys[key.LEFT]:
      print("left arrow key is pressed")


  def on_key_press(self,symbol,modifiers):
    if symbol == key.F:
      print("the F key was pressed")


  def on_key_release(self,symbol,modifiers):
    if symbol == key.F:
      print("the F key was released")


  def on_mouse_scroll(self,x,y,scroll_x,scroll_y):
    if scroll_y < 0:
      print("scrolling top of mouse wheel down")
    elif scroll_y > 0:
      print("scrolling top of mouse wheel up")


  def on_mouse_motion(self,x,y,dx,dy):
    print("the mouse is now at "+str(x)+","+str(y)+" and it moved "+str(dx)+","+str(dy)+" pixels to get there")


  def on_mouse_press(self,x,y,button,modifiers):
    if button == mouse.LEFT:
      print("clicked left mouse button at "+str(x)+","+str(y))


  def unload_all_objects(self):
    self.batch = Batch()


  def load_object(self,obj):
    print(obj.gl_vertices)
    print(obj.gl_mode)
    if len(obj.vertices) == 0:
      return

    if obj.type == "point":
      self.batch.add(len(obj.vertices),obj.gl_mode,None,obj.gl_vertices)
    else:
      print("loading unknown type",obj.type)
      self.batch.add_indexed(len(obj.vertices),obj.gl_mode,None,obj.gl_vertices)
    self.changed_batch = True


  def reload_objects(self,objects):
    self.unload_all_objects()

    for obj in objects:
      self.load_object(obj)


  # called every frame to actually draw the frame
  def on_draw(self):
    # checks to see if you are pressing say, the left arrow key, and does
    # what should be done when you are pressing it, say moving left
    self.check_user_input()

    self.clear() # clear the screen

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65.0,800.0/500.0,0.1,1000.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    glColor3f(175.0,175.0,175.0)
    self.batch.draw()