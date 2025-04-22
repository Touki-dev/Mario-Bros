import pyxel, Mario

class Game:
    def __init__(self):
        # Initialise la fenêtre de jeu
        pyxel.init(220, 160, title="Mario Bros")
        pyxel.images[0].load(0, 0, 'Img/marios.png')  # Charge les sprites de Mario

        # Initialise les attributs du jeu
        self.pos_camera = [0,0]
        self.floor_y = pyxel.height * 2 / 3  # Position verticale du sol
        self.mario = Mario(pyxel.width / 2 - 18/2, self.floor_y - 16)  # Crée une instance de Mario
        self.blocks = [
            (-pyxel.width * 10, self.floor_y, pyxel.width * 20, pyxel.height / 3, 4),  # Sol
            (100, self.floor_y - 55, 60, 10, 10),  # Bloc exemple
        ]
        pyxel.run(self.update, self.draw)  # Lance la boucle de jeu

    def refresh(self):
        """Rafraîchit l'écran en dessinant l'arrière-plan."""
        pyxel.cls(12)

    def update(self):
        """Met à jour l'état du jeu."""
        self.mario.update(self.blocks)
        self.pos_camera = Mario.move_camera(self.mario, self.pos_camera)
        pyxel.camera(self.pos_camera[0], self.pos_camera[1])

    def draw(self):
        """Dessine tous les éléments du jeu à l'écran."""
        self.refresh()
        for b in self.blocks:
            pyxel.rect(b[0], b[1], b[2], b[3], b[4])  # Dessine les blocs
        self.mario.draw()  # Dessine Mario

Game()
