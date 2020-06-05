""" Where's That Word? functions. """

# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
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

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them!

def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.

    >>> get_row_length('abcd\nefgh\nijkl\n')
    4
    """

    return len(puzzle.split('\n')[0])


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1


# Implement the required functions below.

def get_current_player(player_one_turn: bool) -> str:
    """Return 'player one' iff player_one_turn is True; otherwise, return
    'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """

    # Complete this function.
    if player_one_turn is True: 
        return P1
     
    return P2 

def get_winner(player_one_score:int, player_two_score:int) -> str:
    '''
    'return which player wins given who scores the most. If the score is tied return tie game'(check the statement)
    >>> get_winner(24, 22)
    'player one wins'
    >>> get_winner(23, 25)
    'player two wins'
    '''
    
    if player_one_score > player_two_score:
        return P1_WINS
    
    elif player_one_score < player_two_score:
        return P2_WINS
    
    return TIE
    
    
    
def reverse(word:str) -> str:
    
    '''
    return the reverse of the given word is inside the function reverse(word)
    >>> reverse(cat)
    'tac'
    '''
    return word[::-1]

    
def get_row(puzzle:str, row:int) -> int:
    """ return the word in the given row of the puzzle. 
    Given that the row length is the same.
    
    >>> get_row('abcd\nefgh\nnijkl\n', 1)
    efgh
    
    >>> get_row('cat\ndog\nyas\n' , 2)
    yas
    """

    string_index = row * (get_row_length(puzzle)+1)
    last_index = string_index + get_row_length(puzzle) 
    
    return puzzle[(string_index):(last_index)]


def get_factor(direction : str) -> int:
    '''
    return the factor value of direction
    
    >>> get_factor('up')
    4
    >>> get_factor('down')
    2
    '''
    if direction is FORWARD:
        return FORWARD_FACTOR
    elif direction is DOWN:
        return DOWN_FACTOR 
    elif direction is BACKWARD:
        return BACKWARD_FACTOR 
    elif direction is UP:
        return UP_FACTOR
        
    return 'invalid direction'




def get_points(direction:str, num_words_left:int ) -> int :
    '''
    Return the points that a player will receive 
    if a certain direction is chosen, 
    given the number of words left to be found.
    >>> get_factor('up')
    4
    >>> get_factor('down')
    2
    '''
    factor_point = get_factor(direction)
    
    if num_words_left >= THRESHOLD:
        return THRESHOLD * factor_point    
    elif num_words_left is 1:
        return ((2 * THRESHOLD - num_words_left) * factor_point) + BONUS
    
     
    return (2 * THRESHOLD - num_words_left) * factor_point
    

def check_guess(puzzle:str, direction:str, guess:str,
row_or_col_num:int, num_words_left:int) -> int:
    
    
    '''if direction is 'up' or direction is'down':
        col_num = row_or_col_num
    elif direction is 'forward' or direction is'backward':
        row = row_or_col_num'''
    
    if  direction == UP:
        col_num = row_or_col_num
        word = get_column(puzzle, col_num)
        text2 = reverse(word)
        if guess in text2:    
            return get_points(direction, num_words_left)
        else :
            return 0
    
        
    
    elif direction == DOWN :
        col_num = row_or_col_num
        text2 = get_column(puzzle, col_num)
        if contains (text2, guess):
            return get_points(direction, num_words_left)
        else:
            return 0
        
        
    
    elif direction == FORWARD :
        row = row_or_col_num
        text2 = get_row(puzzle, row)
        if guess in text2:
            return get_points(direction, num_words_left)
        else:
            return 0
        
    
    elif direction == BACKWARD :
        row = row_or_col_num
        word = get_row(puzzle, row)
        text1 = reverse(word)
        if contains (text2, guess):
            return get_points(direction, num_words_left)
        else:
            return 0
        
    return 'error'
        
    

        
    ''''if contains(text1, text2) is True:
        return get_points(direction, num_words_left)
    return 0'''
        
        

print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'forward', 'ijkl', 2, 4))
        
print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'forward', 'abcd', 0, 3))

print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'forward', 'efgh', 1, 2))
      
            
print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'backward', 'lkji', 2, 4))
        
print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'backward', 'dcba', 0, 3))

print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'backward', 'hgfe', 1, 2))

               
print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'backward', 'ijkl', 2, 4))
        
print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'backward', 'abcd', 0, 4))

print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'backward', 'efgh', 1, 4))


print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'down', 'cgko', 2, 4))
        
print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'down', 'aeim', 0, 3))

print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'down', 'bfjn', 1, 2))


print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'up', 'okgc', 2, 4))
        
print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'up', 'miea', 0, 3))

print(check_guess('abcd\nefgh\nijkl\nmnop\n', 'up', 'efgh', 1, 2))

    
pz =('abcd\nefgh\nijkl\nmnop\nqrst\n')
print("-----------MORE TEST---------")

print(check_guess(pz, 'forward', 'ijkl', 2, 4))
print(check_guess(pz, 'forward', 'cd', 0, 5))
print(check_guess(pz, 'forward', 'mno', 3, 1))
print(check_guess(pz, 'forward', 'uk', 0, 5))

print(check_guess(pz, 'up', 'njf', 1, 4))
print(check_guess(pz, 'up', 'mi', 0, 5))
print(check_guess(pz, 'up', 'okg', 2, 1))
print(check_guess(pz, 'up', 'uk', 3, 2))

print(check_guess(pz, 'backward ', 'kji', 2, 4))
print(check_guess(pz, 'backward ', 'dcba', 0, 5))
print(check_guess(pz, 'backward ', 'on', 3, 1))
print(check_guess(pz, 'backward ', 'uk', 0, 5))

print(check_guess(pz, 'down ', 'cg', 2, 4))
print(check_guess(pz, 'down ', 'ae', 0, 5))
print(check_guess(pz, 'down ', 'dhkp', 3, 1))
print(check_guess(pz, 'down ', 'uk', 0, 5))

         




