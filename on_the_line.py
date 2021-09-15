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
