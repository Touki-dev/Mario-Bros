import pyxel

class Pipe:
    def __init__(self, x, y, worldDestination, bg, rotate=0, scale=1):
        pyxel.images[2].load(0, 0, 'Img/pipe.png')
        self.x = x
        self.y = y
        self.rotate = rotate
        self.scale = scale
        self.hit_box = {
            "x": self.x,
            "y": self.y,
            "w": 32,
            "h": 64,
            "col": None,
            "class": 'Pipe',
            "destination": worldDestination,
        }

    def draw(self):
        pyxel.blt(self.x, self.y, 2, 0, 0, 32, 64, 12, self.rotate, self.scale)