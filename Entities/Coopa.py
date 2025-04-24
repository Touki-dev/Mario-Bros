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
        self.carapace = False
        self.shot = False

    def to_carapace(self):
        self.carapace = True
        self.frame = 5

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

    def check_collisions(self, x, y, blocks):
        """Vérifie les collisions entre le coopa et les blocs."""
        collisions = []
        for b in blocks:
            if not (b["x"] + b["w"] <= x or b["x"] >= x + self.width or b["y"] + b["h"] <= y or b["y"] >= y + self.height):
                collisions.append(b)
        return collisions

    def update(self, blocks):
        """Met à jour la position et l'état du coopa."""
        if not self.carapace:
            self.change_direction(blocks)
            self.x += 1 * self.dir
            if pyxel.frame_count % 5 == 0:
                self.frame = 1-self.frame
        else:
            self.frame = 5
        if self.shot:
            self.frame = 4
            # Gravité
            if not self.check_collisions(self.x, self.y + self.vertical_speed + GRAVITY, blocks):
                self.vertical_speed += GRAVITY
                self.y += self.vertical_speed
            else:
                self.vertical_speed = 0

            if self.check_collisions(self.x + (self.speed * self.dir), self.y, blocks):
                self.dir = self.dir * -1
            self.x += self.speed * self.dir

    def draw(self):
        """Dessine le coopa à l'écran."""
        pyxel.blt(self.x, self.y, 2, self.frame * (self.width + 2), 64, self.width * -self.dir, self.height, 12)