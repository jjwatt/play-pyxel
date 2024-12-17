import random

import pyxel

width = 500
height = 100
border = 20
y = 50

pyxel.init(width, height, title="Drawing lines in Pyxel")

def update():
    pass

def draw():
    step = 10
    lastx = -999
    lasty = -999
    pyxel.cls(5)
    # pyxel.rect(10, 10, 20, 20, 11)
    # pyxel.line(20, 50, randx, randy, 0)
    for x in range(border, width-border, step):
        if lastx > -999:
            pyxel.line(x, y, lastx, lasty, 11)
        lastx = x
        lasty = y


pyxel.run(update, draw)
