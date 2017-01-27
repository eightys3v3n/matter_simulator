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


def V3f_AddTo_Test():
  a = space.Vector3f()
V3f_AddTo_Test_req = []


def V3f_Dot_Test():
  a = space.Vector3f(space.Position3f(2,3,7))
  b = space.Vector3f(space.Position3f(4,8,2))
  r = a.dot(b)
  if r != 46:
    print("dot product of two vectors is wrong, should be 46 is",r)
    return True

  return False
V3f_Dot_Test_req = []


def V3f_Multiply_Test():
  a = space.Vector3f(space.Position3f(2,2,2))
  r = a * 2
  if r != space.Vector3f(space.Position3f(4,4,4)):
    print(a," multiplied by 2 should be 4,4,4 but its ",r)
    return True

  return False
V3f_Multiply_Test_req = []


def V3f_Divide_Test():
  a = space.Vector3f(space.Position3f(9,9,9))
  r = a / 3
  if r != space.Vector3f(space.Position3f(3,3,3)):
    print("failed to divide 9,9,9 by 3, actually got ",r)
    return True

  return False
V3f_Divide_Test_req = []


def Vector3f_Test():
  pass
Vector3f_Test_req = [test_positions.Positions_Test,V3f_Equals_Test,V3f_AddTo_Test,V3f_Multiply_Test]


def Vectors_Test():
  pass
Vectors_Test_req = [Vector3f_Test]