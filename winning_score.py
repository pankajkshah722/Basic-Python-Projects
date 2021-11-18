## Canadian Computing Competition: 2019 Stage 1, Junior #1
"""
You record all of the scoring activity at a basketball game. 
Points are scored by a 3-point shot, a 2-point field goal, 
or a 1-point free throw.

You know the number of each of these types of scoring 
for the two teams: the Apples and the Bananas. Your 
job is to determine which team won, or if the game ended in a tie.
"""

## Input Specification
"""
The first three lines of input describe the scoring of the Apples, 
and the next three lines of input describe the scoring of the Bananas. 
For each team, the first line contains the number of successful 3-point
shots, the second line contains the number of successful 2-point field 
goals, and the third line contains the number of successful 1-point free
 throws. Each number will be an integer between 0 and 100, inclusive.
"""

## Output Specification
"""
The output will be a single character. If the Apples scored more 
points than the Bananas, output A. If the Bananas scored more 
points than the Apples, output B. Otherwise, output T, to indicate a tie.
"""

apple_three = int(input())
apple_two = int(input())
apple_one = int(input())
banana_three = int(input())
banana_two = int(input())
banana_one = int(input())
apple_total = apple_three * 3 + apple_two * 2 + apple_one
banana_total = banana_three * 3 + banana_two * 2 + banana_one
if apple_total > banana_total:
    print('A')
elif banana_total > apple_total:
    print('B')
else:
    print('T')