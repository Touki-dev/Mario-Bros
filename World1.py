import pyxel
from Mario import *
from Pipe import *

class World1:
    def __init__(self):
        self.pos_camera = [0,0]
        self.floor_y = pyxel.height * 3 / 4  # Position verticale du sol
        self.mario = Mario((pyxel.width / 2 - 18/2, self.floor_y - 16))  # Crée une instance de Mario
        self.background = 12
        self.pipe1 = Pipe(170, self.floor_y - 64, 'world2', self.background)
        self.blocks = [{
            "x": -pyxel.width * 10,
            "y": self.floor_y,
            "w": pyxel.width * 20,
            "h": pyxel.height / 4,
            "col": 4,
            "class": None,
            "arg1": None
        },  # Sol
        {
            "x": 100,
            "y": self.floor_y - 55,
            "w": 30,
            "h": 10,
            "col": 10,
            "class": None,
            "arg1": None
        }, self.pipe1.hit_box]


    def refresh(self):
        """Rafraîchit l'écran en dessinant l'arrière-plan."""
        pyxel.cls(self.background)
        pyxel.blt(self.pos_camera[0] + 15, 15, 1, 0, 0, 48, 24, self.background) # Nuages
        pyxel.blt(self.pos_camera[0] + 160, 50, 1, 48, 0, 32, 24, self.background)
    
    def update(self):
        """Met à jour l'état du jeu."""
        change_world = self.mario.update(self.blocks)
        return self.mario.move_camera(self.pos_camera), change_world

    def draw(self):
        self.refresh()
        for b in self.blocks:
            pyxel.rect(b["x"], b["y"], b["w"], b["h"], b["col"])
        
        self.mario.draw()
        self.pipe1.draw()