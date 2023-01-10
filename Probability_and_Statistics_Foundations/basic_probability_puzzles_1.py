"""
Objective
In this challenge we practive calculating probability.

Task
In a single toss of 2 fair (evenly-weighted) 6-sided dice, 
find the probability of that their sum will be at most 9.
"""

from fractions import Fraction

condition_met = 0
visited = 0
for i in range(1, 6+1):
    for j in range(1, 6+1):
        if i+j <= 9:
            condition_met += 1
        visited += 1

print(Fraction(condition_met, visited))
