import math

def score(x, y):
    x_center = 0
    y_center = 0

    distance = math.sqrt((x-x_center)**2+(y-y_center)**2)
    print(distance)

    if distance > 10:
        return 0
    if distance > 5 and distance <= 10:
        return 1
    if distance > 1 and distance <= 5:
        return 5
    if distance <= 1:
        return 10