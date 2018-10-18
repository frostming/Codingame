"""Puzzle of the week: Disordered First Contact
https://www.codingame.com/ide/13945982cfc79fb7567d1d06c7ea3e2073d7f966
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


def encode(message):
    result = []
    nchars = 1
    while message:
        if nchars % 2:
            result.append(message[:nchars])
        else:
            result.insert(0, message[:nchars])
        message = message[nchars:]
        nchars += 1
    return ''.join(result)


def decode(message):
    message_len = len(message)
    n = int(math.ceil((math.sqrt(1+8*message_len)-1)/2))
    last_part_len = n - n*(n+1)//2 + message_len
    if n % 2:  # last part is at the tail
        start_pos = (n + 1)*(n - 1) //4
    else:
        start_pos = n * (n - 2)//4 + last_part_len
    l = r = start_pos
    result = []
    for i in range(1, n + 1):
        if i % 2:
            result.append(message[r:r+i])
            r += i
        else:
            result.append(message[max(0, l-i):l])
            l -= i
    return ''.join(result)



if n > 0:
    for _ in range(n):
        message = decode(message)
elif n < 0:
    for _ in range(-n):
        message = encode(message)
print(message)
