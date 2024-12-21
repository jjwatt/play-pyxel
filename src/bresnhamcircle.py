import pyxel

def bcircle(x0, y0, radius):
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
def draw_circle(x, y, radius, color):
    points = bcircle(x, y, radius)
    for p in points:
        pyxel.pset(p[0], p[1], color)
width, height = 400, 400
pyxel.init(width, height, title="bresenham circle")
pyxel.cls(5)
draw_circle(200, 200, 100, 11)
pyxel.show()
