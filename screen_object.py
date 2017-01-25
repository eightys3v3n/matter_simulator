from pyglet.gl import GL_POINTS,GL_QUADS
from pyglet.gl import gluNewQuadric,gluSphere,glTranslatef
from space import Position3f
import variables


# ScreenObject File
# this file is used for classes and functions that store the information behind the shapes being
# drawn on the screen. A ScreenObject is some shape, image, or text that can be drawn in the window


class ScreenObject:
  def __init__(self,o_type,position=[]):
    self.position = Position3f()
    self.sphere_args = Position3f()
    self.vertices = []
    self.colour = []
    self.type = None
    self.max_points = 0

    if not isinstance(position,(list,tuple,Position3f)):
      raise Exception("position must be a list of Position3f",type(position))

    if o_type == "point":
      self.type = o_type
      self.gl_mode = GL_POINTS
      self.max_points = 1
      if len(position) != 1:
        raise Exception("a point can only be initialized with 1 Position3f",position)

      self.add_point(position[0])

    elif o_type == "rectangle":
      self.type = o_type
      self.gl_mode = GL_QUADS
      self.max_points = 4

      if len(position) != 2:
        raise Exception("a rectangle can only be initialized with 2 Position3f",position)
      self.rectangle_at(position[0],position[1])

    elif o_type == "cube":
      self.type = o_type
      self.gl_mode = GL_QUADS
      self.max_points = 24

    elif o_type == "sphere":
      self.type = o_type
      self.gl_mode = None
      self.max_points = 2

      if len(position) != 2:
        raise Exception("a sphere can only be initialized with 2 Position3f",position)

      self.position = position[0]
      self.sphere_args = position[1]

    else:
      raise Exception("unknown object type",o_type)

    if not isinstance(o_type,str):
      raise Exception("expected a string for type, got '"+str(type(o_type))+"'")


  def __getattr__(self,key):
    if key == "gl_vertices":
      ret = ()
      for vert in self.vertices:
        ret += (vert.x,vert.y,vert.z)
      return ("v3f",ret)
    elif key == "gl_order":
      r = []
      if self.type == "point":
        r = [0]
      elif self.type == "rectangle" or self.type == "cube":
        for i in range(len(self.vertices)):
          r.append(i)
        r.append(0)

      return r


  def add_point(self,point):
    if not isinstance(point,Position3f):
      raise Exception("expected a Position3f object",type(point))

    if len(self.vertices) >= self.max_points:
      print("can't add a second point to a point object")
    else:
      self.vertices.append(point)
      self.colour.append(variables.default_colour)


  def add_points(self,points):
    if not isinstance(points,(list,tuple,Position3f)):
      raise Exception("expected an array of Position3f objects",type(points))

    for point in points:
      self.add_point(point)


  def rectangle_at(self,pos,size):
    if size.x == 0:
      self.add_point(Position3f(pos.x,pos.y-size.y/2,pos.z-size.z/2))
      self.add_point(Position3f(pos.x,pos.y+size.y/2,pos.z-size.z/2))
      self.add_point(Position3f(pos.x,pos.y+size.y/2,pos.z+size.z/2))
      self.add_point(Position3f(pos.x,pos.y-size.y/2,pos.z+size.z/2))
    elif size.y == 0:
      self.add_point(Position3f(pos.x-size.x/2,pos.y,pos.z+size.z/2))
      self.add_point(Position3f(pos.x-size.x/2,pos.y,pos.z-size.z/2))
      self.add_point(Position3f(pos.x+size.x/2,pos.y,pos.z-size.z/2))
      self.add_point(Position3f(pos.x+size.x/2,pos.y,pos.z+size.z/2))
    elif size.z == 0:
      self.add_point(Position3f(pos.x-size.x/2,pos.y-size.y/2,pos.z))
      self.add_point(Position3f(pos.x-size.x/2,pos.y+size.y/2,pos.z))
      self.add_point(Position3f(pos.x+size.x/2,pos.y+size.y/2,pos.z))
      self.add_point(Position3f(pos.x+size.x/2,pos.y-size.y/2,pos.z))


  def draw(self):
    if self.type == "sphere":
      sphere = gluNewQuadric()
      glTranslatef(self.position.x,self.position.y,self.position.z)
      gluSphere(sphere,10,100,20)
      self.position.x += 1