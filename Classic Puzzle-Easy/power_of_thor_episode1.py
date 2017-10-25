import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    print("Remaining turns:", remaining_turns, file=sys.stderr)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    d_x, d_y = light_x - initial_tx, light_y - initial_ty
    while d_x != 0 and d_y != 0:
        if d_x > 0:
            move_x = 'E'
            d_x -= 1
        else:
            move_x = 'W'
            d_x += 1
        if d_y > 0:
            move_y = 'S'
            d_y -= 1
        else:
            move_y = 'N'
            d_y += 1
        print(move_y + move_x)
    if d_x != 0:
        for i in range(abs(d_x)):
            print('E' if d_x > 0 else 'W')
    if d_y != 0:
        for i in range(abs(d_y)):
            print('S' if d_y > 0 else 'N')
