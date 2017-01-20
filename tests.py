from test import Tests
from time import sleep
import materials,space,screen_object,utils


tests = Tests()


def Map():
  r = utils.Map(5,0,10,0,100)
  if r != 50:
    print("map(5,1,10,1,100 should be 50",r)
    return True

  return False
tests.new(Map)


def Position3f():
  a = space.Position3f(0,0,0)
  b = space.Position3f(1,1,1)
  if a == b:
    print("two different positions are equal")
    return True

  b = space.Position3f(0,0,0)
  if a != b:
    print("two equal positions are not equal")
    return True

  return False
tests.new(Position3f)


def Vector3f():
  a = space.Vector3f(0,0,0,1,1,1)
  b = space.Vector3f(0,0,0,1,1,1)
  if a != b:
    print("two equal vectors are not equal")
    return True

  b = space.Vector3f(1,1,1,0,0,0)
  if a == b:
    print("two different vectors are equal")
    return True

  return False
tests.new(Vector3f)


def ScreenObject():
  try:
    o = screen_object.ScreenObject("Point",space.Position3f())
    if o.type != "Point":
      print("didn't set ScreenObject.type correctly on initialization")
      return True

    if o.vertices != [space.Position3f()]:
      print("didn't set ScreenObject.vertices correctly on initialization")
      return True
  except Exception as e:
    print("failed to create a point screen object")
    print(e)
    return True

  try:
    o = screen_object.ScreenObject("Point",space.Position3f(10,10,10))
    if o.type != "Point":
      print("didn't set ScreenObject.type correctly on initialization")
      return True

    if o.vertices != [space.Position3f(10,10,10)]:
      print("didn't set ScreenObject.vertices to 10,10,10",o.vertices)
      return True
  except Exception as e:
    print("failed to create a point screen object")
    print(e)
    return True

  return False
tests.new(ScreenObject,[Position3f])


def Material():
  m = materials.hydrogen
  if m.get_radius() != 2.5985180598166497:
    print("hydrogens radius is incorrect",m.get_radius())
    return True

  return False
tests.new(Material,[Position3f,Vector3f])


def Example():
  return None
tests.new(Example)