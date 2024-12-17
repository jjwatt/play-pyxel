import random

import pyxel

width = 500
height = 100
randx = random.randint(1, width)
randy = random.randint(1, height)
pyxel.init(width, height, title="Drawing lines in Pyxel")

def update():
    pass


def draw():
    pyxel.cls(5)
    # pyxel.rect(10, 10, 20, 20, 11)
    pyxel.line(20, 50, randx, randy, 0)

pyxel.run(update, draw)
