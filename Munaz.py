def get_row (puzzle:str, row:int) -> int:
""" return the word in the given row of the puzzle.
Given that the row length is the same.
>>> get_row('abcd\nefgh\nnijkl\n', 1)
efgh
>>> get_row('cat\ndog\nyasir\n' , 2)
yasir
"""
puzzle_adjusted = puzzle.strip().split('\n')
string_index = (row * get_row_length(puzzle))
last_index = string_index + get_row_length(puzzle)
return puzzle_adjusted[string_index:last_index]
