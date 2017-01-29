import unittest
from view import View
from space import Position3f,Position2f


class TestView(unittest.TestCase):
  def test___init__(self):
    v = View()
    self.assertEqual(v.position,Position3f())
    self.assertEqual(v.direction,Position2f())


  def test_move(self):
    v = View()

    v.move(1,0,0)
    self.assertEqual(v.position,Position3f(1,0,0))

    v.move(1,1,0.5)
    self.assertEqual(v.position,Position3f(2,1,0.5))

    v.position = Position3f()
    v.direction.y = 90.0
    v.move(1,0,0)
    self.assertEqual(v.position,Position3f(0,0,1))

    v.position = Position3f()
    v.direction.x = 90.0
    v.move(1,0,0)
    self.assertEqual(v.position,Position3f(0,0,1))


  def test_look(self):
    v = View()

    v.look(Position2f(10.0,90.0))
    self.assertEqual(v.direction,Position2f(10,90))

    v.direction = Position2f()
    v.look(Position2f(91.0,361.0))
    self.assertEqual(v.direction,Position2f(90,1))

    v.direction = Position2f()
    v.look(Position2f(-91.0,-361.0))
    self.assertEqual(v.direction,Position2f(-90,-1))