WIDTH = 800
HEIGHT = 600
TITLE = "Python Adventure"

#Game states
MENU = "menu"
GAME = "game"

game_state = MENU
music_on = True

#Buttons
start_button = Rect((300,220), (200, 50))
music_button = Rect((300,290), (200, 50))
exit_button = Rect((300,220), (200, 50))

def draw():
    screen.clear()

    if game_state == MENU:
        draw_menu()
    elif game_state == GAME:
        draw_game()

def draw_menu():
    screen.draw.text(
        "PYTHON ADVENTURE",
        center=(WIDTH // 2, 120),
        fontsize=60,
        color="white"
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


def draw_game():
    screen.draw.text(
        "GAME RUNNING...",
        center=(WIDTH // 2, HEIGHT // 2),
        fontsize=40,
        color="white"
    )


def on_mouse_down(pos):
    global game_state, music_on

    if game_state == MENU:
        if start_button.collidepoint(pos):
            game_state = GAME

        elif music_button.collidepoint(pos):
            music_on = not music_on

        elif exit_button.collidepoint(pos):
            quit()