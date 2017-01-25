import test_positions
import space


def Equal_Test():
  a = vectors.Vector3f(position.Position3f(1,1,1))
  b = vectors.Vector3f(position.Position3f(1,1,1))
  if a != b:
    print("two equal vectors are not equal")
    return True

  b = vectors.Vector3f(position.Position3f(-1,-1,-1))
  if a == b:
    print("two different vectors are equal")
    return True


  if a.angles != position.Position2f(45.0,45.0):
    print("incorrect angles 45,45",a.angles)
    return True

  a = vectors.Vector3f(position.Position3f(1,1,1))
  b = vectors.Vector3f(position.Position3f(1,1,1))
  a.direction.y = 0
  if a.angles != position.Position2f(0.0,45.0):
    print("incorrect angles 0,45",a.angles)
    return True

  a.direction.y = 1
  a.direction.x = 0
  if a.angles != position.Position2f(45.0,0.0):
    print("incorrect angles 45,0",a.angles)
    return True

  return False
Equal_Test = []


def Vector3f_Test():
  pass
Vector3f_Test_req = [test_positions.Positions_Test,Equal_Test]


def Vectors_Test():
  pass
Vectors_Test_req = [Vector3f_Test]