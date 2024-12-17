import random
import pyxel

width = 500
height = 100
borderx = 20
bordery = 10
y = 50
step = 10
lastx = -999
lasty = -999
pyxel.init(width, height, title="Drawing lines in Pyxel")
pyxel.cls(5)
for x in range(borderx, width-borderx, step):
    y = bordery + random.uniform(0, height - 2 * bordery)
    if lastx > -999:
        pyxel.line(x, y, lastx, lasty, 11)
    lastx = x
    lasty = y
pyxel.show()
