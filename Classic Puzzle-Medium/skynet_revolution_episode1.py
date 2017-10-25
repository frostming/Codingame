import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
matrix = []


def find_closest(line, start=0):
    for i, val in enumerate(line[start:]):
        if val == '0':
            return i + start
    return -1


for i in range(height):
    line = input()  # width characters, each either 0 or .
    matrix.append(line)

for y, line in enumerate(matrix):
    x = find_closest(line)
    while x >= 0:
        output = [x, y]
        right_x = find_closest(line, x + 1)
        if right_x > x:
            output.extend([right_x, y])
        else:
            output.extend([-1, -1])
        bottom_y = find_closest([line[x] for line in matrix], y + 1)
        if bottom_y > y:
            output.extend([x, bottom_y])
        else:
            output.extend([-1, -1])
        print(*output)
        x = right_x
