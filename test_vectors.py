import unittest
import utils
from space import Vector3f,Position3f,Position2f


class TestVector3f(unittest.TestCase):
  def test___init__(self):
    a = Vector3f()
    self.assertEqual(a.origin,Position3f())
    self.assertEqual(a.destination,Position3f())

    with self.assertRaises(TypeError):
      Vector3f(1)

    with self.assertRaises(TypeError):
      Vector3f(1,1)

    with self.assertRaises(TypeError):
      Vector3f(Position3f(),0)

    with self.assertRaises(TypeError):
      Vector3f(Position3f(),Position3f(),1)

    with self.assertRaises(Exception):
      Vector3f(0,0,0,0,0)

    with self.assertRaises(Exception):
      Vector3f(origin=Position3f(),abc=1)

    with self.assertRaises(TypeError):
      Vector3f(origin=1)


    a = Vector3f(Position3f(1,1,1),Position3f(-1,-1,-1))
    self.assertEqual(a.destination,Position3f(-1,-1,-1))
    self.assertEqual(a.origin,Position3f(1,1,1))

    a = Vector3f(Position3f(1,1,1))
    self.assertEqual(a.destination,Position3f(1,1,1))
    self.assertEqual(a.origin,Position3f())

    a = Vector3f(origin=Position3f(1,1,1))
    self.assertEqual(a.destination,Position3f())
    self.assertEqual(a.origin,Position3f(1,1,1))

    a = Vector3f(origin=Position3f(1,1,1),destination=Position3f(-1,-1,-1))
    self.assertEqual(a.destination,Position3f(-1,-1,-1))
    self.assertEqual(a.origin,Position3f(1,1,1))

    a = Vector3f(1,1,1)
    self.assertEqual(a.destination,Position3f(1,1,1))
    self.assertEqual(a.origin,Position3f())

    a = Vector3f(1,1,1,-1,-1,-1)
    self.assertEqual(a.destination,Position3f(-1,-1,-1))
    self.assertEqual(a.origin,Position3f(1,1,1))


  def test___str__(self):
    a = Vector3f()
    a.origin      = Position3f(0,0,0)
    a.destination = Position3f(1,1,1)
    self.assertEqual(a.__repr__(),"(0.0,0.0,0.0)->(1.0,1.0,1.0)")


  def test___repr__(self):
    a = Vector3f()
    a.origin      = Position3f(0,0,0)
    a.destination = Position3f(1,1,1)
    self.assertEqual(a.__repr__(),"(0.0,0.0,0.0)->(1.0,1.0,1.0)")


  def test___eq__(self):
    self.assertTrue(
      Vector3f(Position3f(1,1,1),Position3f()) ==
      Vector3f(Position3f(1,1,1),Position3f())
    )

    self.assertFalse(
      Vector3f(Position3f(2,1,1),Position3f()) ==
      Vector3f(Position3f(1,1,1),Position3f())
    )

    self.assertFalse(
      Vector3f(Position3f(),Position3f(1,1,1)) ==
      Vector3f(Position3f(),Position3f())
    )

    self.assertTrue(
      Vector3f(Position3f(),Position3f(1,1,1)) ==
      Vector3f(Position3f(),Position3f(1,1,1))
    )

    self.assertFalse(
      Vector3f(Position3f(),Position3f(1,1,1)) ==
      Vector3f(Position3f(1,1,1),Position3f())
    )

    self.assertTrue(
      Vector3f(Position3f(2,2,2),Position3f(1,1,1)) ==
      Vector3f(Position3f(2,2,2),Position3f(1,1,1))
    )

    self.assertFalse(Vector3f() == 1)


  def test___ne__(self):
    self.assertFalse(
      Vector3f(Position3f(1,1,1),Position3f()) !=
      Vector3f(Position3f(1,1,1),Position3f())
    )

    self.assertTrue(
      Vector3f(Position3f(2,1,1),Position3f()) !=
      Vector3f(Position3f(1,1,1),Position3f())
    )

    self.assertTrue(
      Vector3f(Position3f(),Position3f(1,1,1)) !=
      Vector3f(Position3f(),Position3f())
    )

    self.assertFalse(
      Vector3f(Position3f(),Position3f(1,1,1)) !=
      Vector3f(Position3f(),Position3f(1,1,1))
    )

    self.assertTrue(
      Vector3f(Position3f(),Position3f(1,1,1)) !=
      Vector3f(Position3f(1,1,1),Position3f())
    )

    self.assertFalse(
      Vector3f(Position3f(2,2,2),Position3f(1,1,1)) !=
      Vector3f(Position3f(2,2,2),Position3f(1,1,1))
    )

    self.assertTrue(Vector3f() != 6)


  def test___add__(self):
    a = Vector3f(1,1,1)
    b = Vector3f(2,2,2)
    self.assertEqual(a+b,Vector3f(3,3,3))

    a = Vector3f(1,1,1,4,4,4)
    b = Vector3f(2,2,2)
    self.assertEqual(a+b,Vector3f(1,1,1,6,6,6))


  def test___iadd__(self):
    init = Vector3f()
    res = init
    res += Vector3f(3,3,3,1,1,1)

    self.assertIs(res,init,msg="in-place addition isn't changing the original")
    self.assertEqual(res,Vector3f(3,3,3,1,1,1))


  def test___sub__(self):
    a = Vector3f(1,1,1,3,3,3)
    b = Vector3f(2,2,2,1,1,1)
    self.assertEqual(a-b,Vector3f(-1,-1,-1,2,2,2))

    a = Vector3f(1,1,1,4,4,4)
    b = Vector3f(1,1,1,3,3,3)
    self.assertEqual(a-b,Vector3f(0,0,0,1,1,1))


  def test___isub__(self):
    init = Vector3f()
    res = init
    res -= Vector3f(2,2,2,1,1,1)

    self.assertIs(res,init,msg="in-place subtraction isn't changing the original")
    self.assertEqual(res,Vector3f(-2,-2,-2,-1,-1,-1))


  def test___mul__(self):
    res = Vector3f(1,1,1,3,5,1)
    self.assertEqual(res*5,Vector3f(1,1,1,15,25,5))


  def test___imul__(self):
    init = Vector3f(1,1,1,3,1,2)
    res = init
    res *= 4

    self.assertIs(res,init,msg="in-place multiplication isn't changing the original")
    self.assertEqual(res,Vector3f(1,1,1,12,4,8))


  def test___truediv__(self):
    ret = Vector3f(1,1,1,9,9,9)
    self.assertEqual(ret/3,Vector3f(1,1,1,3,3,3),msg="division isn't working correctly")


  def test___itruediv__(self):
    init = Vector3f(1,1,1,9,9,9)
    ret = init
    ret /= 3

    self.assertIs(ret,init,msg="in-place division isn't changing the original")
    self.assertEqual(ret,Vector3f(1,1,1,3,3,3),msg="in-place division isn't working correctly")


  def test_from_zero(self):
    self.assertEqual(Vector3f(1,1,1,3,3,3).from_zero,Vector3f(2,2,2))
    self.assertEqual(Vector3f(-1,-1,-1,3,3,3).from_zero,Vector3f(4,4,4))


  def test_array(self):
    self.assertEqual(Vector3f(1,1,1,3,3,3).array,[1,1,1,3,3,3])


  def test_magnitude(self):
    self.assertEqual(Vector3f(3,3,3).magnitude,5.196152)


  def test_direction(self):
    self.assertEqual(Vector3f(1,1,1,3,3,3).from_zero,Vector3f(2,2,2))
    self.assertEqual(Vector3f(-1,-1,-1,3,3,3).from_zero,Vector3f(4,4,4))


  def test_angles(self):
    self.assertEqual(Vector3f(1,1,1).angles,Position2f(45,45))



if __name__ == '__main__':
  unittest.main()