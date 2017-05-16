import unittest
from particle import Particle
from space import Position3f,Vector3f


class TestParticle(unittest.TestCase):
  def test___init__(self):
    p = Particle(mass=100,density=2.6808)
    self.assertEqual(p.mass,100)
    self.assertEqual(p.density,2.6808)
    self.assertEqual(p.position,Position3f())
    self.assertEqual(p.velocity,Vector3f())
    self.assertEqual(p.acceleration,Vector3f())


  def test_radius(self):
    p = Particle(mass=100,density=2.6808)
    self.assertEqual(round(p.radius,3),4.0)


  def test_displacement(self):
    p1 = Particle()
    p2 = Particle()
    p2.position = Position3f(3,5,2)
    d = p1.displacement(p2)
    self.assertEqual(d,Vector3f(0,0,0,3,5,2))


  def test_update(self):
    p = Particle()
    p.acceleration = Vector3f(1.5,1,0.5)
    p.update()
    self.assertEqual(p.velocity,Vector3f(0,0,0,1.5,1,0.5))
    self.assertEqual(p.position,Position3f(1.5,1,0.5))
    self.assertEqual(p.acceleration,Vector3f(1.5,1,0.5))

    p.update()
    self.assertEqual(p.velocity,Vector3f(0,0,0,3,2,1))
    self.assertEqual(p.position,Position3f(4.5,3,1.5))
    self.assertEqual(p.acceleration,Vector3f(1.5,1,0.5))


  def test___eq__(self):
    p = Particle(100)
    p1 = Particle(100)

    self.assertTrue(p==p1)

    p1.position.x = 3
    self.assertFalse(p==p1)