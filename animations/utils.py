import math


def distance(x0, y0, x1, y1):
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)


def polarToRectangular(app, distance, theta):
    x = app.width / 2 + distance * math.cos(theta)
    y = app.height / 2 + distance * math.sin(theta)
    return x, y
