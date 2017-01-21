import variables


# Material File
# this file is for all the functions and classes that store the information about materials
# these materials will be what move around the screen in clumps (spheres)


class Material:
  def __init__(self,mass=0,density=0):
    self.mass = mass
    self.density = density


  def get_radius(self):
    v = self.mass * self.density
    r = pow(4.0/3.0 * variables.pi * v,1.0/3.0)
    return r