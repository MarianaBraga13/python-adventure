from maps import level_1, TILE_SIZE

level_map = level_1

# CENARIO
tile_images = {
    "#": "border",
    ".": "dirt",
    "K": "key",
    "R": "bot",
    "M": "mouse",
    "V": "virus",
    "*": "wall"
}

WIDTH=800
HEIGHT=600
TITLE="Python Adventure"

#GAME STATES
MENU="menu"
GAME="game"

#MENU STATE
game_state=MENU
music_on=True

#BUTTONS
start_button = Rect((300,220), (200, 50))
music_button = Rect((300,290), (200, 50))
exit_button = Rect((300,360), (200, 50))

def draw():
    if game_state == MENU:
        draw_menu()
    elif game_state == GAME:
        draw_game()

# MENU
def draw_menu():
    screen.draw.text(
        "Python Adventure",
        center=(WIDTH // 2, 120),
        fontsize=60,
        color="green"
    )        

# DRAWING BUTTONS
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

# MENU CONTROLS
def on_mouse_down(pos):
    global game_state, music_on

    if game_state == MENU:
        if start_button.collidepoint(pos):
            game_state = GAME

        elif music_button.collidepoint(pos):
            music_on = not music_on

        elif exit_button.collidepoint(pos):
            quit()
# CENARIO

def draw_level(level):
    # CHÃO
    for row_index, row in enumerate(level):
        for col_index, tile in enumerate(row):
            if tile == ".":
                screen.blit("dirt", (col_index * TILE_SIZE, row_index * TILE_SIZE))

    # PAREDES
    for row_index, row in enumerate(level):
        for col_index, tile in enumerate(row):
            if tile == "#":
                screen.blit("border", (col_index * TILE_SIZE, row_index * TILE_SIZE))
bots = []
keys = []
viruses = []

def load_level(level):
    bots.clear()
    keys.clear()
    viruses.clear()

    for row, line in enumerate(level):
        for col, tile in enumerate(line):
            x = col * TILE_SIZE + TILE_SIZE // 2
            y = row * TILE_SIZE + TILE_SIZE // 2

            if tile == "R":
                bots.append(Actor("bot", (x, y)))
            elif tile == "K":
                keys.append(Actor("key", (x, y)))
            elif tile == "V":
                viruses.append(Actor("virus", (x, y)))              

# GAME STATE and DRAWING THE HERO

# def draw_ground():
#     for row_index, row in enumerate(level_map):
#         for col_index, tile in enumerate(row):
#             if tile == ".":
#                 screen.blit(
#                     "dirt",
#                     (col_index * TILE_SIZE, row_index * TILE_SIZE)
#                 )

# def draw_walls():
#     for row_index, row in enumerate(level_map):
#         for col_index, tile in enumerate(row):
#             if tile == "#":
#                 screen.blit(
#                     "border",
#                     (col_index * TILE_SIZE, row_index * TILE_SIZE)
#                 )
                
def draw_game():
    screen.clear()

    draw_level(level_map)

    for key in keys:
        key.draw()

    for bot in bots:
        bot.draw()

    for virus in viruses:
        virus.draw()

    snake.actor.draw()    
        

# SNAKE (HERO)
class Snake:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = WIDTH // 2
        self.speed = 4
        self.move = False
        self.jumping = False
        self.underground = True

        # IDLE FRAMES
        self.idle_frames = [
            "snake_idle0",
            "snake_idle1",
        ]

        # MOVE FRAMES --> <--
        self.move_frames = [
            "snake_move0",
            "snake_move1"
        ]

        # JUMP FRAMES ^ 

        self.jump_frames = [
            "snake_jump0",
            "snake_jump1"
        ]

        self.frame_index = 0
        self.frame_timer = 0

        # GRAVITY
        self.vy = 0
        self.gravity = 0.8
        self.jump_strength = -14
        self.on_ground = True

        # GROUND
        self.ground_y = HEIGHT -80
        self.y = self.ground_y

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
        if keyboard.space and self.on_ground:
            self.vy = self.jump_strength
            self.on_ground = False
            self.vy += self.gravity
            self.y += self.vy
        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.vy = 0
            self.on_ground = True

        self.animate()   
        self.actor.pos = (self.x, self.y)

    # ANIMATion
    def animate(self):
        self.frame_timer +=1

        if self.frame_timer >=15:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % 2
            
            if not self.on_ground:
                self.actor.image = self.jump_frames[self.frame_index]

            if self.moving:
                self.actor.image = self.move_frames[self.frame_index]
            else:
                self.actor.image = self.idle_frames[self.frame_index]


def update():
    if game_state == GAME:
        snake.update()

# CREATING THE HERO           
snake = Snake() 







