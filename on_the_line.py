# On The Line Function
# Author: Stevan Kriss
# Date: 9/15/21
# Class: BME547 - Medical Software Design

# Entire Function - not modular
def on_the_line_calc(point1, point2, x):
    slope_num = point2[1] - point1[1]
    slope_denom = point2[0] - point1[0]
    slope = slope_num / slope_denom
    intercept = point1[1] - slope * point1[0]
    y = x * slope + intercept
    return y

# Breaking function down into smaller steps - modular

# Slope calculation from 2 (x,y) points
def slope_calc(point1, point2)
    slope_num = point2[1] - point1[1]
    slope_denom = point2[0] - point1[0]
    slope = slope_num / slope_denom
    return slope

# Intercept calculation from 1 (x,y) point and slope
def intercept_calc(point1, point2, slope)
    intercept = point1[1] - slope * point1[0]
    return intercept

# Y value calculation from x input using slope and intercept
def y_calc(x, slope, intercept)
    y = x * slope + intercept
    return y

