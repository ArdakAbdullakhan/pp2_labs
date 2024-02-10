import math
def degree_to_radian(n):
    radians = n * (math.pi / 180)
    return radians

print("Output radian:", degree_to_radian(int(input("Input degree:"))))