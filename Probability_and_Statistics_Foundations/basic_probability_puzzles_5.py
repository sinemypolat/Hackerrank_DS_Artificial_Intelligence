"""
Objective
In this challenge we practive calculating probability.

Task
There are 10 people about to sit down around a round table. 
Find the probability that 
2 particular people will sit next to one another.
"""

"""
Solution
If we treat these 2 people as 1, they can sit in (9-1)! different ways.
These 2 people can also change places between each other: 2!

Overall, 10 people could sit in (10-1)! ways.

Result = 2!*(9-1)!/(10-1)! = 2/9
"""

print("2/9")