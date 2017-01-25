from test import Tests
from time import sleep
from position import Position2f,Position3f
import particle,position,screen_object,utils,view








def Map():
  r = utils.Map(5,0,10,0,100)
  if r != 50:
    print("map(5,1,10,1,100 should be 50",r)
    return True

  return False
tests.new(Map)


def Position2f_():
  a = Position2f()
  b = Position2f()
  if a != b:
    print("two equal positions are not equal")
    return True

  b = Position2f(1,1)
  if a == b:
    print("two different positions are equal")
    return True

  a += b
  if a != Position2f(1,1):
    print("didn't do += correctly",a)
    return True

  if a+b != Position2f(2,2):
    print("didn't add correctly",a+b)
    return True

  a = Position2f(1,1) * Position2f(3,3)
  if a != Position2f(3,3):
    print("broken multiplication 1,1 * 3,3 = 3,3",a)
    return True

  a = Position2f(5,2) * Position2f(2,4)
  if a != Position2f(10,8):
    print("broken multiplication 5,2 * 2,4 = 10,8",a)
    return True

  a = Position2f(3,6)
  a *= Position2f(2,2)
  if a != Position2f(6,12):
    print("broken multiplication 3,6 * 2,2 = 6,12",a)
    return True

  a = Position2f(0,0)
  b = Position2f(2,2)
  if a.displacement(b) != Position2f(2,2):
    print("displacement is incorrect 2,2",a.displacement(b))
    return True

  a = Position2f(angle=0)
  if a != Position2f(1,0):
    print("angle interpreted to position wrong 1,0",a)
    return True

  a = Position2f(angle=90)
  if a != Position2f(0,1):
    print("angle interpreted to position wrong 0,1",a)
    return True

  a = Position2f(angle=45)
  if a != Position2f(0.707107,0.707107):
    print("angle interpreted to position wrong 0.707107,0.707107",a)
    return True

  a = Position2f()
  if a.angle != 0.0:
    print("angle for 0,0 is incorrect",a.angle)
    return True

  a = Position2f(1,1)
  if a.angle != 45.0:
    print("angle for 1,1 is incorrect",a.angle)
    return True

  a = Position2f(0,1)
  if a.angle != 90.0:
    print("angle for 0,1 is incorrect",a.angle)
    return True

  a = Position2f(1,0)
  if a.angle != 0.0:
    print("angle for 1,0 is incorrect",a.angle)
    return True

  return False
tests.new(Position2f_)


def Position3f_():
  a = Position3f(0,0,0)
  b = Position3f(0,0,0)
  if a != b:
    print("two equal positions are not equal")
    return True

  b = Position3f(1,1,1)
  if a == b:
    print("two different positions are equal")
    return True

  a += b
  if a != Position3f(1,1,1):
    print("didn't do += correctly",a)
    return True

  if a+b != Position3f(2,2,2):
    print("didn't add correctly",a+b)
    return True

  a = Position3f(1.5,2,4) * Position3f(5,2,1)
  if a != Position3f(7.5,4,4):
    print("broken multiplication 1.5,2,4 * 5,2,1 = 7.5,4,4",a)
    return True

  a = Position3f(3,6,9)
  a *= Position3f(2,0.5,3)
  if a != Position3f(6,3,27):
    print("broken multiplication 3,6,9 * 2,0.5,3 = 6,3,27",a)
    return True

  a = Position3f(0,0,0)
  b = Position3f(2,2,2)
  if a.displacement(b) != Position3f(2,2,2):
    print("displacement is incorrect 2,2,2",a.displacement(b))
    return True

  a = Position3f(angles=Position2f(0,0))
  if a != Position3f(0,0,1):
    print("angle interpreted incorrectly 0,0,1",a)
    return True

  a = Position3f(angles=Position2f(45,0))
  if a != Position3f(0,0.707107,0.707107):
    print("angle interpreted incorrectly 0,0.707107,0.707107",a)
    return True

  a = Position3f(angles=Position2f(0,45))
  if a != Position3f(0.707107,0,0.707107):
    print("angle interpreted incorrectly 0.707107,0,0.707107",a)
    return True

  a = Position3f()
  if a.angles != Position2f(0,0):
    print("angle for 0,0,0 is incorrect",a.angle)
    return True

  a = Position3f(1,0,0)
  if a.angles != Position2f(0,90):
    print("angles for 1,0,0 is incorrect",a.angles)
    return True

  a = Position3f(0,1,0)
  if a.angles != Position2f(90,0):
    print("angles for 0,1,0 is incorrect",a.angles)
    return True

  a = Position3f(0,0,1)
  if a.angles != Position2f():
    print("angles for 0,0,1 is incorrect",a.angles)
    return True

  a = Position3f(1,0,1)
  if a.angles != Position2f(0,45):
    print("angles for 1,0,1 is incorrect",a.angles)
    return True

  a = Position3f(0,1,1)
  if a.angles != Position2f(45,0):
    print("angles for 0,1,1 is incorrect",a.angles)
    return True

  a = Position3f(1,1,1)
  if a.angles != Position2f(45,45):
    print("angles for 0,0,1 is incorrect",a.angles)
    return True

  return False
tests.new(Position3f_,[Position2f])


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

  if a.angles != Position2f(45.0,45.0):
    print("incorrect angles 45,45",a.angles)
    return True

  a.direction.y = 0
  if a.angles != Position2f(0.0,45.0):
    print("incorrect angles 0,45",a.angles)
    return True

  a.direction.y = 1
  a.direction.x = 0
  if a.angles != Position2f(45.0,0.0):
    print("incorrect angles 45,0",a.angles)
    return True

  return False
tests.new(Vector3f)


def ScreenObject():
  try:
    o = screen_object.ScreenObject("Point",Position3f())
    if o.type != "point":
      print("didn't set ScreenObject.type correctly on initialization")
      return True

    if o.vertices != [Position3f()]:
      print("didn't set ScreenObject.vertices correctly on initialization")
      return True
  except Exception as e:
    print("failed to create a point screen object")
    print(e)
    return True

  try:
    o = screen_object.ScreenObject("Point",Position3f(10,10,10))
    if o.type != "point":
      print("didn't set ScreenObject.type correctly on initialization")
      return True

    if o.vertices != [Position3f(10,10,10)]:
      print("didn't set ScreenObject.vertices to 10,10,10",o.vertices)
      return True
  except Exception as e:
    print("failed to create a point screen object")
    print(e)
    return True

  return False
tests.new(ScreenObject,[Position3f])


def View():
  v = view.View()

  v.move(1,0,0)
  if v.position != Position3f(1,0,0):
    print("didn't move correctly on x",v.position)
    return True

  v.move(0,1,0)
  if v.position != Position3f(1,1,0):
    print("didn't move correctly on x",v.position)
    return True

  v.move(0,0,1)
  if v.position != Position3f(1,1,1):
    print("didn't move correctly on x",v.position)
    return True

  v.position = Position3f()
  v.heading = Position3f()
  v.look(angle=Position2f(45,0))
  if v.heading != Position3f(0,0.707107,0.707107):
    print("not looking correctly for angles 45,0",v.heading)
    return True

  v.position = Position3f()
  v.heading = Position3f()
  v.look(angle=Position2f(-45,0))
  if v.heading != Position3f(0,-0.707107,0.707107):
    print("not looking correctly for angles -45,0",v.heading)
    return True

  v.position = Position3f()
  v.heading = Position3f(10,10,10)
  v.look(angle=Position2f(-45,0))
  if v.heading != Position3f(17.07107,10,17.07107):
    print("not looking correctly for angles -45,0 from 10,10,10",v.heading)
    return True

  return False
tests.new(View,[Position3f])


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