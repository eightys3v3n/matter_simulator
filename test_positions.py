import space


def P2f_Equals_Test():
  a = space.Position2f()
  b = space.Position2f()
  if a != b:
    print("two equal space. are not equal")
    return True

  b = space.Position2f(1,1)
  if a == b:
    print("two different space. are equal")
    return True
  return False
P2f_Equals_Test_req = []


def P2f_Addition_Test():
  a = space.Position2f()
  b = space.Position2f(1,1)
  a += b
  if a != space.Position2f(1,1):
    print("didn't do += correctly",a)
    return True

  if a+b != space.Position2f(2,2):
    print("didn't add correctly",a+b)
    return True
  return False
P2f_Addition_Test_req = []


def P3f_Dot_Test():
  a = space.Position3f(2,3,7)
  b = space.Position3f(4,8,2)
  if a.dot(b) != 46:
    print("incorrect dot product 2,3,7 . 4,8,2 = 46|",a.dot(b))
    return True

  a = space.Position3f(3,3,3)
  b = space.Position3f(2,2,2)
  if a.dot(b) != 18:
    print("incorrect dot product 3,3,3 . 2,2,2 = 18|",a.dot(b))
    return True

  return False
P3f_Dot_Test_req = []


def Position2f_Test():
  a = space.Position2f(0,0)
  b = space.Position2f(2,2)
  if a.displacement(b) != space.Position2f(2,2):
    print("displacement is incorrect 2,2",a.displacement(b))
    return True

  a = space.Position2f()
  if a.angle != 0.0:
    print("angle for 0,0 is incorrect",a.angle)
    return True

  a = space.Position2f(1,1)
  if a.angle != 45.0:
    print("angle for 1,1 is incorrect",a.angle)
    return True

  a = space.Position2f(0,1)
  if a.angle != 90.0:
    print("angle for 0,1 is incorrect",a.angle)
    return True

  a = space.Position2f(1,0)
  if a.angle != 0.0:
    print("angle for 1,0 is incorrect",a.angle)
    return True

  return False
Position2f_Test_req = [P2f_Equals_Test,P2f_Addition_Test]


def Position3f_Test():
  a = space.Position3f(0,0,0)
  b = space.Position3f(0,0,0)
  if a != b:
    print("two equal space. are not equal")
    return True

  b = space.Position3f(1,1,1)
  if a == b:
    print("two different space. are equal")
    return True

  a += b
  if a != space.Position3f(1,1,1):
    print("didn't do += correctly",a)
    return True

  if a+b != space.Position3f(2,2,2):
    print("didn't add correctly",a+b)
    return True

  a = space.Position3f(1.5,2,4) * space.Position3f(5,2,1)
  if a != space.Position3f(7.5,4,4):
    print("broken multiplication 1.5,2,4 * 5,2,1 = 7.5,4,4",a)
    return True

  a = space.Position3f(3,6,9)
  a *= space.Position3f(2,0.5,3)
  if a != space.Position3f(6,3,27):
    print("broken multiplication 3,6,9 * 2,0.5,3 = 6,3,27",a)
    return True

  a = space.Position3f(0,0,0)
  b = space.Position3f(2,2,2)
  if a.displacement(b) != space.Vector3f(space.Position3f(2,2,2)):
    print("displacement is incorrect 2,2,2",a.displacement(b))
    return True

  return False
Position3f_Test_req = [Position2f_Test]


def Positions_Test():
  return None
Positions_Test_req = [Position2f_Test,Position3f_Test]