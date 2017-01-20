import variables

class Material:
  def __init__(self,mass=0,density=0):
    self.mass = mass
    self.density = density


  def get_radius(self):
    v = self.mass * self.density
    r = pow(4.0/3.0 * variables.pi * v,1.0/3.0)
    return r