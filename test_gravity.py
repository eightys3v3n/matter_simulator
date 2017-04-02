import unittest
import gravity
from particle import Particle
from space import Vector3f,Position3f


class TestGravity(unittest.TestCase):
  def test_gravity_effect(self):
    self.assertEqual(gravity.gravity_effect(10000,Vector3f(1,1,1)),Vector3f(1.2836421e-7,1.2836421e-7,1.2836421e-7))


  def test_gravity_between_particles(self):
    p1 = Particle()
    p1.mass = 10000
    p2 = Particle()
    p2.position = Position3f(1,1,1)
    res = gravity.gravity_between_particles(p1,p2)
    self.assertEqual(res,Vector3f(1.2836421e-7,1.2836421e-7,1.2836421e-7))


  def test_gravity(self):
    particles = []
    a = Particle(mass=10000)
    a.mass = 10000
    particles.append(a)
    b = Particle(position=Position3f(1,1,1))
    particles.append(b)

    gravity.gravity(particles)
    a = particles[0].acceleration
    self.assertEqual(a,Vector3f(1.2836421e-7,1.2836421e-7,1.2836421e-7))