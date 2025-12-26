import pgzrun
import random

WIDTH = 700
HEIGHT = 700

ship = Actor("r") 
ship.pos = 350, 630

aliens = []
lasers = []
pows = []

alien_types = ["crab", "squid"]
bullet_image = "bullets"
power_images = ["po", "f"]
life = 5
score = 0
alien_speed = 2
direction = 1

def spawn():
    if len(aliens) < 12:
        for i in range(6):
            img = "crab" if i % 2 == 0 else "squid"
            alien = Actor(img)
            alien.x = 80 + (i * 100)
            alien.y = 50
            aliens.append(alien)

def power():
    p = Actor(random.choice(power_images))
    p.x = random.randint(50, 650)
    p.y = -10
    pows.append(p)

def update():
    global life
    global direction
    global score
    global alien_speed
    if keyboard.left or keyboard.a:
        if ship.left > 0:
            ship.x -= 8
    elif keyboard.right or keyboard.d:
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
            
    for bullet in lasers:
        bullet.y -= 15
        if bullet.y < 0:
            lasers.remove(bullet)
    for pow in pows:
        pow.y += 5
        if pow.y > HEIGHT:
            pows.remove(pow)

    check_collision()

def on_key_down(key):
    if key == keys.SPACE:
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
    for pow in pows:
        pow.draw()
    screen.draw.text(f"Life: {life}", (20, 10), color="cyan", fontsize=35)
    screen.draw.text(f"Score: {score}", (550, 10), color="white", fontsize=35)
    
    if life <= 0:
        screen.draw.text("MISSION FAILED", (WIDTH//2 - 180, HEIGHT//2), color="red", fontsize=70)
    elif score >= 500:
        screen.draw.text("GALAXY SAVED!", (WIDTH//2 - 180, HEIGHT//2), color="gold", fontsize=70)

def check_collision():
    global life, score, alien_speed
    for bullet in lasers:
        for alien in aliens:
            if bullet.colliderect(alien):
                aliens.remove(alien)
                lasers.remove(bullet)
                score += 20
                alien_speed += 0.1 
                break
    for alien in aliens:
        if alien.colliderect(ship):
            aliens.remove(alien)
            life -= 1
    for pow in pows:
        if pow.colliderect(ship):
            pows.remove(pow)
            life += 1
clock.schedule_interval(spawn, 5.0)
clock.schedule_interval(power, 8.0)

pgzrun.go()