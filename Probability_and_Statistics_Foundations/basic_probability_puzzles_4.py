"""
Objective
In this challenge, we practice calculating probability.

Task
Bag1 contains 4 red balls and 5 black balls.
Bag2 contains 3 red balls and 7 black balls.

One ball is drawn from Bag1, and 2 balls are drawn from Bag2. 
Find the probability that 2 balls are black and 1 ball is red.
"""

from fractions import Fraction
b1 = ['r']*4 + ['b']*5
b2 = ['r']*3 + ['b']*7

visited = 0
condition_met = 0
for i in b1:
    for idx, j in enumerate(b2):
        for k in b2[idx+1:]:
            drawn = [i,j,k]
            if drawn.count('r')==1 and drawn.count('b')==2:
                condition_met+=1
            visited+=1
            
print(Fraction(condition_met, visited))
