import unittest
import utils
from space import Position3f,Position2f


class TestPosition2f(unittest.TestCase):
  def test___init__(self):
    res = Position2f()
    self.assertEqual(res.x,0.0)
    self.assertEqual(res.y,0.0)

    res = Position2f(1,3)
    self.assertEqual(res.x,1.0)
    self.assertEqual(res.y,3.0)

    res = Position2f(x=1,y=3)
    self.assertEqual(res.x,1.0)
    self.assertEqual(res.y,3.0)

    res = Position2f(angle=45)
    self.assertEqual(res.x,0.707107)
    self.assertEqual(res.y,0.707107)

    res = Position2f(angle=0)
    self.assertEqual(res.x,1.0)
    self.assertEqual(res.y,0.0)

    res = Position2f(angle=90)
    self.assertEqual(res.x,0.0)
    self.assertEqual(res.y,1.0)


class TestPosition3f(unittest.TestCase):
  def test___init__(self):
    res = Position3f()
    self.assertEqual(res.x,0.0)
    self.assertEqual(res.y,0.0)
    self.assertEqual(res.z,0.0)

    res = Position3f(3,1,4)
    self.assertEqual(res.x,3.0)
    self.assertEqual(res.y,1.0)
    self.assertEqual(res.z,4.0)

    res = Position3f(x=3,y=1,z=5)
    self.assertEqual(res.x,3.0)
    self.assertEqual(res.y,1.0)
    self.assertEqual(res.z,5.0)


  def test___str__(self):
    self.assertEqual(Position3f(3,1,4).__str__(),"(3.0,1.0,4.0)")


  def test___repr__(self):
    self.assertEqual(Position3f(1,3,5).__repr__(),"(1.0,3.0,5.0)")


  def test___eq__(self):
    self.assertTrue(Position3f(1,1,1) == Position3f(1,1,1))
    self.assertTrue(Position3f(4.0,1,1) == Position3f(4.0,1,1))
    self.assertFalse(Position3f(0,1,1) == Position3f(1,1,1))


  def test___ne__(self):
    self.assertTrue(Position3f(1,0,0) != Position3f(1,1,1))
    self.assertFalse(Position3f(1,1,1) != Position3f(1,1,1))


  def test___add__(self):
    res = Position3f(0,0,0) + Position3f(0,0,0)
    self.assertEqual(res,Position3f(0,0,0))

    res = Position3f(0,0,0) + Position3f(0,1,0)
    self.assertEqual(res,Position3f(0,1,0))

    res = Position3f(-1,3,-2) + Position3f(4,-2,5)
    self.assertEqual(res,Position3f(3,1,3))

    a = Position3f(1,1,1)
    b = Position3f(-2,-2,-2)
    res = a+b
    self.assertIsNot(res,a)
    self.assertIsNot(res,b)


  def test___iadd__(self):
    init = Position3f()
    res = init
    res += Position3f(1,1,1)

    self.assertIs(res,init,msg="in-place addition isn't changing the original")
    self.assertEqual(res,Position3f(1,1,1),msg="in-place addition isn't doing addition correctly")


  def test___sub__(self):
    res = Position3f(3,3,3) - Position3f(1,1,1)
    self.assertEqual(res,Position3f(2,2,2))

    res = Position3f(4,6,1) - Position3f(2,1,-4)
    self.assertEqual(res,Position3f(2,5,5))

    a = Position3f(1,1,1)
    b = Position3f(-1,-1,-1)
    res = a-b
    self.assertIsNot(res,a)
    self.assertIsNot(res,b)


  def test___isub__(self):
    init = Position3f()
    res = init
    res -= Position3f(-5,-3,-1)

    self.assertIs(res,init,msg="in-place subtraction isn't changing the original")
    self.assertEqual(res,Position3f(5,3,1),msg="in-place subtraction isn't doing subtraction correctly")


  def test___mul__(self):
    res = Position3f(2,0.5,3) * Position3f(3,4,3)
    self.assertEqual(res,Position3f(6,2,9))

    res = Position3f(2,0.5,3) * Position3f(0,0,0)
    self.assertEqual(res,Position3f(0,0,0))

    res = Position3f(0,0,0) * Position3f(0,0,0)
    self.assertEqual(res,Position3f(0,0,0))

    res = Position3f(0,0,0) * 0
    self.assertEqual(res,Position3f(0,0,0))

    res = Position3f(2,3,5) * 2
    self.assertEqual(res,Position3f(4,6,10))

    res = Position3f(2,3,2) * 3.0
    self.assertEqual(res,Position3f(6,9,6))


    a = Position3f(2,2,2)
    b = Position3f(3,1,4)
    res = a*b
    self.assertIsNot(res,a)
    self.assertIsNot(res,b)


  def test___imul__(self):
    init = Position3f(2,2,2)
    res = init
    res *= Position3f(3,1,5)

    self.assertIs(res,init,msg="in-place multiplication isn't changing the original")
    self.assertEqual(res,Position3f(6,2,10),msg="in-place multiplication isn't doing multiplication correctly")

    init = Position3f(2,2,2)
    res = init
    res *= 4

    self.assertIs(res,init,msg="in-place multiplication isn't changing the original")
    self.assertEqual(res,Position3f(8,8,8),msg="in-place multiplication isn't doing multiplication correctly")

    init = Position3f(2,2,2)
    res = init
    res *= 0.5

    self.assertIs(res,init,msg="in-place multiplication isn't changing the original")
    self.assertEqual(res,Position3f(1,1,1),msg="in-place multiplication isn't doing multiplication correctly")


  def test___truediv__(self):
    ret = Position3f(9,9,9)
    self.assertEqual(ret/3,Position3f(3,3,3),msg="true division isn't working correctly")
    self.assertEqual(ret/2,Position3f(4.5,4.5,4.5),msg="true division isn't working correctly")


  def test___itruediv__(self):
    init = Position3f(9,9,9)
    res = init
    res /= 3
    self.assertIs(res,init,msg="in-place true division isn't changing the original")
    self.assertEqual(res,Position3f(3,3,3),msg="in-place division isn't working correctly")


  def test_displacement(self):
    a = Position3f()
    b = Position3f(1,1,1)
    r = a.displacement(b).direction.destination
    self.assertEqual(r,Position3f(1,1,1))

    a = Position3f(-1,-3,-1)
    b = Position3f(1,2,1)
    r = a.displacement(b).direction.destination
    self.assertEqual(r,Position3f(2,5,2))

    a = Position3f(1,1,1)
    b = Position3f(4,6,-3)
    r = a.displacement(b).direction.destination
    self.assertEqual(r,Position3f(3,5,-4))


  def test_array(self):
    self.assertEqual(Position3f(3,5,1).array, [3.0,5.0,1.0])


  def test_dot(self):
    with self.assertRaises(Exception):
      Position3f(3,3,3).dot(1)

    self.assertEqual(Position3f(3,4,3).dot(Position3f(2,.5,2)), 14)
    self.assertEqual(Position3f(0,0,0).dot(Position3f(2,.5,2)), 0.0)


  def test_self_dot(self):
    self.assertEqual(Position3f(3,3,3).self_dot, 27)
    self.assertEqual(Position3f(0,0,0).self_dot, 0.0)


if __name__ == '__main__':
  unittest.main()