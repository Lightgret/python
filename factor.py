UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

def get_factor(direction : str) -> int:
 if direction == FORWARD
  return FORWARD_FACTOR
 elseif direction == DOWN
  return DOWN_FACTOR 
 elseif direction == BACKWARD
  return BACKWARD_FACTOR 
 elseif direction == UP
  return UP_FACTOR
 else
  return 'invalid direction'
  
  
  
