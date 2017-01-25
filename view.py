from pyglet.gl import gluPerspective,glRotatef,glTranslatef
from math import hypot,cos,sin,tan,acos,atan,asin,radians,degrees,atan2
from space import Position3f,Position2f
import variables


# View File
# this file contains the stuff to change how the user is viewing the simulation
# it currently does stuff like rotating the view, looking side to side, and flying
# around the simulation space.


class View:
  def __init__(self):
    self.position = Position3f()
    self.direction = Position2f()


  def move(self,x=None,y=None,z=None,position=None):
    if x != None and y != None and z != None:
      position = Position3f(x,y,z)
    hyp = hypot(position.x,position.z)
    ang = degrees(atan2(position.z,position.x))
    ang = round(ang,6)

    self.position.x += round(hyp*cos(radians(ang+self.direction.y)),6)
    self.position.z += round(hyp*sin(radians(ang+self.direction.y)),6)
    self.position.y += position.y


  def look(self,angle):
    if not isinstance(angle,Position2f):
      raise Exception("expected Position2f",type(angle))

    self.direction += angle
    if self.direction.y > 360:
      self.direction.y -= 360
    elif self.direction.y < -360:
      self.direction.y += 360
    if self.direction.x > 90:
      self.direction.x = 90
    elif self.direction.x < -90:
      self.direction.x = -90


  def draw(self):
    gluPerspective(65.0,800.0/500.0,0.1,1000.0)
    glRotatef(self.direction.x,1,0,0)
    glRotatef(self.direction.y,0,1,0)
    glTranslatef(self.position.x,self.position.y,self.position.z)