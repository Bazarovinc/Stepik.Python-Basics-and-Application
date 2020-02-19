def closest_mod_5(x):
  y = x
  while True:
      if y % 5 == 0 and y >= x:
          break
      y +=1
  return y