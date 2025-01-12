"""Bresenham's Drawing Algorithms"""
import pyxel

def bresenham_line(x1, y1, x2, y2):
    """Bresenham's Line Drawing algorithm.
    Args:
        x1, y1, x2, y2: The beginning and end points
    Returns:
      A list of points for the line
    """
    # deltas
    dx = x2 - x1
    dy = y2 - y1

    # which direction?
    x_step = 1 if dx > 0 else -1
    y_step = 1 if dy > 0 else -1

    # abs of deltas
    dx = abs(dx)
    dy = abs(dy)

    points = []
    # Initialize decision variable
    if dx >= dy:
        # line is more horizontal
        d = 2 * dy - dx
        while x1 != x2:
            points.append((x1, y1))
            if d > 0:
                y1 += y_step
                d -= 2 * dx
            x1 += x_step
            d += 2 * dy
    else:
        # line is more vertical
        d = 2 * dx - dy
        while y1 != y2:
            points.append((x1, y1))
            if d > 0:
                x1 += x_step
                d -= 2 * dy
            y1 += y_step
            d += 2 * dx
    # Add the final point
    points.append((x2, y2))
    return points


def bresenham_circle(x0, y0, radius):
    x = radius
    y = 0
    err = 0
    points = []
    while x >= y:
        points.extend([(x0 + x, y0 + y), (x0 + y, y0 + x),
                       (x0 - y, y0 + x), (x0 - x, y0 + y),
                       (x0 - x, y0 - y), (x0 - y, y0 - x),
                       (x0 + y, y0 - x), (x0 + x, y0 - y)])
        y += 1
        err += 1 + 2 * y
        if 2 * (err - x) + 1 > 0:
            x -= 1
            err += 1 - 2 * x
    return points


def draw_line(x1, y1, x2, y2, col):
    points = bresenham_line(x1, y1, x2, y2)
    for p in points:
        pyxel.pset(p[0], p[1], col)


def draw_filled_rectangle(x1, y1, x2, y2, color):
    for y in range(y1, y2 + 1):
        draw_line(x1, y, x2, y, color)


def draw_circle(x, y, radius, color):
    points = bresenham_circle(x, y, radius)
    for p in points:
        pyxel.pset(p[0], p[1], color)
