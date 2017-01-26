import test_positions
import space


def V3f_Equals_Test():
  a = space.Vector3f(space.Position3f(1,1,1))
  b = space.Vector3f(space.Position3f(1,1,1))
  if a != b:
    print("two equal vectors are not equal")
    return True

  b = space.Vector3f(space.Position3f(-1,-1,-1))
  if a == b:
    print("two different vectors are equal")
    return True

  return False
V3f_Equals_Test_req = []


def V3f_Magnitude_Test():
  a = space.Vector3f(space.Position3f(0,0,0),space.Position3f(10,10,10))
  print(a.magnitude)
  if a.magnitude != 17.320508:
    print("incorrect magnitude for vector 10,10,10",a.magnitude)
    return True

  a = space.Vector3f(space.Position3f(0,0,0),space.Position3f(1,1,1))
  a.magnitude = 17.320508
  if a.destination != space.Position3f(10,10,10):
    print("incorrectly extended vector by setting magnitude 10,10,10",a.destination)
    return True

  return False
V3f_Magnitude_Test_req = []


def V3f_AddTo_Test():
  a = space.Vector3f()
V3f_AddTo_Test_req = []

def Vector3f_Test():
  pass
Vector3f_Test_req = [test_positions.Positions_Test,V3f_Equals_Test,V3f_AddTo_Test,V3f_Magnitude_Test]


def Vectors_Test():
  pass
Vectors_Test_req = [Vector3f_Test]