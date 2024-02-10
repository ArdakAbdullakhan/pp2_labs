import math

def area_parallelogram(l,h):
    area = l * h
    return float(area)

print('Expected Output:', area_parallelogram(int(input('Length of base: ')), int(input('Height of parallelogram: '))))