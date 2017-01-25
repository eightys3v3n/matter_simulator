from particle import Particle


def apply_gravity(particles):
  for particle in particles:
    for particle2 in particles:
      if particle == particle2:
        continue

      # particle is the Particle you are calculating acceleration for
      # particle2 is the Particle that is affecting particle
