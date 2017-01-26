from math import degrees,hypot,atan,cos,sin,atan2,radians,asin,acos,sqrt
import variables


# Space File
# this file has the classes for measurments of things in space
# so positions, vectors. they are named like so
# capital letter first, then number of dimentions, then type
# so Vector3f is a 3d vector with floats


# a 2d position
class Position2f:
  def __init__(self,x=0.0,y=0.0,angle=None):
    x = float(x)
    y = float(y)

    if angle == None:
      self.x = x
      self.y = y
    else:
      angle = float(angle)
      self.x = cos(radians(angle))
      self.y = sin(radians(angle))
      self.x = round(self.x,6)
      self.y = round(self.y,6)


  # basically just makes functions that are called without the ()
  # needs to be replaced because it no longer ckmplains when
  # you call something that doesn't exist
  def __getattr__(self,key):
    if key == "array":
      return (self.x,self.y)
    elif key == "angle":
      angle = 0
      if self.x:
        angle = degrees(atan(self.y/self.x))
        angle = round(angle,6)
      elif self.y:
        angle = degrees(asin(self.y))
        angle = round(angle,6)
      return angle


  def __str__(self):
    return "("+str(self.x)+","+str(self.y)+")"


  def __repr__(self):
    return self.__str__()


  def __eq__(self,other):
    if not isinstance(other,Position2f):
      return False

    if self.x != other.x:
      return False
    if self.y != other.y:
      return False
    return True


  def __add__(self,other):
    if not isinstance(other,Position2f):
      raise Exception("can't add Position2f and",type(other))
    return Position2f(self.x+other.x,self.y+other.y)


  def __radd__(self,other):
    if not isinstance(other,Position2f):
      raise Exception("can't add Position2f and",type(other))
    self.x += other.x
    self.y += other.y


  def __mul__(self,other):
    if isinstance(other,Position2f):
      return Position2f(self.x*other.x,self.y*other.y)
    elif isinstance(other,float):
      return Position2f(self.x*other,self.y*other)
    else:
      raise Exception("can't multiple Position2f and",type(other))


  def __rmul__(self,other):
    if isinstance(other,Position2f):
      self.x *= other.x
      self.y *= other.y
    elif isinstance(other,float):
      self.x *= other
      self.y *= other
    else:
      raise Exception("can't multiple Position2f and",type(other))


  def displacement(self,other):
    if not isinstance(other,Position2f):
      raise Exception("can't calculate displacement between Position2f and",type(other))

    d = Position2f()
    d.x = other.x - self.x
    d.y = other.y - self.y
    return d


# a 3d position
class Position3f:
  def __init__(self,x=0,y=0,z=0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)


  @property
  def array(self):
    return (self.x,self.y,self.z)


  def __str__(self):
    return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"


  def __repr__(self):
    return self.__str__()


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


  def __add__(self,other):
    if not isinstance(other,Position3f):
      raise Exception("can't add Position3f and",other)
    return Position3f(self.x+other.x,self.y+other.y,self.z+other.z)


  # when doing a += b self is a and other is b
  def __radd__(self,other):
    if not isinstance(other,Position3f):
      raise Exception("can't add Position3f and",other)

    self.x += other.x
    self.y += other.y
    self.z += other.z


  def __sub__(self,other):
    if not isinstance(other,Position3f):
      raise Exception("can't add Position3f and",other)

    new = Position3f()
    new.x = self.x - other.x
    new.y = self.y - other.y
    new.z = self.z - other.z
    return new


  def __mul__(self,other):
    if not isinstance(other,Position3f):
      raise Exception("can't add Position3f and",other)

    if isinstance(other,Position3f):
      return Position3f(self.x*other.x,self.y*other.y,self.z*other.z)
    elif isinstance(other,float):
      return Position3f(self.x*other,self.y*other,self.z*other)
    else:
      raise Exception("can't multiple Position3f and",type(other))


  def __rmul__(self,other):
    if not isinstance(other,Position3f):
      raise Exception("can't add Position3f and",other)

    if isinstance(other,Position3f):
      self.x *= other.x
      self.y *= other.y
      self.z *= other.z
    elif isinstance(other,float):
      self.x *= other
      self.y *= other
      self.z *= other
    else:
      raise Exception("can't multiple Position3f and",type(other))


  def displacement(self,other):
    if not isinstance(other,Position3f):
      raise Exception("can't calculate displacement between Position3f and",type(other))

    d = Vector3f()
    d.origin.x = self.x
    d.origin.y = self.y
    d.origin.z = self.z
    d.destination.x = other.x
    d.destination.y = other.y
    d.destination.z = other.z
    return d


# a 3d vector, ie two 3d positions
class Vector3f:
  def __init__(self,destination=Position3f(),origin=Position3f()):
    self.origin = origin
    self.destination = destination


  @property
  def magnitude(self):
    d = self.direction.destination
    mag = 0.0
    mag = sqrt(pow(d.x,2)+pow(d.y,2)+pow(d.z,2))
    mag = round(mag,variables.precision)
    return mag


  @magnitude.setter
  def magnitude(self,v):
    new = Position3f()
    new.y = v*sin(radians(self.angles.x))
    h = v*cos(radians(self.angles.x))
    new.x = h*cos(radians(self.angles.y))
    new.z = h*sin(radians(self.angles.y))
    self.origin = Position3f()
    self.destination = new


  @property
  def direction(self):
    d = Vector3f()
    d.destination.x = self.destination.x - self.origin.x
    d.destination.y = self.destination.y - self.origin.y
    d.destination.z = self.destination.z - self.origin.z
    return d


  @property
  def angles(self):
    x = self.destination.x - self.origin.x
    y = self.destination.y - self.origin.y
    z = self.destination.z - self.origin.z
    hyp = Position2f()
    angles = Position2f()
    if y:
      angles.x = degrees(atan(y/z))
      hyp.x = hypot(z,y)
    if x:
      hyp.y = hypot(x,z)
      angles.y = degrees(atan(z/x))
    return angles


  @property
  def x(self):
    return self.destination.x - self.origin.x


  @property
  def y(self):
    return self.destination.y - self.origin.y


  @property
  def z(self):
    return self.destination.z - self.origin.z


  @x.setter
  def x(self,v):
    self.destination.x = self.origin.x + v


  @y.setter
  def y(self,v):
    self.destination.y = self.origin.y + v


  @z.setter
  def z(self,v):
    self.destination.z = self.origin.z + v



  def __eq__(self,other):
    if not isinstance(other,Vector3f):
      raise Exception("can't add Vector3f and",other)

    if self.origin != other.origin:
      return False
    elif self.destination != other.destination:
      return False
    return True


  def __sub__(self,other):
    if not isinstance(other,Vector3f):
      raise Exception("can't add Vector3f and",other)

    new = Vector3f()
    own_zero_origin = self.destination
    other_zero_origin = other.destination

    if self.origin != Position3f():
      own_zero_origin = self.direction

    if other.origin != Position3f():
      other_zero_origin = other.direction

    new.destination = own_zero_origin - other_zero_origin
    return new


  def __add__(self,other):
    if not isinstance(other,Vector3f):
      raise Exception("can't add Vector3f and",other)

    #print("   self",self)
    #print("   other",other)

    new = Vector3f()
    own_zero_origin = self.destination
    other_zero_origin = other.destination

    if self.origin != Position3f():
      own_zero_origin = self.direction.destination

    if other.origin != Position3f():
      other_zero_origin = other.direction.destination

    new.destination = own_zero_origin + other_zero_origin
    return new


  def __str__(self):
    array = []
    array.append(self.origin.x)
    array.append(self.origin.y)
    array.append(self.origin.z)
    string = array.__str__()
    array.append(self.destination.x)
    array.append(self.destination.y)
    array.append(self.destination.z)
    return array.__str__()


  def __repr__(self):
    return self.__str__()


# just a temparary test function
def main():
  a = Position3f(10,10,10)
  b = Position3f(5,5,5)
  print(a-b)

  a = Vector3f(Position3f(10,10,10))
  b = Vector3f(Position3f(0,0,0))
  a += b
  print(a)

if __name__ == "__main__":
  main()