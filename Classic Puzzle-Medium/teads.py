import sys

"""Dijkstra algorithm solution!"""

edges = dict()
n = int(input())  # the number of adjacency relations
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]
    edges.setdefault(xi, []).append(yi)
    edges.setdefault(yi, []).append(xi)

max_depth = 0

while len(edges) > 2:
    print(edges, file=sys.stderr)
    to_delete = []
    for i, val in edges.items():
        if len(val) == 1:
            to_delete.append(i)
    for i in to_delete:
        neighbor = edges[i][0]
        edges[neighbor].remove(i)
        del edges[i]
    max_depth += 1

if len(edges) == 2:
    max_depth += 1

print(max_depth)
