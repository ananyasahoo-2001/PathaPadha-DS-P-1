# Calculating the distance between two points

x = (x1,x2) = (float(input("Enter x1: ")) , float(input("      x2: ")))
y = (y1,y2) = (float(input("Enter y1: ")) , float(input("      y2: ")))

distance = (((x2-x1)**2) + ((y2-y1)**2)) ** 0.5

print("Distance between two points is " , distance)
