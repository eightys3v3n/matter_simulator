from pyglet.gl import *
from space import Position3f
import variables


class ScreenObject:
  def __init__(self,o_type,position=Position3f(),size=Position3f(10,10,0),radius=1,colour=[255.0,255.0,255.0]):
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
    self.quadric = None

    if not isinstance(position,Position3f):
      raise Exception("position must be a Position3f")

    if not isinstance(size,Position3f):
      raise Exception("size must be a Position3f")

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
      self.generate_rectangle()

    elif o_type == "sphere":
      self.type = "sphere"
      self.max_points = 1
      self.radius = radius
      self.sphere_args = variables.default_sphere_args
      self.quadric = gluNewQuadric()

    else:
      raise Exception("unknown object type",o_type)


  @property
  def gl_vertices(self):
    if self.type == "sphere":
      raise Exception("can't get the vertices of a sphere")

    ret = ()
    for vert in self.vertices:
      ret += (vert.x,vert.y,vert.z)
    return ("v3f",ret)


  @property
  def gl_order(self):
    if self.type != "rectangle":
      raise Exception("can't get vertices of objects other than rectangles and cubes")

    r = []
    for i in range(len(self.vertices)):
      r.append(i)
    r.append(0)

    return r


  def add_point(self,point):
    if self.type == "sphere":
      raise Exception("can't add points to a sphere, they are auto-generated")
    if not isinstance(point,Position3f):
      raise Exception("expected a Position3f object",type(point))

    if len(self.vertices) >= self.max_points:
      print("can't add a more points to '"+self.type+"' object which has a maximum of "+str(self.max_points)+" points")
    else:
      self.vertices.append(point)
      self.vertices_colour.append(self.colour)


  def add_points(self,points):
    if self.type == "sphere":
      raise Exception("can't add points to a sphere, they are auto-generated")
    if not isinstance(points,(list,tuple,Position3f)):
      raise Exception("expected a tuple of Position3f objects",points)

    for point in points:
      self.add_point(point)


  def generate_rectangle(self):
    if self.type != "rectangle":
      raise Exception("can't generate a rectangle of non-rectangle objects")

    p = self.position
    p2 = Position3f()
    p2.x = p.x + self.size.x
    p2.y = p.y + self.size.y
    p2.z = p.z + self.size.z

    if self.size.x == 0:
      self.add_point(Position3f(p.x,p.y-p2.y/2,p.z-p2.z/2))
      self.add_point(Position3f(p.x,p.y+p2.y/2,p.z-p2.z/2))
      self.add_point(Position3f(p.x,p.y+p2.y/2,p.z+p2.z/2))
      self.add_point(Position3f(p.x,p.y-p2.y/2,p.z+p2.z/2))
    elif self.size.y == 0:
      self.add_point(Position3f(p.x-p2.x/2,p.y,p.z+p2.z/2))
      self.add_point(Position3f(p.x-p2.x/2,p.y,p.z-p2.z/2))
      self.add_point(Position3f(p.x+p2.x/2,p.y,p.z-p2.z/2))
      self.add_point(Position3f(p.x+p2.x/2,p.y,p.z+p2.z/2))
    elif self.size.z == 0:
      self.add_point(Position3f(p.x-p2.x/2,p.y-p2.y/2,p.z))
      self.add_point(Position3f(p.x-p2.x/2,p.y+p2.y/2,p.z))
      self.add_point(Position3f(p.x+p2.x/2,p.y+p2.y/2,p.z))
      self.add_point(Position3f(p.x+p2.x/2,p.y-p2.y/2,p.z))
    else:
      raise Exception("you can'y have a 3d rectangle",self.size)


  def update_from_particle(self,particle):
    self.position = particle.position
    self.radius = particle.radius


  def draw(self):
    if self.type != "sphere":
      raise Exception("can only use ScreenObject.draw on sphere types")

    glColor3f(self.colour[0],self.colour[1],self.colour[2])
    glTranslatef(self.position.x,self.position.y,self.position.z)
    gluSphere(self.quadric,self.radius,self.sphere_args[0],self.sphere_args[1])
    glTranslatef(-self.position.x,-self.position.y,-self.position.z)