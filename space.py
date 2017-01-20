class Position2i:
  def __init__(self,x=0,y=0):
    self.x = x
    self.y = y


  #def __getattr__(self,key):
    #if key == "test":
      #calculate test and return it


  def __str__(self):
    return "("+str(self.x)+","+str(self.y)+")"


class Position2f:
  def __init__(self,x=0.0,y=0.0):
    self.x = x
    self.y = y


class Position3f:
  def __init__(self,x=0.0,y=0.0,z=0.0):
    self.x = x
    self.y = y
    self.z = z


  def __getattr__(self,key):
    if key == "raw":
      return (self.x,self.y,self.z)


  def __eq__(self,other):
    if not isinstance(other,Position3f):
      return False

    if self.x != other.x:
      return False
    if self.y != other.y:
      return False
    if self.z != other.z:
      return False
    return True


class Vector3f:
  def __init__(self,x=None,y=None,z=None,dx=None,dy=None,dz=None,origin=Position3f(),direction=Position3f()):
    if x != None and y != None and z != None and dx != None and dy != None and dz != None:
      origin = Position3f(x,y,z)
      direction = Position3f(dx,dy,dx)

    self.origin = origin
    self.direction = direction


  def __eq__(self,other):
    if self.origin != other.origin:
      return False
    elif self.direction != other.direction:
      return False
    return True