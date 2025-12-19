# WIDTH = 800
# HEIGHT = 600
# TITLE = "Python Adventure"

# #Game states
# MENU = "menu"
# GAME = "game"

# game_state = MENU
# music_on = True

# #Buttons
# start_button = Rect((300,220), (200, 50))
# music_button = Rect((300,290), (200, 50))
# exit_button = Rect((300,360), (200, 50))

# def draw():
#     screen.clear()

#     if game_state == MENU:
#         draw_menu()
#     elif game_state == GAME:
#         draw_game()

# def draw_menu():
#     screen.draw.text(
#         "PYTHON ADVENTURE",
#         center=(WIDTH // 2, 120),
#         fontsize=60,
#         color="white"
#     )
    
#     draw_button(start_button, "Start Game")
#     draw_button(music_button, f"Music: {'ON' if music_on else 'OFF'}")
#     draw_button(exit_button, "Exit")


# def draw_button(rect, text):
#     screen.draw.filled_rect(rect, (40, 40, 40))
#     screen.draw.rect(rect, "white")
#     screen.draw.text(
#         text,
#         center=rect.center,
#         fontsize=32,
#         color="white"
#     )

#Snake - Hero

def draw_game():
    screen.clear()
    snake.draw()

class Snake:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        self.idle_frames = [
            "snake/idle_0",
            "snake/idle_1",
            "snake/idle_2"
        ]

        self.move_frames = [
            "snake/move_0",
            "snake/move_1",
            "snake/move_2"
        ]

        self.frame_index = 0
        self.animation_timer = 0
        self.speed = 3
        self.moving = False

        self.actor = Actor(self.idle_frames[0], (self.x, self.y))

    def update(self):
        self.moving = False

        if keyboard.left:
            self.x -= self.speed
            self.moving = True

        if keyboard.right:
            self.x += self.speed
            self.moving = True

        self.actor.pos = (self.x, self.y)
        self.animate()

    def animate(self):
        self.animation_timer += 1

        if self.animation_timer >= 10:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % 3

            if self.moving:
                self.actor.image = self.move_frames[self.frame_index]
            else:
                self.actor.image = self.idle_frames[self.frame_index]

    def draw(self):
        self.actor.draw()
        snake = Snake() 

    def update():
        if game_state == GAME:
            snake.update()          

# def on_mouse_down(pos):
#     global game_state, music_on

#     if game_state == MENU:
#         if start_button.collidepoint(pos):
#             game_state = GAME

#         elif music_button.collidepoint(pos):
#             music_on = not music_on

#         elif exit_button.collidepoint(pos):
#             quit()

         