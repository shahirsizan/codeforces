import math

n, gun_coordinateX, gun_coordinateY = map(int, input().split())
stormtroopers_coordinate_list = list()

for particular_soldiers_coordinate in range(n):
    a, b = list( map(int, input().split()) )
    stormtroopers_coordinate_list.append((a, b))

angles_list = list()

for particular_soldiers_coordinate in stormtroopers_coordinate_list:
    xDist = particular_soldiers_coordinate[0] - gun_coordinateX
    yDist = particular_soldiers_coordinate[1] - gun_coordinateY
    theta = math.atan2(yDist, xDist)    # `atan2` is inverse of tan
    if theta > 0:
        theta = theta
    else:
        theta = theta + math.pi

    theta = round(theta, 10)
    if theta not in angles_list:
        angles_list.append(theta)

no_of_shots = len(angles_list)
print(no_of_shots)
