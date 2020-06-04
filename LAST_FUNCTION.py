check_guess(puzzle:str, direction:str, guessed_word:str, location:int, words_left:int) -> int:

 '''
like first your code will check if guessed_word 
inside puzzle using contains function (helper function ) 
step 2 if it's there then check which row or column 
it was in and in which direction? 
if row col number and directions matches users
 given direction and row col number 
then return result else return 0
'''



check_guess (puzzle :str, guessed_word :str)

print  (print_puzzle(puzzle))
if contains (puzzle, guessed_word ) == TRUE:
  print  ('yes it worked')
else:
  print  ("nope, not eorking")

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



def get_num_rows(puzzle: str) -> int:
    """Return the number of rows in puzzle.

    puzzle is a game board.

    >>> get_num_rows('abcd\nefgh\nijkl\n')
    3
    """

    return puzzle.count('\n')


def get_num_cols(puzzle: str) -> int:
    """Return the number of columns in puzzle.

    puzzle is a game board.

    >>> get_num_cols('abcd\nefgh\nijkl\n')
    4

    """

    return puzzle.index('\n')


def print_puzzle(puzzle: str) -> None:
    """Print the puzzle with row and column numbers and two spaces between
    each letter.

    """

    # Split puzzle into rows and get dimensions.
    puzzle_rows = puzzle.strip().split('\n')
    num_rows = get_num_rows(puzzle)
    num_columns = get_num_cols(puzzle)

    # Print the column headings.
    print('   ', end='')
    for col_number in range(num_columns):
        print(col_number, ' ', end='')

    print()

    # Print each row number and row.
    for row_number in range(num_rows):
        print(row_number, end='  ')
        print('  '.join(puzzle_rows[row_number]))

    print()


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1

pz= 'abcd\nefgh\nijkl\n'
print  (print_puzzle('abcd\nefgh\nijkl\n')
print  (contains (pz, jk))
