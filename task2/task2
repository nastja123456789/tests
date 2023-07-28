import sys
def point_position(center_x, center_y, radius, point_x, point_y):
    distance_squared = (point_x - center_x) ** 2 + (point_y - center_y) ** 2
    if distance_squared == radius ** 2:
        return 0
    elif distance_squared < radius ** 2:
        return 1
    else:
        return 2
filename1 = sys.argv[1]
with open(filename1, 'r') as file:
    center_x, center_y = map(float, file.readline().split())
    radius = float(file.readline())
filename2 = sys.argv[2]
with open(filename2, 'r') as file:
    for line in file:
        point_x, point_y = map(float, line.split())
        position = point_position(center_x, center_y, radius, point_x, point_y)
        print(position)
