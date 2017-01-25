from position import Position3f

class Vector3f:
  def __init__(self,destination=Position3f(),origin=Position3f()):
    self.origin = origin
    self.direction = direction


  @property
  def magnitude(self):
    mag = 0.0
    mag = pow(self.destination.x - self.origin.x,2)
    mag += pow(self.destination.y - self.origin.y,2)
    mag += pow(self.destination.z - self.origin.z,2)
    mag = sqrt(mag)
    return mag


  @property
  def angles(self):
    x = self.direction.x - self.origin.x
    y = self.direction.y - self.origin.y
    z = self.direction.z - self.origin.z
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
    elif self.direction != other.direction:
      return False
    return True