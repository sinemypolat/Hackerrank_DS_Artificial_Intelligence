"""
Task
Princess Peach is trapped in one of the four corners of a square grid. 
You are in the center of the grid and can move one step 
at a time in any of the four directions. 
Can you rescue the princess?

Input
The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. 
This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). 
The bot position is denoted by 'm' and the princess position is denoted by 'p'.

Grid is indexed using Matrix Convention

Output
Print out the moves you will take to rescue the princess in one go. 
The moves must be separated by '\n', a newline. 
The valid moves are LEFT or RIGHT or UP or DOWN.

"""

def displayPathtoPrincess(n,grid):
    for i1, j in enumerate(grid):
        for i2, k in enumerate(grid):
            if grid[i1][i2]=='m': bot_loc = [i1,i2]
            elif grid[i1][i2]=='p': p_loc = [i1,i2]

    diff = tuple(x-y for x,y in zip(bot_loc, p_loc))

    if diff[0]<0:
        for i in range(abs(diff[0])):
            print("DOWN")
    elif diff[0]>0:
        for i in range(diff[0]):
            print("UP")
    if diff[1]<0:
        for i in range(abs(diff[1])):
            print("RIGHT")
    elif diff[1]>0:
        for i in range(diff[1]):
            print("LEFT")
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
