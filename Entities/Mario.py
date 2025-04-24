import pyxel
from Constantes import GRAVITY

class Mario:
    def __init__(self, spawnpoint):
        pyxel.images[0].load(0, 0, 'Img/marios.png')
        # Initialise la position de Mario
        self.spawnpoint = spawnpoint
        self.x, self.y = self.spawnpoint
        # Initialise les attributs de Mario
        self.frame = 0  # Frame actuelle de l'animation
        self.direction = 1  # Direction de Mario (1 pour droite, -1 pour gauche)
        self.speed = 2  # Vitesse de déplacement de Mario
        self.frame_stop_count = None  # Compteur pour arrêter l'animation
        self.vertical_speed = 0  # Vitesse verticale de Mario
        self.is_jumping = False  # Indique si Mario est en train de sauter
        self.jump_strength = 8  # Force du saut
        self.width = 16  # Largeur de Mario
        self.height = 16  # Hauteur de Mario
        self.invincibility = 0
        self.show = True

    def check_collisions(self, x, y, blocks):
        """Vérifie les collisions entre Mario et les blocs."""
        collisions = []
        for b in blocks:
            # Vérifie si Mario entre en collision avec un bloc
            if not (b["x"] + b["w"] <= x or b["x"] >= x + self.width or b["y"] + b["h"] <= y or b["y"] >= y + self.height):
                collisions.append(b)
                if b["class"]:
                    if b["class"] == 'Pipe':
                        if (pyxel.floor(y + self.height) == b["y"] or b["y"]+b["h"]-5 <= y <= b["y"]+b["h"]) \
                            and b["x"] <= x <= x + self.width <= b["x"] + b["w"]:
                            self.change_world = b["destination"]
                            self.x, self.y = self.spawnpoint
                            print(b["destination"])
        return collisions

    def move_camera(self, pos_camera):
        if pyxel.width / 3 + pos_camera[0] > self.x:
            pos_camera[0] -= pyxel.width / 3 - abs(pos_camera[0] - self.x)
        elif pyxel.width / 3 * 2 + pos_camera[0] < self.x:
            pos_camera[0] += abs(pos_camera[0] - self.x) - pyxel.width / 3 * 2
            
        if pyxel.height / 3 + pos_camera[1] > self.y:
            pos_camera[1] -= pyxel.height / 3 - abs(pos_camera[1] - self.y)
        elif pyxel.height / 3 * 2 + pos_camera[1] < self.y:
            pos_camera[1] += abs(pos_camera[1] - self.y) - pyxel.height / 3 * 2
            
        return pos_camera

    def collision_mob(self, mobs):
        for m in mobs:
            if not (m["x"] + m["w"] <= self.x or m["x"] >= self.x + self.width or m["y"] + m["h"] <= self.y or m["y"] >= self.y + self.height):
                print(not self.invincibility)
                if not self.invincibility:
                    self.damage = 1
                    self.invincibility = 31

    def update(self, blocks, mobs):
        """Met à jour la position et l'état de Mario."""
        self.change_world = False
        self.damage = 0
        # Logique de saut
        if pyxel.btnp(pyxel.KEY_UP) and self.is_jumping == 0:
            self.is_jumping = 1
            self.vertical_speed = -self.jump_strength

        if self.is_jumping == 1:
            self.vertical_speed += GRAVITY
            self.y += self.vertical_speed

            # Vérifie les collisions avec les blocs
            if self.check_collisions(self.x, self.y, blocks):
                self.y -= self.vertical_speed
                self.vertical_speed = 0
                self.is_jumping = 0
        else:
            # Gravité
            if not self.check_collisions(self.x, self.y + self.vertical_speed + GRAVITY, blocks):
                self.vertical_speed += GRAVITY
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
            self.speed += self.speed/3/30 if self.speed/3/30 <= 3 else 0
            if pyxel.frame_count % 3 == 0:
                self.frame += 1
                if self.frame >= 4:
                    self.frame = 1
        else:
            if self.frame == 4 and pyxel.frame_count - self.frame_stop_count == 10:
                self.frame = 0
        if pyxel.btnr(pyxel.KEY_LEFT) or pyxel.btnr(pyxel.KEY_RIGHT):
            self.frame = 4
            self.frame_stop_count = pyxel.frame_count
            self.speed = 2
        
        self.collision_mob(mobs)
        if self.invincibility:
            if (self.invincibility-1) % 6 == 0:
                print(self.invincibility)
                self.show = not self.show
            self.invincibility -= 1
        return self.change_world, self.damage

    def draw(self):
        """Dessine Mario à l'écran."""
        if self.show:
            pyxel.blt(self.x, self.y, 0, self.frame * (self.width + 2), 0, self.width * self.direction, 16, 12)
