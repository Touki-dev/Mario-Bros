import pyxel
from Entities.Mario import *
from Entities.Pipe import *
from Entities.Coopa import *

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
            "x": 50,
            "y": self.floor_y - 55,
            "w": 60,
            "h": 10,
            "col": 10,
            "class": None,
            "arg1": None
        }, self.pipe1.hit_box]

        self.coopa = Coopa((self.blocks[1]["x"], self.blocks[1]["y"] - 24), [1])

    def refresh(self):
        """Rafraîchit l'écran en dessinant l'arrière-plan."""
        pyxel.cls(self.background)
        pyxel.blt(self.pos_camera[0] + 15, 15, 1, 0, 0, 48, 24, self.background) # Nuages
        pyxel.blt(self.pos_camera[0] + 160, 50, 1, 48, 0, 32, 24, self.background)
    
    def update(self):
        """Met à jour l'état du jeu."""
        self.coopa.update(self.blocks)
        change_world, damage = self.mario.update(self.blocks, [self.coopa])
        return self.mario.move_camera(self.pos_camera), change_world, damage

    def draw(self):
        self.refresh()
        
        self.mario.draw()
        self.coopa.draw()
        self.pipe1.draw()

        return self.blocks