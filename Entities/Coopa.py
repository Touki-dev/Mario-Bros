import pyxel
from Constantes import GRAVITY

class Coopa:
    def __init__(self, spawnpoint, blocks_path):
        pyxel.images[2].load(0, 64, 'Img/coopa.png')
        # Initialise la position du Coopa
        self.spawnpoint = spawnpoint
        self.x, self.y = self.spawnpoint
        # Initialise les attributs du Coopa
        self.blocks_path = blocks_path
        self.frame = 0
        self.dir = 1
        self.speed = 2
        self.frame_stop_count = None
        self.vertical_speed = 0
        self.width = 16
        self.height = 24

    def change_direction(self, blocks):
        def onblock(block):
            if self.dir == 1:
                return self.y + self.height == block["y"] and block["x"] <= self.x + self.width <= block["x"] + block["w"]
            else:
                return self.y + self.height == block["y"] and block["x"] <= self.x <= block["x"] + block["w"]

        for i in self.blocks_path:
            if onblock(blocks[i]):
                return
        self.dir = -self.dir

    def update(self, blocks):
        """Met à jour la position et l'état de Mario."""
        self.change_direction(blocks)
        self.x += 1 * self.dir
        if pyxel.frame_count % 5 == 0:
            self.frame = 1-self.frame

        self.hit_box = {
            "x": self.x,
            "y": self.y,
            "w": self.width,
            "h": self.height,
        }
        return self.hit_box

    def draw(self):
        """Dessine Mario à l'écran."""
        pyxel.blt(self.x, self.y, 2, self.frame * (self.width + 2), 64, self.width * -self.dir, self.height, 12)