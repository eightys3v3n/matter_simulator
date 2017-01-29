import unittest
from random import random as _random
from utils import Map,Random


class TestMap(unittest.TestCase):
  def test_out_of_bounds(self):
    self.assertEqual(Map(-1,0,10,0,100),0.0)
    self.assertEqual(Map(11,0,10,0,100),100.0)


  def test_bottom(self):
    self.assertEqual(Map(1,1,5,1,100),1.0)
    self.assertEqual(Map(10,10,50.5,1,100),1.0)


  def test_middle(self):
    self.assertEqual(Map(5,0,10,0,100),50.0)
    self.assertEqual(Map(1,0,2,0,100),50.0)
    self.assertEqual(Map(0.5,0,1,0,100),50.0)
    self.assertEqual(Map(0.44,0,1,0,100),44.0)


  def test_top(self):
    self.assertEqual(Map(1,0,1,0,100),100.0)
    self.assertEqual(Map(10,0,10,0,100),100.0)
    self.assertEqual(Map(0.5,0,0.5,0,100),100.0)


class TestRandom(unittest.TestCase):
  def test_default(self):
    for i in range(20):
      r = Random()
      self.assertGreaterEqual(r,0.0)
      self.assertLessEqual(r,1.0)


  def test_range(self):
    min = round(_random() * 10,2)
    max = 0
    while max <= min:
      max = round(_random() * 100,2)

    for i in range(20):
      r = Random(min,max)
      self.assertGreaterEqual(r,min)
      self.assertLessEqual(r,max)


if __name__ == '__main__':
  unittest.main()