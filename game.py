from maps import level_1, TILE_SIZE

# ======================
# MAPA
# ======================
level_map = level_1

tile_images = {
    "X": "bx",
    "Y": "by",
    ".": "dirt",
    "#": "w",
    "R": "robot2",
    "K": "key",
    "V": "virus2",
    
}

# ======================
# CONFIGURAÇÕES
# ======================
WIDTH = 800
HEIGHT = 600
TITLE = "Python Adventure"

MAP_WIDTH = len(level_map[0]) * TILE_SIZE
MAP_OFFSET_X = (WIDTH - MAP_WIDTH) // 2

MENU = "menu"
GAME = "game"

game_state = MENU
music_on = True

# ======================
# BOTÕES
# ======================
start_button = Rect((300, 220), (200, 50))
music_button = Rect((300, 290), (200, 50))
exit_button = Rect((300, 360), (200, 50))

# ======================
# LISTAS DE OBJETOS
# ======================
bots = []
keys = []
viruses = []

# ======================
# HERO (SNAKE)
# ======================
class Snake:
    def __init__(self):
        self.x = MAP_OFFSET_X + TILE_SIZE * 2
        self.y = TILE_SIZE * 2
        self.speed = 4
        self.moving = False

        self.idle_frames = ["snake_idle0", "snake_idle1"]
        self.move_frames = ["snake_move0", "snake_move1"]

        self.frame_index = 0
        self.frame_timer = 0

        self.actor = Actor(self.idle_frames[0], (self.x, self.y))

    def update(self):
        self.moving = False

        if keyboard.left:
            self.x -= self.speed
            self.moving = True
        if keyboard.right:
            self.x += self.speed
            self.moving = True
        if keyboard.up:
            self.y -= self.speed
            self.moving = True
        if keyboard.down:
            self.y += self.speed
            self.moving = True

        self.animate()
        self.actor.pos = (self.x, self.y)

    def animate(self):
        self.frame_timer += 1

        if self.frame_timer >= 15:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % 2

            if self.moving:
                self.actor.image = self.move_frames[self.frame_index]
            else:
                self.actor.image = self.idle_frames[self.frame_index]


snake = Snake()

# ======================
# CARREGAR MAPA
# ======================
def load_level(level):
    bots.clear()
    keys.clear()
    viruses.clear()

    for row, line in enumerate(level):
        for col, tile in enumerate(line):
            x = MAP_OFFSET_X + col * TILE_SIZE + TILE_SIZE // 2
            y = row * TILE_SIZE + TILE_SIZE // 2

            if tile == "R":
                bots.append(Actor("bot", (x, y)))
            elif tile == "K":
                keys.append(Actor("key", (x, y)))
            elif tile == "V":
                viruses.append(Actor("virus", (x, y)))

# ======================
# DESENHAR MAPA
# ======================

def draw_level(level):
    for row, line in enumerate(level):
        for col, tile in enumerate(line):
            image = tile_images.get(tile)
            if image:
                screen.blit(
                    image,
                    (
                        MAP_OFFSET_X + col * TILE_SIZE,
                        row * TILE_SIZE
                    )
                )

# ======================
# DRAW PRINCIPAL
# ======================
def draw():
    screen.clear()

    if game_state == MENU:
        draw_menu()
    elif game_state == GAME:
        draw_game()

# ======================
# MENU
# ======================
def draw_menu():
    screen.draw.text(
        "Python Adventure",
        center=(WIDTH // 2, 120),
        fontsize=60,
        color="green"
    )

    draw_button(start_button, "Start Game")
    draw_button(music_button, f"Music: {'ON' if music_on else 'OFF'}")
    draw_button(exit_button, "Exit")

def draw_button(rect, text):
    screen.draw.filled_rect(rect, (40, 40, 40))
    screen.draw.rect(rect, "white")
    screen.draw.text(
        text,
        center=rect.center,
        fontsize=32,
        color="white"
    )

# ======================
# GAME
# ======================
def draw_game():
    draw_level(level_map)

    for key in keys:
        key.draw()

    for bot in bots:
        bot.draw()

    for virus in viruses:
        virus.draw()

    snake.actor.draw()

# ======================
# UPDATE
# ======================
def update():
    if game_state == GAME:
        snake.update()

# ======================
# INPUT
# ======================
def on_mouse_down(pos):
    global game_state, music_on

    if game_state == MENU:
        if start_button.collidepoint(pos):
            game_state = GAME
            load_level(level_map)

        elif music_button.collidepoint(pos):
            music_on = not music_on

        elif exit_button.collidepoint(pos):
            quit()
