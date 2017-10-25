import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
binary_message = ''.join('{:07b}'.format(ord(c)) for c in message)
print('Binary message:', binary_message, file=sys.stderr)

result = []
current = None

for c in binary_message:
    if current is None or current[-1] != c:
        if current:
            result.append('0' * len(current))
        current = c
        if current == '1':
            result.append('0')
        else:
            result.append('00')
    else:
        current += c
if current:
    result.append('0' * len(current))

print(result, file=sys.stderr)
print(' '.join(result))
