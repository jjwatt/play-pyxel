import pyxel

def bline(x1, y1, x2, y2):
    points = []
    # deltas
    dx = x2 - x1
    dy = y2 - y1
    

pyxel.init(width, height, title="Drawing lines in Pyxel")
pyxel.cls(5)
pyxel.show()
