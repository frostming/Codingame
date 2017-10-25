import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class Node:
    def __init__(self, i):
        self.val = i
        self._links = set()
        self.exit = False

    def connect(self, other):
        self._links.add(other)
        other._links.add(self)

    def disconnect(self, other):
        self._links.discard(other)
        other._links.discard(self)

    def __repr__(self):
        return '<Node {}>'.format(self.val)

    def pick_one_node(self):
        # print(self._links, file=sys.stderr)
        if not self._links:
            return None
        for node in self._links:
            if node.exit:
                self.disconnect(node)
                return node
        node = self._links.pop()
        self.disconnect(node)
        return node

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

all_nodes = [Node(i) for i in range(n)]

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    all_nodes[n1].connect(all_nodes[n2])
    # print('{}-{}'.format(n1, n2), file=sys.stderr)


for i in range(e):
    ei = int(input())  # the index of a gateway node
    all_nodes[ei].exit = True

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    node = all_nodes[si].pick_one_node()
    if node is not None:
        print(si, node.val)
