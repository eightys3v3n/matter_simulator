import copy
from math import degrees,hypot,atan,cos,sin,atan2,radians,asin,acos,sqrt
import variables

"""
Classes and to keep attributes of an object in space.
"""


global precision
precision = variables.precision


class Position2f:
  """
  A coordinate in 2D space. Defined by x and y.
  """
  def __init__(self,x=None,y=None,angle=None):
    """
    Construct a new position object
      optional param:x      the x value of the new object
      optional param:y      the y value of the new object
      optional param:angle  an angle which you desire the coordinates for
        this will set x and y to the values for the given angle in a unit circle
    """
    global precision

    self.x = 0.0
    self.y = 0.0

    if x is not None:
      self.x = float(x)
    if y is not None:
      self.y = float(y)

    if angle is not None:
      angle = float(angle)
      self.x = cos(radians(angle))
      self.y = sin(radians(angle))
      self.x = round(self.x,precision)
      self.y = round(self.y,precision)

  @property
  def array(self):
    """
    returns: an array, [x,y], for this object
    """
    return [self.x,self.y]


  @property
  def angle(self):
    """
    returns: the angle of this position from (0,0)
    The return angle is rounded to variables.precision digits
    """
    global precision

    angle = 0
    if self.x:
      angle = degrees(atan(self.y/self.x))
      angle = round(angle,presicion)
    elif self.y:
      angle = degrees(asin(self.y))
      angle = round(angle,presicion)
    return angle


  def __str__(self):
    """
    returns: a string representation of this position
      '(x,y)'
    """
    return "("+str(self.x)+","+str(self.y)+")"


  def __repr__(self):
    """
    Used when this class is printed with 'print()'
    returns: self.__str__()
    """
    return self.__str__()


  # called when you do 'if position == otherposition'
  def __eq__(self,other):
    """
    other: another Position2f object
    returns: True if this element and other have the same values

      a = Position2f(2,2)
      b = Position2f(3,3)
      c = a == b
      # c is False

      b = Position(2,2)
      c = a == b
      #c is True
    """
    if not isinstance(other,Position2f):
      return False

    if self.x != other.x:
      return False
    if self.y != other.y:
      return False
    return True


  # is called when you do 'abc + def' or 'abc += def'
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
  def __init__(self,x=None,y=None,z=None):
    self.x = 0.0
    self.y = 0.0
    self.z = 0.0

    if x is not None:
      self.x = float(x)
    if y is not None:
      self.y = float(y)
    if z is not None:
      self.z = float(z)


  @property
  def array(self):
    return [self.x,self.y,self.z]


  def dot(self,other):
    """
    Returns the dot product of self and other, both Position3f tyoes. or it should; it's unchecked
    """
    if not isinstance(other,Position3f):
      raise Exception("can't get the dot product of Position3f and ",other)

    ret = Position3f()
    ret.x = self.x * other.x
    ret.y = self.y * other.y
    ret.z = self.z * other.z

    return ret.x + ret.y + ret.z


  @property
  def self_dot(self):
    return self.dot(self)


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


  def __ne__(self,other):
    if not isinstance(other,Position3f):
      return True

    if self.x != other.x:
      return True
    if self.y != other.y:
      return True
    if self.z != other.z:
      return True

    return False


  def __add__(self,other):
    if not isinstance(other,Position3f):
      raise Exception("can't add Position3f and",other)

    new = Position3f()
    new.x = self.x + other.x
    new.y = self.y + other.y
    new.z = self.z + other.z
    return new


  # when doing a += b self is a and other is b
  def __iadd__(self,other):
    if not isinstance(other,Position3f):
      raise Exception("can't add Position3f and",other)

    self.x += other.x
    self.y += other.y
    self.z += other.z
    return self


  def __sub__(self,other):
    if not isinstance(other,Position3f):
      raise TypeError

    new = Position3f()
    new.x = self.x - other.x
    new.y = self.y - other.y
    new.z = self.z - other.z
    return new


  def __isub__(self,other):
    if not isinstance(other,Position3f):
      raise TypeError

    self.x -= other.x
    self.y -= other.y
    self.z -= other.z
    return self



  def __mul__(self,other):
    if isinstance(other,Position3f):
      new = Position3f()
      new.x = self.x * other.x
      new.y = self.y * other.y
      new.z = self.z * other.z
      return new
    elif isinstance(other,float) or isinstance(other,int):
      new = Position3f()
      new.x = self.x * other
      new.y = self.y * other
      new.z = self.z * other
      return new
    else:
      raise Exception("can't multiple Position3f and",type(other))


  def __imul__(self,other):
    if isinstance(other,Position3f):
      self.x *= other.x
      self.y *= other.y
      self.z *= other.z
    elif isinstance(other,float) or isinstance(other,int):
      self.x *= other
      self.y *= other
      self.z *= other
    else:
      raise Exception("can't multiply Position3f and",type(other))

    return self


  def __truediv__(self,other):
    if isinstance(other,Position3f):
      raise NotImplementedError("division of Position3f types isn't implemented")

    elif isinstance(other,(int,float)):
      ret = Position3f()
      ret.x = self.x / other
      ret.y = self.y / other
      ret.z = self.z / other
    else:
      raise TypeError("can't divide Position3f by",other)

    return ret


  def __itruediv__(self,other):
    if isinstance(other,Position3f):
      raise NotImplementedError("in-place division of Position3f types isn't implemented")

    elif isinstance(other,(int,float)):
      self.x /= other
      self.y /= other
      self.z /= other
    else:
      raise TypeError("can't divide Position3f by",type(other))

    return self


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
  """
  A class for storing a 3D vector.
  The vector is stored as an origin(Position3f) and a destination(Position3f).
  """
  def __init__(self,*args,**kargs):
    """
    Construct a Vector3f

    Initialization examples:
      ()               | initialize with zeros
      (a)              | initialize destination as a
                          a must be a Position3f type
      (a,b)            | initialize origin as a and destination as b
                          a,b must be Position3f types
      (x,y,z)          | initialize destination as (x,y,z) and origin as (0,0,0)
                          x,y,z must be float or int types
      (x,y,z,x1,y1,z1) | initialize origin as (x,y,z) and destination as (x1,y1,z1)
                          x,y,z,x1,y1,z1) must be float or int types
      (origin=a,destination=b) | sets the origin to a and destination to b
                              a,b must be Position3f types
    """
    self.origin = Position3f()
    self.destination = Position3f()

    if len(kargs) > 0:
      c = 0

      if "destination" in kargs:
        if not isinstance(kargs["destination"],Position3f):
          raise TypeError("destination must be a Position3f")
        self.destination = kargs["destination"]
        c += 1
      if "origin" in kargs:
        if not isinstance(kargs["origin"],Position3f):
          raise TypeError("origin must be a Position3f")
        self.origin = kargs["origin"]
        c += 1

      if c != len(kargs):
        raise Exception("unexpected number of key-word arguments",kargs)

    elif len(args) > 0:
      if len(args) == 1:
        if not isinstance(args[0],Position3f):
          raise TypeError("one argument must be a Position3f for the destination")

        self.destination = args[0]

      elif len(args) == 2:
        if not all(isinstance(arg,Position3f) for arg in args):
          raise TypeError("two arguments must be Position3f types, origin then destination")

        self.origin       = args[0]
        self.destination  = args[1]

      elif len(args) == 3:
        if not all(isinstance(arg,(int,float)) for arg in args):
          raise TypeError("three arguments must be the ints/floats for the destination")

        self.destination.x = args[0]
        self.destination.y = args[1]
        self.destination.z = args[2]

      elif len(args) == 6:
        if not all(isinstance(arg,(int,float)) for arg in args):
          raise TypeError("six arguments must be ints/floats for origin(0,1,2) then destination(3,4,5)")

        self.origin.x = args[0]
        self.origin.y = args[1]
        self.origin.z = args[2]
        self.destination.x = args[3]
        self.destination.y = args[4]
        self.destination.z = args[5]

      else:
        raise Exception("invalid number of arguments, see 'help(Vector3f)'")


  def __str__(self):
    string = "("+str(self.origin.x)+","+str(self.origin.y)+","+str(self.origin.z)+")"
    string += "->"
    string += "("+str(self.destination.x)+","+str(self.destination.y)+","+str(self.destination.z)+")"
    return string


  def __repr__(self):
    return self.__str__()


  def __eq__(self,other):
    if not isinstance(other,Vector3f):
      return False

    if self.origin != other.origin:
      return False
    if self.destination != other.destination:
      return False
    return True


  def __ne__(self,other):
    if not isinstance(other,Vector3f):
      return True

    if self.origin != other.origin:
      return True
    if self.destination != other.destination:
      return True
    return False


  def __add__(self,other):
    if not isinstance(other,Vector3f):
      raise Exception("can't add Vector3f and",other)

    new = Vector3f()
    new.origin = self.origin + other.origin
    new.destination = self.destination + other.destination

    return new


  def __iadd__(self,other):
    if not isinstance(other,Vector3f):
      raise Exception("can't add Vector3f and",other)

    self.origin += other.origin
    self.destination += other.destination

    return self


  def __sub__(self,other):
    if not isinstance(other,Vector3f):
      raise Exception("can't add Vector3f and",other)

    new = Vector3f()
    new.destination = self.destination - other.destination
    new.origin = self.origin - other.origin
    return new


  def __isub__(self,other):
    if not isinstance(other,Vector3f):
      raise Exception("can't subtract Vector3f and",other)

    self.origin -= other.origin
    self.destination -= other.destination

    return self


  def __mul__(self,other):
    if isinstance(other,Vector3f):
      raise NotImplementedError("Vector3f * Vector3f isn't implemented")

    elif isinstance(other,(int,float)):
      ret = Vector3f()
      ret.origin = self.origin
      ret.destination = self.destination * other

    else:
      raise TypeError("can't multiply Vector3f and ",other)

    return ret


  def __imul__(self,other):
    if isinstance(other,Vector3f):
      raise NotImplementedError("Vector3f *= Vector3f isn't implemented")

    elif isinstance(other,(int,float)):
      self.destination *= other

    else:
      raise TypeError("can't in-place multiply Vector3f and",other)

    return self


  def __truediv__(self,other):
    if isinstance(other,Vector3f):
      raise NotImplementedError("vector3f / vector3f isn't implimented yet")

    elif isinstance(other,int) or isinstance(other,float):
      ret = Vector3f()
      ret.origin = self.origin
      ret.destination = self.destination / other

    else:
      raise TypeError("can't divide Vector3f and ",other)

    return ret


  def __itruediv__(self,other):
    if isinstance(other,Vector3f):
      raise NotImplementedError("vector3f /= vector3f isn't implimented yet")

    elif isinstance(other,int) or isinstance(other,float):
      self.destination /= other

    else:
      raise TypeError("can't divide Vector3f and ",other)

    return self


  @property
  def from_zero(self):
    if self.origin == Position3f():
      return self

    new = Vector3f()
    new.destination = self.destination - self.origin
    return new


  @property
  def array(self):
    return [self.origin.x,self.origin.y,self.origin.z,self.destination.x,self.destination.y,self.destination.z]


  @property
  def magnitude(self):
    global precision

    d = self.direction.destination
    mag = 0.0
    mag = sqrt(pow(d.x,2)+pow(d.y,2)+pow(d.z,2))
    mag = round(mag,precision)
    return mag


  @property
  def direction(self):
    return self.from_zero


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


  def dot(self,other):
    if not isinstance(other,Vector3f):
      raise Exception("can't get the dot product of Vector3f and ",other)

    me = self.direction.destination
    you = other.direction.destination

    return me.dot(you)


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