import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def get_distance(lon_a, lat_a, lon_b, lat_b):
    temp_list = [lon_a, lat_a, lon_b, lat_b]
    for i in range(len(temp_list)):
        if isinstance(temp_list[i], str):
            temp_list[i] = float(temp_list[i].replace(',', '.'))
        temp_list[i] = temp_list[i] / 180 * math.pi
    lon_a, lat_a, lon_b, lat_b = temp_list
    x = (lon_b - lon_a) * math.cos((lat_a + lat_b) / 2)
    y = lat_b - lat_a
    return math.sqrt(x**2 + y**2) * 6371


lon = input()

lat = input()

n = int(input())
min_d, min_name = 99999, None

for i in range(n):
    defib = input()
    _, name, _, _, lon_t, lat_t = defib.split(';')
    distance = get_distance(lon, lat, lon_t, lat_t)
    print("Distance of {}:".format(name), distance, file=sys.stderr)
    if distance < min_d:
        min_d = distance
        min_name = name

print(min_name)
