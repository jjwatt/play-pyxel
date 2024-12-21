import pyxel
import random


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


def draw_line(x1, y1, x2, y2, col):
    points = bline(x1, y1, x2, y2)
    for p in points:
        pyxel.pset(p[0], p[1], col)


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


class ChristmasDemo:
    def __init__(self):
        self.width = 256
        self.height = 256
        self.snowflakes = []
        self.ornaments = []
        pyxel.init(self.width,
                   self.height,
                   title="ChristmasDemo")
        self.initialize_snowflakes()
        self.initialize_ornaments()
        pyxel.run(self.update, self.draw)

    def initialize_snowflakes(self):
        """Init snowflakes with random positions"""
        for _ in range(400):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            self.snowflakes.append([x, y])

    def initialize_ornaments(self):
        """Initialize static ornaments."""
        tree_x = self.width // 2
        tree_y = self.height - 20
        self.ornaments = []
        # Generate ornaments within tree bounds
        for _ in range(15):  # Adjust number of ornaments
            while True:
                # Adjust bounds to match tree width
                x = random.randint(int(tree_x - 20), int(tree_x + 20))
                # Match tree height
                y = random.randint(int(tree_y - 80), int(tree_y - 20))
                # Check within tree bounds (triangle shape)
                layer_height = tree_y - y
                # Match layer width
                layer_width = 60 - (layer_height // 20) * 15
                if abs(tree_x - x) <= layer_width // 2:
                    self.ornaments.append((x, y))
                    break

    def update(self):
        """Update snowflake positions."""
        for snowflake in self.snowflakes:
            snowflake[1] += 1  # move snowflake down
            if snowflake[1] > self.height:  # reset snowflake to the top
                snowflake[0] = random.randint(0, self.width)
                snowflake[1] = 0

    def draw_tree(self):
        """Draw a simple Christmas tree."""
        tree_x = self.width / 2
        tree_y = self.height - 20

        # Draw tree trunk
        pyxel.rect(tree_x - 5, tree_y - 20, 10, 20, pyxel.COLOR_BROWN)

        # Draw tree layers
        # colors = [pyxel.COLOR_GREEN, pyxel.COLOR_DARKGREEN]
        layer_height = 20
        for i in range(4):
            layer_width = 80 - i * 15
            base_y = tree_y - layer_height  # bottom of current layer
            top_y = tree_y - (i + 1) * layer_height  # top of the current layer
        pyxel.tri(
            tree_x - layer_width // 2, base_y,  # left corner
            tree_x, top_y,                      # bottom point
            tree_x + layer_width // 2, base_y,  # Right corner
            pyxel.COLOR_GREEN,
        )

        # Add ornaments
        # Draw ornaments with blinking effect
        # Adjust this for faster/slower blinking (lower is faster)
        blink_speed = 10
        
        color_choice = (random.choice([pyxel.COLOR_RED, pyxel.COLOR_YELLOW, pyxel.COLOR_GREEN])
                        if pyxel.frame_count % blink_speed == 0 else pyxel.COLOR_YELLOW)
        for x, y in self.ornaments:
            # Set color to blink or keep steady
            color = color_choice if color_choice else pyxel.COLOR_WHITE
            pyxel.circ(x, y, 1, color)
            
        # Draw the star at the top
        pyxel.circ(tree_x, tree_y - 80, 5, pyxel.COLOR_YELLOW)

    def draw_snowy_ground(self):
        """Draw a snowy ground with random specks of snow."""
        ground_y = self.height - 20  # Height of the ground
        pyxel.rect(0, ground_y, self.width, 30, pyxel.COLOR_WHITE)
        speed = 15
        # Add specks of snow for texture
        # Adjust number of specks
        for _ in range(100):
            if pyxel.frame_count % speed == 0:
                x = random.randint(0, self.width)
                y = random.randint(ground_y, self.height)
                pyxel.pset(x, y, pyxel.COLOR_LIGHT_BLUE)

    def draw_moon(self):
        """Draw a moon with a glowing effect."""
        moon_x = self.width - 50  # X position for the moon (near top-right corner)
        moon_y = 50              # Y position for the moon
        moon_radius = 15         # Radius of the moon

        # Draw the glow (larger, semi-transparent circle)
        pyxel.circb(moon_x, moon_y, moon_radius + 8, pyxel.COLOR_LIGHT_BLUE)
        pyxel.circb(moon_x, moon_y, moon_radius + 6, pyxel.COLOR_LIGHT_BLUE)

        # Draw the moon itself
        pyxel.circ(moon_x, moon_y, moon_radius, pyxel.COLOR_WHITE)
    
    def draw_snow(self):
        """Draw snowflakes"""
        for snowflake in self.snowflakes:
            pyxel.pset(snowflake[0],
                       snowflake[1],
                       pyxel.COLOR_WHITE)

    def draw(self):
        """Draw frame."""
        pyxel.cls(pyxel.COLOR_BLACK)
        self.draw_snow()
        self.draw_tree()
        self.draw_snowy_ground()
        self.draw_moon()


if __name__ == "__main__":
    ChristmasDemo()

