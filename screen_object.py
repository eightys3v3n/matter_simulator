from pyglet import gl
from space import Position3f
import variables


POINTS = 1
QUADS = 2


class ScreenObject:
  def __init__(self,o_type,position=None,size=None,radius=None,colour=None,headless=False):
    self.headless = headless
    self.type = None
    self.radius = 1
    self.sphere_args = None
    self.max_points = 0
    self.vertices = []
    self.vertices_colour = []
    self.quadric = None
    self.size = Position3f()
    self.position = Position3f()
    self.size = Position3f()
    self.colour = [255.0,255.0,255.0]

    if position is not None:
      self.position = position
    if colour is not None:
      self.colour = colour

    if not isinstance(position,Position3f):
      raise TypeError("position must be a Position3f")


    if o_type == "point":
      self.type = "point"
      self.max_points = 1
      self.add_point(position)

    elif o_type == "rectangle":
      self.type = "rectangle"
      self.max_points = 4

      if size is not None:
        self.size = size
      if not isinstance(size,Position3f):
        raise TypeError("size must be a Position3f")
      self.generate_rectangle()

    elif o_type == "sphere":
      self.type = "sphere"
      self.max_points = 1
      self.radius = radius
      self.sphere_args = variables.default_sphere_args

      if not self.headless:
        self.quadric = gl.gluNewQuadric()

    else:
      raise TypeError("unknown object type",o_type)


  @property
  def gl_mode(self):
    if self.headless:
      return None

    if self.type == "point":
      return gl.GL_POINTS
    elif self.type == "rectangle":
      return gl.GL_QUADS
    else:
      raise Exception("unrecognized mode",self.type)


  @property
  def gl_vertices(self):
    if self.headless:
      return None

    if self.type == "sphere":
      raise Exception("can't get the vertices of a sphere")

    ret = ()
    for vert in self.vertices:
      ret += (vert.x,vert.y,vert.z)
    return ("v3f",ret)


  @property
  def gl_order(self):
    if self.headless:
      return None

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
      raise TypeError("expected a Position3f but got",point)

    if len(self.vertices) >= self.max_points:
      print("can't add a more points to '"+self.type+"' object which has a maximum of "+str(self.max_points)+" points")
    else:
      self.vertices.append(point)
      self.vertices_colour.append(self.colour)


  def add_points(self,points):
    if self.type == "sphere":
      raise Exception("can't add points to a sphere, they are auto-generated")
    if not all(isinstance(point,Position3f) for point in points):
      raise TypeError("expected a tuple of Position3f objects but got",points)

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
      raise Exception("you can't have a 3d rectangle",self.size)


  def update_from_particle(self,particle):
    self.position = particle.position
    self.radius = particle.radius


  def draw(self):
    if self.headless:
      return None

    if self.type == "sphere":
      gl.glColor3f(self.colour[0],self.colour[1],self.colour[2])
      gl.glTranslatef(self.position.x,self.position.y,self.position.z)
      gl.gluSphere(self.quadric,self.radius,self.sphere_args[0],self.sphere_args[1])
      gl.glTranslatef(-self.position.x,-self.position.y,-self.position.z)
    else:
      gl.glShape()
      gl.glAddPoint
      gl.glEnd()