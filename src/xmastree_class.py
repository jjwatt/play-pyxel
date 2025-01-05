import pyxel
import random


class ChristmasDemo:
    def __init__(self):
        self.width = 256
        self.height = 256
        pyxel.init(self.width,
                   self.height,
                   title="ChristmasDemo")
        pyxel.images[0].load(0, 0, "christmas_tree_w_snow2.png")
        self.snowflakes = []
        self.ornaments = []
        self.current_frame = 0
        self.tree_width = 128
        self.tree_height = 160
        self.initialize_snowflakes()
        pyxel.run(self.update, self.draw)

    def initialize_snowflakes(self):
        """Init snowflakes with random positions"""
        for _ in range(400):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            self.snowflakes.append([x, y])

    def update(self):
        """Update snowflake positions."""
        # update tree sprite
        if pyxel.frame_count % 10 == 0:
            # cycle between the two frames
            self.current_frame = (self.current_frame + 1) % 2

        for snowflake in self.snowflakes:
            snowflake[1] += 1  # move snowflake down
            if snowflake[1] > self.height:  # reset snowflake to the top
                snowflake[0] = random.randint(0, self.width)
                snowflake[1] = 0

    def draw_snowy_ground(self):
        """Draw a snowy ground with random specks of snow."""
        ground_y = self.height - 48  # Height of the ground
        pyxel.rect(0, ground_y, self.width, 60, pyxel.COLOR_WHITE)
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
        # X position for the moon (near top-right corner)
        moon_x = self.width - 50
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
        pyxel.cls(0)

        self.draw_snowy_ground()
        u = self.current_frame * 128
        # Draw the sprite at the x mid-point
        tree_x = (pyxel.width // 2) - (self.tree_width // 2)
        tree_y = (pyxel.height // 2) - 32
        pyxel.blt(tree_x, tree_y, 0, u, 0, 128, 160, 0)
        pyxel.text(5, 5, f"Frame: {self.current_frame}", 7)
        pyxel.text(5, 15, f"Frame Count: {pyxel.frame_count}", 7)
        self.draw_snow()
        self.draw_moon()


if __name__ == "__main__":
    ChristmasDemo()
