"""
Awalé is an african 2 players game consisting of moving grains in some bowls.
Each player has 7 bowls indexed from 0 to 6. The last bowl is the reserve.

Input
5 1 0 6 2 2 3
3 4 0 3 3 2 2
0

Output
5 1 0 6 2 2 [3]
0 5 1 4 3 2 [2]
"""
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

op_bowls = list(map(int, input().strip().split()))
my_bowls = list(map(int, input().strip().split()))
num = int(input())

selection = {
    True: (my_bowls, 7),
    False: (op_bowls, 6)
}


def distribute():
    is_my_bowl = True
    hand_grains = my_bowls[num]
    my_bowls[num] = 0
    current = num + 1
    bowels, max_num = selection[is_my_bowl]
    while hand_grains > 0:
        if current == max_num:
            is_my_bowl = not is_my_bowl
            bowels, max_num = selection[is_my_bowl]
            current = 0
        bowels[current] += 1
        hand_grains -= 1
        current += 1

    print(' '.join(map(str, op_bowls[:-1])), '[{}]'.format(op_bowls[-1]))
    print(' '.join(map(str, my_bowls[:-1])), '[{}]'.format(my_bowls[-1]))
    if is_my_bowl and current == len(my_bowls) - 1:
        print('REPLAY')


distribute()
