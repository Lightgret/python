def get_points(direction:str, word_left: int) ->int:
 if word_left == 1:
  return (2*THRESHOLD - word_left) * get_factor(direction)+ BONUS
 elif word_left >= THRESHOLD:
  return THRESHOLD * get_factor(direction)
 else:
  return (2*THRESHOLD - word_left) * get_factor(direction)

print(get_points('up', 6))
print(get_points('up', 5))
print(get_points('up', 4))
print(get_points('up', 3))
print(get_points('up', 2))
print(get_points('up', 1))

print(get_points('down', 6))
print(get_points('down', 5))
print(get_points('down', 4))
print(get_points('down', 3))
print(get_points('down', 2))
print(get_points('down', 1))

print(get_points('forward', 6))
print(get_points('forward', 5))
print(get_points('forward', 4))
print(get_points('forward', 3))
print(get_points('forward', 2))
print(get_points('forward', 1))

print(get_points('backward', 6))
print(get_points('backward', 5))
print(get_points('backward', 4))
print(get_points('backward', 3))
print(get_points('backward', 2))
print(get_points('backward', 1))
