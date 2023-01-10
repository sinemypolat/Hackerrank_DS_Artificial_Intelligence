"""
Objective
In this challenge, we practice calculating probability.

Task
A firm produces steel pipes in three plants.

Plant A produces 500 units per day and has a fraction defective output of 0.005.
Plant B produces 1000 units per day and has a fraction defective output of 0.008.
Plant C produces 2000 units per day and has a fraction defective output of 0.010.
At random, a pipe is selected from the day’s total production and it is found to be defective. 
What is the probability that it came from plant A?
"""

# Bayes theorem
# P(A|defective) = P(A and defective) / P(defective)

#result=(0.005*(500/3500))/((0.005*(500/3500)) + (0.008*(1000/3500)) + (0.010*(2000/3500)))

print("5/61")