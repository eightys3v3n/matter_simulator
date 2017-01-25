from position import Position3f


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


  def __str__(self):
    array = []
    array.append(self.destination.x - self.origin.x)
    array.append(self.destination.y - self.origin.y)
    array.append(self.destination.z - self.origin.z)
    return array.__str__()

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

  def __str__(self):
    array = []
    array.append(self.destination.x - self.origin.x)
    array.append(self.destination.y - self.origin.y)
    array.append(self.destination.z - self.origin.z)
    return array.__str__()


def main():
	L = Vector3f(Position3f(9,13,4),Position3f(2,2,1))
	h=L.direction
	print(h)
	k=L.magnitude
	print(k)
	input("does this look right")


if __name__ == "__main__":
  main()