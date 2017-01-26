from particle import Particle


def calculate_gravity(p1,p2):
  #f = GMm/r^2
  force = Vector3f()
  magnitude = variables.G * p1.mass * p2.mass
  magnitude /= pow(p1.displacement(p2).magnitude,2)

  p1.magnitude = magnitude


def apply_gravity(particle,particles):
  for p in particles:
    particle.acceleration += calculate_gravity(particle,p1)


def gravity(particles):
  for particle in particles:
    apply_gravity(particle,particles)
