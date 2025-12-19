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

# GAME STATE and DRAWING THE HERO

def draw_game():
        screen.clear()
        snake.actor.draw()

# SNAKE (HERO)
class Snake:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = WIDTH // 2
        self.speed = 4

        self.actor = Actor("snake_idle0", (self.x, self.y))

    def update(self):
        if keyboard.left:
            self.x -= self.speed
        if keyboard.right:
            self.x += self.speed
        if keyboard.up:
            self.y -= self.speed
        if keyboard.down:
            self.y += self.speed   

        self.actor.pos = (self.x, self.y)     

def update():
    if game_state == GAME:
        snake.update()

# CREATING THE HERO           
snake = Snake() 







