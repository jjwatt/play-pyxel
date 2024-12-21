import pyxel

pyxel.init(256, 256, title="Draw Sprite")
# load the sprite sheet
pyxel.images[0].load(0, 0, "christmas_tree_w_snow2.png")
current_frame = 0
tree_width = 128
tree_height = 160

def update():
    global current_frame
    # Adjust speed
    if pyxel.frame_count % 10 == 0:
        # cycle between 0 and 1
        current_frame = (current_frame + 1) % 2

def draw():
    pyxel.cls(0)
    u = current_frame * 128
    # Draw the sprite at in the x mid-point
    tree_x = (pyxel.width // 2) - (tree_width // 2)
    tree_y = (pyxel.height // 2) - 32
    pyxel.blt(tree_x, tree_y, 0, u, 0, 128, 160, 6)
    pyxel.text(5, 5, f"Frame: {current_frame}", 7)
    pyxel.text(5, 15, f"Frame Count: {pyxel.frame_count}", 7)

pyxel.run(update, draw)
