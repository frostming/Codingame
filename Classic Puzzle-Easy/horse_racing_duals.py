import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

strengths = []

for i in range(n):
    pi = int(input())
    strengths.append(pi)

strengths.sort()
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
min_d = min(abs(i - j) for i, j in zip(strengths, strengths[1:]))
print(min_d)
