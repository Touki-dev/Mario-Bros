import pyxel

class Mario:
    def __init__(self, x, y):
        # Initialise la position de Mario
        self.x = x
        self.y = y

        # Initialise les attributs de Mario
        self.frame = 0  # Frame actuelle de l'animation
        self.direction = 1  # Direction de Mario (1 pour droite, -1 pour gauche)
        self.speed = 2  # Vitesse de déplacement de Mario
        self.frame_stop_count = None  # Compteur pour arrêter l'animation
        self.vertical_speed = 0  # Vitesse verticale de Mario
        self.is_jumping = False  # Indique si Mario est en train de sauter
        self.jump_strength = 8  # Force du saut
        self.gravity = 0.5  # Gravité appliquée à Mario
        self.width = 18  # Largeur de Mario
        self.height = 16  # Hauteur de Mario

    def check_collisions(self, x, y, blocks):
        """Vérifie les collisions entre Mario et les blocs."""
        collisions = []
        for b in blocks:
            bx, by, bw, bh, _ = b
            # Vérifie si Mario entre en collision avec un bloc
            if not (bx + bw <= x or bx >= x + self.width or by + bh <= y or by >= y + self.height):
                collisions.append(b)
        return collisions

    def update(self, blocks):
        """Met à jour la position et l'état de Mario."""
        # Logique de saut
        if pyxel.btnp(pyxel.KEY_UP) and self.is_jumping == 0:
            self.is_jumping = 1
            self.vertical_speed = -self.jump_strength

        if self.is_jumping == 1:
            self.vertical_speed += self.gravity
            self.y += self.vertical_speed

            # Vérifie les collisions avec les blocs
            if self.check_collisions(self.x, self.y, blocks):
                self.y -= self.vertical_speed
                self.vertical_speed = 0
                self.is_jumping = 0
        else:
            # Gravité
            if not self.check_collisions(self.x, self.y + self.vertical_speed + self.gravity, blocks):
                self.vertical_speed += self.gravity
                self.y += self.vertical_speed
            else:
                self.vertical_speed = 0

        # Mouvement horizontal
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_RIGHT):
            self.frame = 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.direction = 1
            if not self.check_collisions(self.x + self.speed, self.y, blocks):
                self.x += self.speed
        if pyxel.btn(pyxel.KEY_LEFT):
            self.direction = -1
            if not self.check_collisions(self.x - self.speed, self.y, blocks):
                self.x -= self.speed
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_RIGHT):
            if self.x % 3 == 0:
                self.frame += 1
                if self.frame >= 4:
                    self.frame = 1
        else:
            if self.frame == 4 and pyxel.frame_count - self.frame_stop_count == 10:
                self.frame = 0
        if pyxel.btnr(pyxel.KEY_LEFT) or pyxel.btnr(pyxel.KEY_RIGHT):
            self.frame = 4
            self.frame_stop_count = pyxel.frame_count

    def draw(self):
        """Dessine Mario à l'écran."""
        pyxel.blt(self.x, self.y, 0, self.frame * 18, 0, 18 * self.direction, 16, 12)

class Game:
    def __init__(self):
        # Initialise la fenêtre de jeu
        pyxel.init(220, 160, title="Mario Bros")
        pyxel.image(0).load(0, 0, 'Img/marios.png')  # Charge les sprites de Mario

        # Initialise les attributs du jeu
        self.floor_y = pyxel.height * 2 / 3  # Position verticale du sol
        self.mario = Mario(0, self.floor_y - 16)  # Crée une instance de Mario
        self.blocks = [
            (0, self.floor_y, pyxel.width, pyxel.height / 3, 4),  # Sol
            (100, self.floor_y - 55, 60, 10, 10)  # Bloc exemple
        ]
        pyxel.run(self.update, self.draw)  # Lance la boucle de jeu

    def refresh(self):
        """Rafraîchit l'écran en dessinant l'arrière-plan."""
        pyxel.rect(0, 0, pyxel.width, pyxel.height, 12)

    def update(self):
        """Met à jour l'état du jeu."""
        self.mario.update(self.blocks)

    def draw(self):
        """Dessine tous les éléments du jeu à l'écran."""
        self.refresh()
        for b in self.blocks:
            pyxel.rect(b[0], b[1], b[2], b[3], b[4])  # Dessine les blocs
        self.mario.draw()  # Dessine Mario

Game()
