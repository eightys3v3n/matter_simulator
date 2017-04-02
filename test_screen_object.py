import unittest
from pyglet import gl
from space import Position3f
from screen_object import ScreenObject
from particle import Particle
import screen_object


class TestScreenObject(unittest.TestCase):
  def test___init__point(self):
    position = Position3f(1,4,1)
    colour = [254.0,254.0,254.0]
    so = ScreenObject("point",position=position,colour=colour,headless=True)
    self.assertEqual(so.type,"point")
    self.assertEqual(so.max_points,1)
    self.assertEqual(so.vertices,[position])
    self.assertEqual(so.vertices_colour,[colour])


  def test___init__rectangle(self):
    p = Position3f(1,4,1)
    s = Position3f(0,6,3)
    p2 = p + s
    colour = [254.0,254.0,254.0]
    so = ScreenObject("rectangle",position=p,size=s,colour=colour,headless=True)
    self.assertEqual(so.type,"rectangle")
    self.assertEqual(so.max_points,4)
    self.assertEqual(so.size,s)
    self.assertEqual(so.vertices_colour,[
      colour,colour,colour,colour
    ])


  def test___init__sphere(self):
    p = Position3f(1,3,2)
    r = 2.4
    colour = [254.0,254.0,254.0]
    so = ScreenObject("sphere",position=p,radius=r,colour=colour,headless=True)
    self.assertEqual(so.type,"sphere")
    self.assertEqual(so.max_points,1)
    self.assertEqual(so.radius,r)


  def test_generate_rectangle(self):
    # rectangle in y,z
    p = Position3f(1,4,1)
    s = Position3f(0,5,7)
    p2 = p + s
    so = ScreenObject("rectangle",position=p,size=s)
    self.assertListEqual(so.vertices,[
      Position3f(p.x,p.y-p2.y/2,p.z-p2.z/2),
      Position3f(p.x,p.y+p2.y/2,p.z-p2.z/2),
      Position3f(p.x,p.y+p2.y/2,p.z+p2.z/2),
      Position3f(p.x,p.y-p2.y/2,p.z+p2.z/2)
    ])

    # rectangle in x,z
    p = Position3f(1,4,1)
    s = Position3f(6,0,7)
    p2 = p + s
    so = ScreenObject("rectangle",position=p,size=s)
    self.assertListEqual(so.vertices,[
      Position3f(p.x-p2.x/2,p.y,p.z+p2.z/2),
      Position3f(p.x-p2.x/2,p.y,p.z-p2.z/2),
      Position3f(p.x+p2.x/2,p.y,p.z-p2.z/2),
      Position3f(p.x+p2.x/2,p.y,p.z+p2.z/2)
    ])

    # rectangle in x,y
    p = Position3f(1,4,1)
    s = Position3f(6,5,0)
    p2 = p + s
    so = ScreenObject("rectangle",position=p,size=s)
    self.assertListEqual(so.vertices,[
      Position3f(p.x-p2.x/2,p.y-p2.y/2,p.z),
      Position3f(p.x-p2.x/2,p.y+p2.y/2,p.z),
      Position3f(p.x+p2.x/2,p.y+p2.y/2,p.z),
      Position3f(p.x+p2.x/2,p.y-p2.y/2,p.z)
    ])



  def test_update_from_particle(self):
    so = ScreenObject("sphere",position=Position3f(),radius=1,headless=True)
    p = Particle()
    p.mass = 100
    p.density = 2.6808
    so.update_from_particle(p)
    self.assertEqual(round(so.radius,3),2.073)