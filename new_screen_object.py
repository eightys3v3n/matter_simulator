from pyglet.gl import GL_POINTS,GL_QUADS
from pyglet.gl import gluNewQuadric,gluSphere,glTranslatef
from space import Position3f
import variables


# ScreenObject File
# this file is used for classes and functions that store the information behind the shapes being
# drawn on the screen. A ScreenObject is some shape, image, or text that can be drawn in the window


class ScreenObject:
  def __init__(self,o_type,position=Position3f(),radius=1,size=Position3f(),colour=[255.0,255.0,255.0]):
    self.type = None
    self.position = position
    self.radius = None
    self.sphere_args = None
    self.size = None
    self.colour = colour
    self.max_points = 0
    self.gl_mode = None
    self.vertices = []
    self.vertices_colour = []

    if o_type == "point":
      self.type = "point"
      self.gl_mode = GL_POINTS
      self.max_points = 1
      self.add_point(position[0])

    elif o_type == "rectangle":
      self.type = "rectangle"
      self.gl_mode = GL_QUADS
      self.max_points = 4
      self.size = size
      self.rectangle_at(self.position,self.size)

    elif o_type == "cube":
      print("the cube type is incomplete")
      return None

    elif o_type == "sphere":
      self.type = "sphere"
      self.max_points = 1
      self.radius = radius
      self.sphere_args = variables.default_sphere_args

    else:
      raise Exception("unknown object type",o_type)


  @property
  def vertices(self):
    ret = ()
    for vert in self.vertices:
      ret += (vert.x,vert.y,vert.z)
    return ("v3f",ret)


  @property
  def order(self):
    if self.type != "rectangle" or self.type != "cube":
      raise Exception("can't get vertices of objects other than rectangles and cubes")

    r = []
    for i in range(len(self.vertices)):
      r.append(i)
    r.append(0)

    return r


  def add_point(self,point):
    if not isinstance(point,Position3f):
      raise Exception("expected a Position3f object",type(point))

    if len(self.vertices) >= self.max_points:
      print("can't add a more points to '"+self.type+"' object which has a maximum of "+str(self.max_points)+" points")
    else:
      self.vertices.append(point)
      self.colour_vertices.append(self.colour)


  def add_points(self,points):
    if not isinstance(points,(list,tuple,Position3f)):
      raise Exception("expected a tuple of Position3f objects",type(points))

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
      glColor3f(self.colour[0],self.colour[1],self.colour[2])
      glTranslatef(self.position.x,self.position.y,self.position.z)
      gluSphere(sphere,int(self.sphere_args.x),int(self.sphere_args.y),int(self.sphere_args.z))
      glTranslatef(-self.position.x,-self.position.y,-self.position.z)
    else:
      raise Exception("can currently only use ScreenObject.draw for spheres")