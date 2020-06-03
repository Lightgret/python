
def get_row(puzzle: str, row_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'efgh'
    """

    puzzle_list = puzzle.strip().split('\n')
    row = ''
    for column in puzzle_list:
        row += col[row_num]

    return row


print(get_column('abcd\nefgh\nijkl\n', 1))

