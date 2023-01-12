"""
Task

Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
Compute Karl Pearson’s coefficient of correlation between these scores.
Compute the answer correct to three decimal places.
"""

from math import sqrt

x = list(map(int, "15 12 8 8 7 7 7 6 5 3".split(" ")))
y = list(map(int, "10 25 17 11 13 17 20 13 9 15".split(" ")))

n = len(x)
sum_xy = sum([i*j for i, j in zip(x, y)])
sum_x = sum(x)
sum_y = sum(y)
sum_x2 = sum([i*i for i in x])
sum_y2 = sum([j*j for j in y])

numerator = (n*sum_xy - sum_x*sum_y)
denominator = sqrt((n*sum_x2 - sum_x**2) * (n*sum_y2 - sum_y**2))
result = numerator/denominator

print(round(numerator/denominator, 3))
