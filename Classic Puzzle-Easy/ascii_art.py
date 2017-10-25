import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
print(t, file=sys.stderr)


def get_start_pos(c):
    offset = ord(c.upper()) - ord('A')
    if offset < 0 or offset > 25:
        offset = 26
    return offset * l

for i in range(h):
    row = input()
    print(row, file=sys.stderr)
    for c in t:
        offset = get_start_pos(c)
        print(row[offset:offset + l], end='')
    print()
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
