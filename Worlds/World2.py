import pyxel
from Entities.Mario import *
from Entities.Pipe import *

class World2:
    def __init__(self):
        self.pos_camera = [0,0]
        self.floor_y = pyxel.height * 3 / 4  # Position verticale du sol
        self.mario = Mario((pyxel.width / 2 - 18/2, self.floor_y - 16))  # Crée une instance de Mario
        self.background = 12
        self.pipe1 = Pipe(0, self.floor_y - 50, False, self.background, rotate=90)
        self.pipe2 = Pipe(170, self.floor_y - 128, 'world1', self.background, rotate=180)
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
        }, self.pipe1.hit_box, self.pipe2.hit_box
        ]

    def refresh(self):
        """Rafraîchit l'écran en dessinant l'arrière-plan."""
        pyxel.cls(self.background)
    
    def update(self):
        """Met à jour l'état du jeu."""
        change_world, damage = self.mario.update(self.blocks, [])
        return self.mario.move_camera(self.pos_camera), change_world, damage

    def draw(self):
        self.refresh()
        
        self.mario.draw()
        self.pipe1.draw()
        self.pipe2.draw()

        return self.blocks