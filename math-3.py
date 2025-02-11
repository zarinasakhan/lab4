import math
n=int(input("enter the number of sides:"))
l=int(input("enter the length of a side:"))
Area=(n * l**2)/(4*math.tan(math.pi/n))
print(int(Area))
