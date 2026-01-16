import pgzrun
import random

WIDTH = 700
HEIGHT = 700

ship = Actor("space-invaders-ship") 
ship.pos = 350, 630

aliens = []
lasers = []
pows = [] 

alien_types = ["octopus", "space_invaders_alien"]
bullet_image = "bullet"
life = 5
score = 0
alien_speed = 0.6
direction = 1

def spawn():
    if len(aliens) < 12:
        for i in range(6):
            img = "octopus" if i % 2 == 0 else "space_invaders_alien"
            alien = Actor(img)
            alien.x = 80 + (i * 100)
            alien.y = 50
            aliens.append(alien)

def update():
    global life, direction, score, alien_speed
    
    if life <= 0 or score >= 500:
        return

    if keyboard.left or keyboard.a:
        if ship.left > 0:
            ship.x -= 8
        game=True
    if keyboard.right or keyboard.d:
        if ship.right < WIDTH:
            ship.x += 8

    move_down = False
    for alien in aliens:
        alien.x += alien_speed * direction
        if alien.right >= WIDTH or alien.left <= 0:
            move_down = True
    
    if move_down:
        direction *= -1
        for alien in aliens:
            alien.y += 40 

    for bullet in lasers[:]: 
        bullet.y -= 15
        if bullet.y < 0:
            lasers.remove(bullet)
            
    check_collision()

def on_key_down(key):
    global life
    global ship
    if key == keys.SPACE and life > 0:
        bullet = Actor(bullet_image)
        bullet.pos = ship.pos
        lasers.append(bullet)

def draw():
    screen.fill("black")
    ship.draw()
    
    for alien in aliens:
        alien.draw()
    for bullet in lasers:
        bullet.draw()
    
    screen.draw.text(f"Life: {life}", (20, 10), color="cyan", fontsize=35)
    screen.draw.text(f"Score: {score}", (550, 10), color="white", fontsize=35)
    
    if life <= 0:
        screen.draw.text("MISSION FAILED", (WIDTH//2 - 180, HEIGHT//2), color="red", fontsize=70)
    elif score >= 500:
        screen.draw.text("GALAXY SAVED!", (WIDTH//2 - 180, HEIGHT//2), color="gold", fontsize=70)

def check_collision():
    global life, score, alien_speed
    
    for bullet in lasers[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                if alien in aliens: aliens.remove(alien)
                if bullet in lasers: lasers.remove(bullet)
                score += 20
                alien_speed += 0.1 
                break 
                
    for alien in aliens[:]:
        if alien.colliderect(ship):
            aliens.remove(alien)
            life -= 1

clock.schedule_interval(spawn, 5.0)

pgzrun.go()