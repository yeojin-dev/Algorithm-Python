import math

ab = int(input())
ac = int(input())
angle_rad = math.atan2(ab, ac)
angle_deg = math.degrees(angle_rad)
print('{}°'.format(round(angle_deg)))
