# On The Line Function
# Author: Stevan Kriss
# Date: 9/15/21
# Class: BME547 - Medical Software Design

# Entire Function - not modular
# define input parameters
x1 = 1
y1 = 2
x2 = 5
y2 = 8
point1 = (x1, y1)
point2 = (x2, y2)
x = 3

def on_the_line_calc(point1, point2, x):
    slope_num = point2[1] - point1[1]
    slope_denom = point2[0] - point1[0]
    slope = slope_num / slope_denom
    intercept = point1[1] - slope * point1[0]
    y = x * slope + intercept
    print(y)
    return y

if __name__ == '__main__':
    on_the_line_calc(point1, point2, x)