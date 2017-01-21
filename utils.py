# Utils File
# this file is for stuff that isn't physics, but doesn't fit in the other files


def Map(v,mn,mx,nmn,nmx):
  r = v - mn
  r /= mx - mn
  r *= nmx - nmn
  r += nmn
  return r