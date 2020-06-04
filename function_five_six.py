def get_factor(direction : str) -> int:
  if direction == FORWARD:
    return FORWARD_FACTOR 
  elif direction == DOWN:
    return DOWN_FACTOR 
  elif direction == BACKWARD:
    return BACKWARD_FACTOR 
  elif direction == UP:
    return UP_FACTOR 
  else:
    return 'invalid direction'
