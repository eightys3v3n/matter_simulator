def Map(v,mn,mx,nmn,nmx):
  r = v - mn
  r /= mx - mn
  r *= nmx - nmn
  r += nmn
  return r