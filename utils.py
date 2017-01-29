from random import random as _random
from space import Position3f


# Utils File
# this file is for stuff that isn't physics, but doesn't fit in the other files


def Map(value,value_min,value_max,return_min,return_max):
  ret = value - value_min
  ret /= value_max - value_min
  ret *= return_max - return_min
  ret += return_min

  if ret > return_max:
    return return_max
  elif ret < return_min:
    return return_min
  else:
    return ret


def Random(min=0.0,max=1.0):
  ret = _random()
  ret = Map(ret,0,1,min,max)
  return ret


def Random3f(x_range,y_range,z_range):
  if not isinstance(x_range,list):
    raise Exception("expected an x_range of [min,max]",x_range)

  if not isinstance(y_range,list):
    raise Exception("expected an y_range of [min,max]",y_range)

  if not isinstance(z_range,list):
    raise Exception("expected an z_range of [min,max]",z_range)

  ret = Position3f()
  ret.x = Map(random(),0,1,x_range[0],x_range[1])
  ret.y = Map(random(),0,1,y_range[0],y_range[1])
  ret.z = Map(random(),0,1,z_range[0],z_range[1])
  return ret