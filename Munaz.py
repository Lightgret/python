def get_row (puzzle:str, row:int) -> int:

string_index = row * (get_row_length(puzzle)+1)
last_index = string_index + get_row_length(puzzle)
return puzzle[string_index:last_index]




def check_guess(puzzle:str, direction:str, guess:str, row_or_col_num:int, num_words_left:int) -> int:

text1 = puzzle
if direction == 'up':
word = get_column(puzzle, col_num)
text2 = reverse(word)
if contains(text1, text2) is True and text2 == guess:
return get_points(direction, num_words_left)
return 0
elif direction == 'down':
text2 = get_column(puzzle, col_num)
if contains(text1, text2) is True and text2 == guess:
return get_points(direction, num_words_left)
return 0
elif direction == 'forward':
text2 = get_row(puzzle, row)
if contains(text1, text2) is True and text2 == guess:
return get_points(direction, num_words_left)
return 0
elif direction == 'backward':
word = get_row(puzzle, row)
text2 = reverse(word)
if contains(text1, text2) is True and text2 == guess:
return get_points(direction, num_words_left)
return 0
return 'invalid direction'
