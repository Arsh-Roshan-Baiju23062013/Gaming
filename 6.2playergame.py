import pgzrun
import random
import sys

print("Player 1 is the Cat (W, A, S, D).")
print("Player 2 is the Bee (Up, Left, Down, Right).")
print("Catch the mouse to score!")

WIDTH = 600
HEIGHT = 500
GAME_TIME = 15

game = True
scoreplayer1 = 0
scoreplayer2 = 0

cat = Actor("cat")
alien = Actor("bee")
mouse = Actor("mouse")

CAT_START_POS = (200, 10)
BEE_START_POS = (400, 40)
MOUSE_START_POS = (150, 200)

cat.pos = CAT_START_POS
alien.pos = BEE_START_POS
mouse.pos = MOUSE_START_POS

def relocate_mouse():
    """Moves the mouse to a random new position within the screen boundaries."""
    mouse.x = random.randint(0, 500)
    mouse.y = random.randint(0, 400)

def timer():

    global game
    game = False

def reset_game():
    global game, scoreplayer1, scoreplayer2

    scoreplayer1 = 0
    scoreplayer2 = 0
    game = True

    cat.pos = CAT_START_POS
    alien.pos = BEE_START_POS
    mouse.pos = MOUSE_START_POS

    clock.unschedule(timer) 
    clock.schedule(timer, GAME_TIME)
    print("\n--- Game Reset! Start Playing! ---")


def draw():
    if game:
        screen.blit("hills", (0, 0))
        cat.draw()
        mouse.draw()
        alien.draw()
        screen.draw.text(f"P1 (Cat): {scoreplayer1}", (10, 10), color="blue")
        screen.draw.text(f"P2 (Bee): {scoreplayer2}", (WIDTH - 150, 10), color="orange")
    else:
        screen.fill((50, 0, 0))
        center_x = WIDTH // 2
        center_y = HEIGHT // 2
        screen.draw.text("TIME'S UP! GAME OVER", (center_x, center_y - 80), color="white", fontsize=48, center=(center_x, center_y - 80))
        if scoreplayer1 > scoreplayer2:
            winner_text = f"PLAYER 1 (CAT) WINS with {scoreplayer1} points!"
            winner_color = "lime"
        elif scoreplayer2 > scoreplayer1:
            winner_text = f"PLAYER 2 (BEE) WINS with {scoreplayer2} points!"
            winner_color = "yellow"
        else:
            winner_text = "IT'S A TIE!"
            winner_color = "cyan"

        screen.draw.text(winner_text, (center_x, center_y), color=winner_color, fontsize=36, center=(center_x, center_y))
        screen.draw.text("Press 'R' to play again!", (center_x, center_y + 80), color="white", fontsize=30, center=(center_x, center_y + 80))


def update():
    global scoreplayer1, scoreplayer2
    
    if game:
        if keyboard.w: cat.y -= 5
        if keyboard.s: cat.y += 5
        if keyboard.a: cat.x -= 5
        if keyboard.d: cat.x += 5
        if keyboard.up: alien.y -= 5
        if keyboard.down: alien.y += 5
        if keyboard.left: alien.x -= 5
        if keyboard.right: alien.x += 5
        cat.x = max(cat.width // 2, min(cat.x, WIDTH - cat.width // 2))
        cat.y = max(cat.height // 2, min(cat.y, HEIGHT - cat.height // 2))
        alien.x = max(alien.width // 2, min(alien.x, WIDTH - alien.width // 2))
        alien.y = max(alien.height // 2, min(alien.y, HEIGHT - alien.height // 2))
        if cat.colliderect(mouse):
            relocate_mouse() 
            scoreplayer1 += 1 
        if alien.colliderect(mouse):
            relocate_mouse()
            scoreplayer2 += 1
            
def on_key_down(key):
    if not game and key == keys.R:
        reset_game()
clock.schedule(timer, GAME_TIME)

pgzrun.go()