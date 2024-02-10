import math

def area_polygon(n,s):
    if(n>2):
        area = (n * s**2)/4 * math.tan(math.pi/n)
        return round(area)
    else:
        print("Your polygon doesn't exist")

print("The area of the polygon is:", area_polygon(int(input("Input number of sides: ")),int(input("Input the length of a side: "))))