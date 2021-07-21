# A simple program to compute the perimeter and area of polygons
#   * Perimeter and area of squares and rectangles
#   * Perimeter and area of triangles
#   * Circumference and area of circles
#   * Perimeter of arbitrary polygon

import math as math


def distance(a, b):
    """
    Computes the Euclidean distance between two points, a and b
    """
    x_coor = a.x - b.x
    y_coor = a.y - b.y
    x_squared = x_coor ** 2
    y_squared = y_coor ** 2
    return math.sqrt(x_squared + y_squared)
    # return math.sqrt(((a.x - b.x)**2) + ((a.y - b.y)**2))


class Point:
    """
    Defines a point in an Euclidean plane
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    """
    Defines a circle in an Euclidean plane
    """
    def __init__(self, point, radius):
        self.point = point
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


class Quadrilateral:
    """
    Defines a rectangle or square in an Euclidean plane
    """
    def __init__(self, top_left, height, width):
        self.top_left = top_left
        self.height = height
        self.width = width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.width * self.height


class Triangle:
    """
    Defines a triangle in an Euclidean plane

    Note that this class is flawed. We know only its size, but not its location.
    """
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return (self.base * self.height) / 2.0


class Polygon:
    """
    Defines a polygon of arbitrary size in an Euclidean plane.

    Note that the points attribute is not a single point, but a list of points that describe the polygon's vertices.
    The sides attribute describes the number of sides of the polygon, which coincides with the length of the points list.
    """
    def __init__(self, sides, points):
        self.sides = sides
        self.points = points

    def perimeter(self):
        per = 0
        for index in range(self.sides):
            if index < len(self.points):  # self.sides
                per += distance(self.points[index], self.points[index + 1])
            else:
                per += distance(self.points[0], self.points[-1])
                # distance(self.points[0], self.points[index])

        return per


if __name__ == "main":
    # do something