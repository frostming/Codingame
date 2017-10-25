import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    max_index, max_h = 0, 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h > max_h:
            max_index, max_h = i, mountain_h
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The index of the mountain to fire on.
    print(max_index)
