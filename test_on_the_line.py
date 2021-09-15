import pytest

# unit test for entire on the line function
@pytest.mark.parametrize("point1, point2, x, exp_y", [
    ((1, 2), (5, 8), 3, 5)])
def test_on_the_line_calc(point1, point2, x, exp_y):
    from on_the_line import on_the_line_calc
    y = on_the_line_calc(point1, point2, x)
    assert y == exp_y

# modular unit testing to match the broken down into steps function

# unit test for slope calculation
@pytest.mark.parametrize("point1, point2, exp_slope", [
    ((1, 2), (5, 8), 1.5)])
def test_slope_calc(point1, point2, exp_slope):
    from on_the_line import slope_calc
    slope = slope_calc(point1, point2)
    assert slope == exp_slope