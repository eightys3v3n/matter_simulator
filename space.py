from math import degrees,hypot,atan


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


class Position3f:
  def __init__(self,x=0.0,y=0.0,z=0.0,angles=None):
    x = float(x)
    y = float(y)
    z = float(z)

    if isinstance(angles,Position2f):
      self.x = sin(radians(angles.y))
      self.y = sin(radians(angles.x))
      if angles.x:
        self.z = cos(radians(angles.x))
      elif angles.y:
        self.z = cos(radians(angles.y))
      else:
        self.z = 1.0
      self.x = round(self.x,6)
      self.y = round(self.y,6)
      self.z = round(self.z,6)
    else:
      self.x = x
      self.y = y
      self.z = z


  def __getattr__(self,key):
    if key == "array":
      return (self.x,self.y,self.z)
    elif key == "angles":
      angles = Position2f()
      if not self.x and not self.y and not self.z:
        return Position2f(0,0)
      elif not self.x and not self.y and self.z:
        return Position2f(0,0)
      elif not self.x and self.y and not self.z:
        return Position2f(90,0)
      elif self.x and not self.y and not self.z:
        return Position2f(0,90)

      if self.z:
        angles.x = degrees(atan(self.y/self.z))
      if self.x:
        angles.y = degrees(atan(self.z/self.x))
      return angles



  def __str__(self):
    return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"


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
      raise Exception("can't add Position3f and",type(other))
    return Position3f(self.x+other.x,self.y+other.y,self.z+other.z)


  # when doing a += b self is a and other is b
  def __radd__(self,other):
    if not isinstance(other,Position3f):
      raise Exception("can't add Position3f and",type(other))

    self.x += other.x
    self.y += other.y
    self.z += other.z


  def __sub__(self,other):
    new = Position3f()
    new.x = self.x - other.x
    new.y = self.y - other.y
    new.z = self.z - other.z
    return new


  def __mul__(self,other):
    if isinstance(other,Position3f):
      return Position3f(self.x*other.x,self.y*other.y,self.z*other.z)
    elif isinstance(other,float):
      return Position3f(self.x*other,self.y*other,self.z*other)
    else:
      raise Exception("can't multiple Position3f and",type(other))


  def __rmul__(self,other):
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


class Vector3f:
  def __init__(self,destination=Position3f(),origin=Position3f()):
    self.origin = origin
    self.destination = destination


  @property
  def magnitude(self):
    mag = 0.0
    mag = pow(self.destination.x - self.origin.x,2)
    mag += pow(self.destination.y - self.origin.y,2)
    mag += pow(self.destination.z - self.origin.z,2)
    mag = pow(mag,.5)
    return mag


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


  def __eq__(self,other):
    if self.origin != other.origin:
      return False
    elif self.destination != other.destination:
      return False
    return True


  def __sub__(self,other):
    new = Vector3f()
    own_zero_origin = self.destination
    other_zero_origin = other.destination

    if self.origin != Position3f():
      own_zero_origin = self.direction

    if other.origin != Position3f():
      other_zero_origin = other.direction

    new.destination = own_zero_origin - other_zero_origin
    return new


  def __str__(self):
    array = []
    array.append(self.destination.x - self.origin.x)
    array.append(self.destination.y - self.origin.y)
    array.append(self.destination.z - self.origin.z)
    return array.__str__()


def main():

  a = Position3f(10,10,10)
  b = Position3f(5,5,5)
  print(a-b)

  a = Vector3f(Position3f(10,10,10))
  b = Vector3f(Position3f(2,2,2))
  print(a-b)


  L = Vector3f(Position3f(9,13,4),Position3f(2,2,1))
  h=L.direction
  print(h)
  k=L.magnitude
  print(k)
  input("does this look right")


if __name__ == "__main__":
  main()