import pyxel
import random

pyxel.init(256, 256, title="Merry Christmas Demo by @lawofcons")
pyxel.load("xmas_resource.pyxres")
# load the sprite sheet
pyxel.images[0].load(0, 0, "christmas_tree_w_snow2.png")

current_frame = 0
tree_width = 128
tree_height = 160
snowflakes = []
current_sequence = 0

def update():
    global current_frame
    global snowflakes
    global current_sequence

    # play song parts back to back and cycle back to the beginning
    if pyxel.play_pos(0) is None:
        current_sequence = (current_sequence + 1) % 3
        pyxel.play(0, current_sequence)
    # speed
    if pyxel.frame_count % 10 == 0:
        # cycle between 0 and 1
        current_frame = (current_frame + 1) % 2
    for snowflake in snowflakes:
        # move snowflake down
        snowflake[1] += 1
        # reset snowflake to the top
        if snowflake[1] > pyxel.height:
            snowflake[0] = random.randint(0, pyxel.width)
            snowflake[1] = 0


def initialize_snowflakes():
    """Init snowflakes with random positions"""
    global snowflakes
    for _ in range(400):
        x = random.randint(0, pyxel.width)
        y = random.randint(0, pyxel.height)
        snowflakes.append([x, y])

def draw():
    global snowflakes
    global current_frame
    global tree_height
    global tree_width
    pyxel.cls(0)

    # Draw snowy ground
    ground_y = pyxel.height - 48  # Height of the ground
    pyxel.rect(0, ground_y, pyxel.width, 60, pyxel.COLOR_WHITE)
    speed = 15
    # add specks of snow for texture
    # adjust number of specks
    for _ in range(100):
        if pyxel.frame_count % speed == 0:
            x = random.randint(0, pyxel.width)
            y = random.randint(ground_y, pyxel.height)
            pyxel.pset(x, y, pyxel.COLOR_LIGHT_BLUE)


    u = current_frame * 128
    # Draw the sprite at in the x mid-point.
    tree_x = (pyxel.width // 2) - (tree_width // 2)
    tree_y = (pyxel.height // 2) - 32
    pyxel.blt(tree_x, tree_y, 0, u, 0, tree_width, tree_height, 0)
    # Draw snowflakes.
    for snowflake in snowflakes:
        pyxel.pset(snowflake[0],
                   snowflake[1],
                   pyxel.COLOR_WHITE)
    # Draw Moon
    moon_x = pyxel.width - 50
    moon_y = 50
    moon_radius = 15

    # Draw the glow (larger, semi-transparent circle).
    pyxel.circb(moon_x, moon_y, moon_radius + 8, pyxel.COLOR_LIGHT_BLUE)
    pyxel.circb(moon_x, moon_y, moon_radius + 6, pyxel.COLOR_LIGHT_BLUE)

    # Draw the moon.
    pyxel.circ(moon_x, moon_y, moon_radius, pyxel.COLOR_WHITE)


initialize_snowflakes()
pyxel.run(update, draw)
