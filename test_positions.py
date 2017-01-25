import space


def Position2f_Test():
  a = space.Position2f()
  b = space.Position2f()
  if a != b:
    print("two equal space. are not equal")
    return True

  b = space.Position2f(1,1)
  if a == b:
    print("two different space. are equal")
    return True

  a += b
  if a != space.Position2f(1,1):
    print("didn't do += correctly",a)
    return True

  if a+b != space.Position2f(2,2):
    print("didn't add correctly",a+b)
    return True

  a = space.Position2f(1,1) * space.Position2f(3,3)
  if a != space.Position2f(3,3):
    print("broken multiplication 1,1 * 3,3 = 3,3",a)
    return True

  a = space.Position2f(5,2) * space.Position2f(2,4)
  if a != space.Position2f(10,8):
    print("broken multiplication 5,2 * 2,4 = 10,8",a)
    return True

  a = space.Position2f(3,6)
  a *= space.Position2f(2,2)
  if a != space.Position2f(6,12):
    print("broken multiplication 3,6 * 2,2 = 6,12",a)
    return True

  a = space.Position2f(0,0)
  b = space.Position2f(2,2)
  if a.displacement(b) != space.Position2f(2,2):
    print("displacement is incorrect 2,2",a.displacement(b))
    return True

  a = space.Position2f(angle=0)
  if a != space.Position2f(1,0):
    print("angle interpreted to space.wrong 1,0",a)
    return True

  a = space.Position2f(angle=90)
  if a != space.Position2f(0,1):
    print("angle interpreted to space.wrong 0,1",a)
    return True

  a = space.Position2f(angle=45)
  if a != space.Position2f(0.707107,0.707107):
    print("angle interpreted to space.wrong 0.707107,0.707107",a)
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
Position2f_Test_req = []


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
  if a.displacement(b) != space.Position3f(2,2,2):
    print("displacement is incorrect 2,2,2",a.displacement(b))
    return True

  a = space.Position3f(angles=space.Position2f(0,0))
  if a != space.Position3f(0,0,1):
    print("angle interpreted incorrectly 0,0,1",a)
    return True

  a = space.Position3f(angles=space.Position2f(45,0))
  if a != space.Position3f(0,0.707107,0.707107):
    print("angle interpreted incorrectly 0,0.707107,0.707107",a)
    return True

  a = space.Position3f(angles=space.Position2f(0,45))
  if a != space.Position3f(0.707107,0,0.707107):
    print("angle interpreted incorrectly 0.707107,0,0.707107",a)
    return True

  a = space.Position3f()
  if a.angles != space.Position2f(0,0):
    print("angle for 0,0,0 is incorrect",a.angle)
    return True

  a = space.Position3f(1,0,0)
  if a.angles != space.Position2f(0,90):
    print("angles for 1,0,0 is incorrect",a.angles)
    return True

  a = space.Position3f(0,1,0)
  if a.angles != space.Position2f(90,0):
    print("angles for 0,1,0 is incorrect",a.angles)
    return True

  a = space.Position3f(0,0,1)
  if a.angles != space.Position2f():
    print("angles for 0,0,1 is incorrect",a.angles)
    return True

  a = space.Position3f(1,0,1)
  if a.angles != space.Position2f(0,45):
    print("angles for 1,0,1 is incorrect",a.angles)
    return True

  a = space.Position3f(0,1,1)
  if a.angles != space.Position2f(45,0):
    print("angles for 0,1,1 is incorrect",a.angles)
    return True

  a = space.Position3f(1,1,1)
  if a.angles != space.Position2f(45,45):
    print("angles for 0,0,1 is incorrect",a.angles)
    return True

  return False
Position3f_Test_req = [Position2f_Test]


def Positions_Test():
  pass
Positions_Test_req = [Position2f_Test,Position3f_Test]