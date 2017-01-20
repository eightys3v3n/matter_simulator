from pyglet.gl import GL_POINTS
from space import Position3f
import variables


class ScreenObject:
  def __init__(self,o_type,points=[]):
    self.vertices = []
    self.colour = []
    self.type = None
    self.max_points = 0


    if o_type in ["point","Point"]:
      self.type = "point"
      self.gl_mode = GL_POINTS
      self.max_points = 1
    else:
      raise Exception("unknown object type",o_type)

    if not isinstance(o_type,str):
      raise Exception("expected a string for type, got '"+str(type(o_type))+"'")

    if points != []:
      if isinstance(points,Position3f):
        self.add_point(points)
      elif isinstance(points,(list,tuple,Position3f)):
        self.add_points(points)
      else:
        raise Exception("expected a Position3f or an array of, got '"+str(type(points))+"'")


  def __getattr__(self,key):
    if key == "gl_vertices":
      ret = ()
      for vert in self.vertices:
        ret += vert.raw
      return ("v3f",ret)
    elif key == "gl_order":
      range(0)


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