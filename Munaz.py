def get_row (puzzle:str, row:int) -> int:

string_index = row * (get_row_length(puzzle)+1)
last_index = string_index + get_row_length(puzzle)
return puzzle[string_index:last_index]
