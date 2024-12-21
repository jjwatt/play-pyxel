import pyxel


def bline(x1, y1, x2, y2):
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    x_step = (1 if x2 > x1 else -1)
    y_step = (1 if y2 > y1 else -1)
    steepq = dy > dx
    if steepq:
        dx, dy = dy, dx
    d = 2 * dy - dx  # decision variable
    points = []
    for _ in range(dx + 1):
        points.append((y1, x1) if steepq else (x1, y1))
        if d > 0:
            y1 += y_step if steepq else x_step
            d -= 2 * dx
        x1 += x_step if not steepq else y_step
        d += 2 * dy
    return points


def draw_line(x1, y1, x2, y2, col):
    points = bline(x1, y1, x2, y2)
    for p in points:
        pyxel.pset(p[0], p[1], col)


width, height = 500, 100
pyxel.init(width, height, title="bresenham line")
pyxel.cls(5)
draw_line(20, 10, 400, 90, 11)
pyxel.show()
