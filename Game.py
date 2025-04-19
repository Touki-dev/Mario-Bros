import pyxel  # type: ignore

class Mario:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.direction = 1
        self.speed = 2
        self.frame_stop_count = None
        self.vertical_speed = 0
        self.is_jumping = False
        self.jump_strength = 8
        self.gravity = 0.5
        self.width = 18
        self.height = 16

    def check_collisions(self, x, y, blocks):
        collisions = []
        for b in blocks:
            bx, by, bw, bh, _ = b
            if not (bx + bw <= x or bx >= x + self.width or by + bh <= y or by >= y + self.height):
                collisions.append(b)
        return collisions

    def update(self, blocks):
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
            print(self.frame)
        else:
            if self.frame == 4 and pyxel.frame_count - self.frame_stop_count == 10:
                self.frame = 0
        if pyxel.btnr(pyxel.KEY_LEFT) or pyxel.btnr(pyxel.KEY_RIGHT):
            self.frame = 4
            self.frame_stop_count = pyxel.frame_count

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.frame * 18, self.is_jumping * 18, self.direction * 18, 16, 12)

class Game:
    def __init__(self):
        pyxel.init(220, 160, title="Mario Bros")
        pyxel.image(0).load(0, 0, 'Img/marios.png')  # Sprites Mario
        self.floor_y = pyxel.height * 2 / 3
        self.mario = Mario(0, self.floor_y - 16)
        self.blocks = [(0, self.floor_y, pyxel.width, pyxel.height / 3, 4), # floor
                       (100, self.floor_y-20, 60, 20, 10)]
        pyxel.run(self.update, self.draw)

    def refresh(self):
        pyxel.rect(0, 0, pyxel.width, pyxel.height, 12)

    def update(self):
        self.mario.update(self.blocks)

    def draw(self):
        self.refresh()
        for b in self.blocks:
            pyxel.rect(b[0], b[1], b[2], b[3], b[4])
        self.mario.draw()

Game()
