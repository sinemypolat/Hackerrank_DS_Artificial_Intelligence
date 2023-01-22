"""
In this version of "Bot saves princess", 
Princess Peach and bot's position are randomly set. 
Can you save the princess?

Task
Complete the function nextMove which takes in 4 parameters 
- an integer N, integers r and c indicating the row & column position of the bot 
and the character array grid - 
and outputs the next move the bot makes to rescue the princess.

Input
The first line of the input is N (<100), the size of the board (NxN). 
The second line of the input contains two space separated integers, which is the position of the bot.
Each cell is denoted by '-' (ascii value: 45). 
The bot position is denoted by 'm' and the princess position is denoted by 'p'.

Grid is indexed using Matrix Convention

Output
Output only the next move you take to rescue the princess. 
Valid moves are LEFT, RIGHT, UP or DOWN
"""

def nextMove(n,r,c,grid):
    # find location of princess
    for i1, j in enumerate(grid):
        for i2, k in enumerate(grid):
            if grid[i1][i2]=='p': p_loc = [i1,i2]

    diff = [x-y for x,y in zip([r,c], p_loc)]
    
    next_move = ""
    if diff[0]<0:
        next_move = "DOWN"
    elif diff[0]>0:
        next_move = "UP"
    elif diff[1]<0:
        next_move = "RIGHT"
    elif diff[1]>0:
        next_move = "LEFT"
            
    return next_move


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))