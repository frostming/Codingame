import sys
import math
import collections

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
tree = lambda: collections.defaultdict(tree)
storage = tree()
number = 0
n = int(input())
for i in range(n):
    current = storage
    telephone = input()
    for d in telephone:
        if d not in current:
            number += 1
        current = current[d]
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# The number of elements (referencing a number) stored in the structure.
print(number)
