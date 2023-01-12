"""
Task

Here are the test scores of 10 students in physics and history:

Physics Scores  15  12  8   8   7   7   7   6   5   3
History Scores  10  25  17  11  13  17  20  13  9   15
Compute the slope of the line of regression obtained
while treating Physics as the independent variable.
Compute the answer correct to three decimal places.
"""

from statistics import mean

x = list(map(int, "15 12 8 8 7 7 7 6 5 3".split(" ")))
y = list(map(int, "10 25 17 11 13 17 20 13 9 15".split(" ")))

# y = a*x + b

# a = ( mean(x)*mean(y) - mean(x*y) ) /( mean(x)**2 - mean(x**2))

numerator = mean(x)*mean(y) - mean([a*b for a,b in zip(x,y)])
denominator = mean(x)**2 - mean([a**2 for a in x])

a = numerator/denominator
b = mean(y) - mean(x)*a

result = a*10 + b

print(round(result, 1))
