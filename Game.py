import pyxel
from Worlds.World1 import *
from Worlds.World2 import *

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
        self.mario_health = 3
        self.gameover = False

        pyxel.run(self.update, self.draw)  # Lance la boucle de jeu

    def update(self):
        """Met à jour l'état du jeu."""
        if not self.gameover:
            self.pos_camera, change_world, damage = self.world_active.update()
            self.mario_health -= damage
            if self.mario_health < 0:
                self.gameover = True
            if change_world != False:
                self.world_active = self.worlds[change_world]

            pyxel.camera(self.pos_camera[0], self.pos_camera[1])

    def draw(self):
        """Dessine tous les éléments du jeu à l'écran."""
        if not self.gameover:
            self.blocks = self.world_active.draw()
            for b in self.blocks:
                if b["col"] != None:
                    pyxel.rect(b["x"], b["y"], b["w"], b["h"], b["col"])
            pyxel.text(self.pos_camera[0] + 10, self.pos_camera[1] + 10, f"{self.mario_health} vies", 0)
        else:
            pyxel.cls(0)
            pyxel.camera()
            pyxel.text(pyxel.width/2 - 18, pyxel.height/2 - 6, "GAME OVER", 7)

Game()
