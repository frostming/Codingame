import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mime_types = dict()
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_types[ext.lower()] = mt
print(mime_types, file=sys.stderr)
for i in range(q):
    fname = input()  # One file name per line.
    print("file name:", fname, file=sys.stderr)
    last_dot = fname.rfind('.')
    if last_dot < 0:
        print("UNKNOWN")
    else:
        ext = fname[last_dot + 1:]
        print(mime_types.get(ext.lower(), 'UNKNOWN'))
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
