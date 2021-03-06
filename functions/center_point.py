# You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines. Write a function that prints the 
# point which is closest to the center of the coordinate system (0, 0) in the format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one. The resulting coordinates must be formatted to the lower integer.


from math import sqrt

def center_point_func(x, y):
    dist_x = sqrt(abs(x[0] ** 2)) + (abs(x[1] ** 2))
    dist_y = sqrt(abs(y[0] ** 2)) + (abs(y[1] ** 2))
    if dist_x < dist_y:
        output = (int(x[0] // 1)), int(x[1] // 1)
    elif dist_y < dist_x:
        output = (int(y[0 // 1])), int(y[1] // 1)
    else:
        output = (int(x[0]// 1)), int(x[1] // 1)
    print(output)

point_1 = (float(input()),float(input()))
point_2 = (float(input()),float(input()))
center_point_func(point_1, point_2)
