"""
Objective
In this challenge we practive calculating probability.

Task
Bag X contains 5 white balls and 4 black balls. 
Bag Y contains 7 white balls and 6 black balls.
You draw 1 ball from bag X and, 
without observing its color, put it into bag Y.
Now, if a ball is drawn from bag Y, 
find the probability that it is black.
"""

from fractions import Fraction
b1 = ['w'] * 5 + ['b'] * 4
b2 = ['w'] * 7 + ['b'] * 6

condition_met = 0
visited = 0
for i in b1:
    b2 = ['w'] * 7 + ['b'] * 6
    b2.append(i)
    for j in b2:
        if j=="b": condition_met+=1
        visited+=1
        
print(Fraction(condition_met, visited))