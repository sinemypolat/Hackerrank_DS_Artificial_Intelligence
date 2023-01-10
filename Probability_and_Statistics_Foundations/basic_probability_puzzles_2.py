"""
Objective
In this challenge, we practice calculating probability.

Task
For a single toss of 2 fair (evenly-weighted) dice, 
find the probability that the values rolled 
by each die will be different and their sum is 6.
"""

from fractions import Fraction

condition_met=0
visited=0
for i in range(1,6+1):
    for j in range(1,6+1):
        if i!=j and i+j==6: condition_met+=1
        visited+=1

print(Fraction(condition_met, visited))
