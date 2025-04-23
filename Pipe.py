import pyxel

class Pipe:
    def __init__(self, x, y, worldDestination, bg):
        pyxel.images[2].load(0, 0, 'Img/pipe.png')
        self.x = x
        self.y = y
        self.hit_box = {
            "x": self.x,
            "y": self.y,
            "w": 32,
            "h": 64,
            "col": bg,
            "class": 'Pipe',
            "destination": worldDestination,
        }

    def draw(self):
        pyxel.blt(self.x, self.y, 2, 0, 0, 32, 64, 12)