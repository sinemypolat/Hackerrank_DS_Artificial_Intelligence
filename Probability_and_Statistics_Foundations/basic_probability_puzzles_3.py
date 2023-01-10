"""
Objective
In this challenge, we practice calculating probability.

Task
There are 3 urns: X, Y and Z.

Urn X contains 4 red balls and 3 black balls.
Urn Y contains 5 red balls and 4 black balls.
Urn Z contains 4 red balls and 4 black balls.
One ball is drawn from each urn. 
What is the probability that 
the 3 balls drawn consist of 2 red balls and 1 black ball?
"""

from fractions import Fraction

x = 4*['r'] + 3*['b']
y = 5*['r'] + 4*['b']
z = 4*['r'] + 4*['b']

condition_met = 0
visited = 0
for i in x:
    for j in y:
        for k in z:
            drawing = [i,j,k]
            r_count = drawing.count("r")
            b_count = drawing.count("b")
            if (r_count ==2) and b_count==1:
                condition_met +=1
            visited+=1
            
print(Fraction(condition_met, visited))
