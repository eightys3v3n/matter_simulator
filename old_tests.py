from time import sleep
import particle,position,screen_object,utils,view


def Map_Test():
  r = utils.Map(5,0,10,0,100)
  if r != 50:
    print("map(5,1,10,1,100 should be 50",r)
    return True

  return False
Map_Test_req = []





def ScreenObject_Test():
  try:
    o = screen_object.ScreenObject("Point",position.Position3f())
    if o.type != "point":
      print("didn't set ScreenObject.type correctly on initialization")
      return True

    if o.vertices != [position.Position3f()]:
      print("didn't set ScreenObject.vertices correctly on initialization")
      return True
  except Exception as e:
    print("failed to create a point screen object")
    print(e)
    return True

  try:
    o = screen_object.ScreenObject("Point",position.Position3f(10,10,10))
    if o.type != "point":
      print("didn't set ScreenObject.type correctly on initialization")
      return True

    if o.vertices != [position.Position3f(10,10,10)]:
      print("didn't set ScreenObject.vertices to 10,10,10",o.vertices)
      return True
  except Exception as e:
    print("failed to create a point screen object")
    print(e)
    return True

  return False
ScreenObject_Test_req = [Position3f_Test]


def View_Test():
  v = view.View()

  v.move(1,0,0)
  if v.position != position.Position3f(1,0,0):
    print("didn't move correctly on x",v.position)
    return True

  v.move(0,1,0)
  if v.position != position.Position3f(1,1,0):
    print("didn't move correctly on x",v.position)
    return True

  v.move(0,0,1)
  if v.position != position.Position3f(1,1,1):
    print("didn't move correctly on x",v.position)
    return True

  v.position = position.Position3f()
  v.heading = position.Position3f()
  v.look(angle=position.Position2f(45,0))
  if v.heading != position.Position3f(0,0.707107,0.707107):
    print("not looking correctly for angles 45,0",v.heading)
    return True

  v.position = position.Position3f()
  v.heading = position.Position3f()
  v.look(angle=position.Position2f(-45,0))
  if v.heading != position.Position3f(0,-0.707107,0.707107):
    print("not looking correctly for angles -45,0",v.heading)
    return True

  v.position = position.Position3f()
  v.heading = position.Position3f(10,10,10)
  v.look(angle=position.Position2f(-45,0))
  if v.heading != position.Position3f(17.07107,10,17.07107):
    print("not looking correctly for angles -45,0 from 10,10,10",v.heading)
    return True

  return False
View_Test_req = [Position3f_Test]


def Particle_Test():
  return None
Particle_Test_req = [Position3f_Test,Vector3f_Test]


def Example_Test():
  return None
Example_Test_req = []