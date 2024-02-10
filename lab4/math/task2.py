import math
def area_trapezoid(h,a,b):
    area = 0.5*(a+b)*h
    return area

print("Expected Output: ", area_trapezoid(int(input("Height: ")),int(input("Base, first value: ")),int(input("Base, second value: "))))