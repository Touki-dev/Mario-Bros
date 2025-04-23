import pyxel
from World1 import *
from World2 import *

class Game:
    def __init__(self):
        # Initialise la fenêtre de jeu
        pyxel.init(220, 160, title="Mario Bros")
        # Charge les images
        pyxel.images[1].load(0, 0, 'Img/nuage-1.png')
        pyxel.images[1].load(48, 0, 'Img/nuage-2.png')
        # Initialise les attributs du jeu
        self.worlds = {
            'world1': World1(),
            'world2': World2(),
        }
        self.world_active = self.worlds['world1']

        pyxel.run(self.update, self.draw)  # Lance la boucle de jeu

    def update(self):
        """Met à jour l'état du jeu."""
        self.pos_camera, change_world = self.world_active.update()
        if change_world != False:
            self.world_active = self.worlds[change_world]

        pyxel.camera(self.pos_camera[0], self.pos_camera[1])

    def draw(self):
        """Dessine tous les éléments du jeu à l'écran."""
        self.blocks = self.world_active.draw()
        for b in self.blocks:
            if b["col"] != None:
                pyxel.rect(b["x"], b["y"], b["w"], b["h"], b["col"])

Game()
