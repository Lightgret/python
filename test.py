
get_current_player(player:bool) -> str
Already Done
get_winner(player1:int, player2:int) -> str
If player1 > player2
return P1_WINS
elseif player1< player2
return P2_WINS
else
return TIE
reverse(word:str) -> str
Working on it
get_row(puzzle:str, row_num:int) -> str
Use helper function that will create pluzzel matrix
return another helper function
I'm trying it now… .
get_factor(direction : str) -> int
If direction == FORWARD
return 1
elseif direction == DOWN
return 2
elseif direction == BACKWARD
return 3
elseif direction == UP
return 4
else
return 'invalid direction'
Return the multiplicative factor
associated with this direction.
THRESHOLD IS OUR MIDDLE GROUND. lets assume we choose our middle ground to be no
5.
Now when game starts, if 5 or more then 5 words left to be found the we simlpy multiply
THRESHOLD * direction.
Lets suppose we need to find 7 words.

7 words left to find….
First word found in some direction .
Score = THRESHOLD * direction
6 words left to find….
Second word found in some direction
Score = THRESHOLD * direction
5 words left to find….
Third word found in some direction .
Score = THRESHOLD * direction
4 words left to find….
now that there are less than 5 words left to find we will change our calculation.
Fourth word found in some direction .
Score = (2*THRESHOLD - 4) * direction
3 words left to find….
Third word found in some direction .
Score = (2*THRESHOLD - 3) * direction
2 words left to find….
Second word found in some direction .
Score = (2*THRESHOLD - 2) * direction
1 words left to find….
Last word found in some direction .
Score = (2*THRESHOLD - 1) * direction + BONUS
0 words left to find….
Game end
Only the last word gets the bonus point.
get_points(direction:str, word_left: int) ->int
if word_left == 1
return (2*THRESHOLD - word_left) * direction + BONUS
elseif word_left >= THRESHOLD
return THRESHOLD * direction
else
return (2*THRESHOLD - word_left) * direction
