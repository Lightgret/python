def get_points(direction:str, word_left: int) ->int:
 if word_left == 1:
  return (2*THRESHOLD - word_left) * direction + BONUS
 elif word_left >= THRESHOLD:
  return THRESHOLD * direction
 else:
  return (2*THRESHOLD - word_left) * direction
