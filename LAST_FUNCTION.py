check_guess(puzzle:str, direction:str, guessed_word:str, location:int, words_left:int) -> int:
 if guessed_word : 
  return points_earned
else:
  return 0

""" the helper function I may need
get puzzle row
get puzzle column 
get_directions
get_points


The first parameter represents the puzzle, 
the second represents a
direction (value of one of the constants UP , DOWN , FORWARD and
BACKWARD ), 
the third represents the guessed word, 
the fourth represents
the row or column number, and 
the fifth represents the number of words
left to be found before this guess. 

If this guessed word is found in this
puzzle at this location (row or column) and in this direction, return the
number of points earned for this guess. 
Otherwise, return 0. 

Hint: you will need to call on several helper functions (from above and
from the starter code).
eg
check_guess('abcd\nefgh\nijkl\nmnop\n', 'forward', 'efgh', 1, 3)
