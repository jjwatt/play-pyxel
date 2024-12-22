import pyxel


def bline(x1, y1, x2, y2):
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


width = 500
height = 100
points = bline(20, 10, 400, 90)
pyxel.init(width, height, title="bresenham line")
pyxel.cls(5)
for p in points:
    pyxel.pset(p[0], p[1], 11)
pyxel.show()
