import pgzrun
import random
WIDTH=512
HEIGHT=512
spaceship=Actor("ship")
pos=(0, 0)
game=True
spaceship.pos=(260, 256)
enemy_images=["greyenemy", "greenenemy", "redenemy", "blueenemy"]
enemies=[]
timer=0
Life=10
Charge=0
d=1
explosions=[]
Attack=False
def draw():
    global timer
    global Life
    global Charge
    global d
    screen.clear()
    screen.blit("map", pos)
    spaceship.draw()
    screen.draw.text("Health:{}".format(Life),(210, 10), color="black")
    screen.draw.text("ENERGY:{}".format(Charge),(210, 30), color="black")   
    if game==True:
        timer=timer+1
        for explosion in explosions:
            explosion.draw()
        if timer%90==0:
            make_enemies()
            timer=0
        for enemy in enemies:
            enemy.draw()
            if Charge%10==0:
                d=d-0.1
            animate(enemy,angle=enemy.angle_to(spaceship.pos)-90, duration=d)  
            animate(enemy, pos=spaceship.pos, duration=2)
            if enemy.colliderect(spaceship)==True:
                if Attack==False:
                    Life=Life-1
                elif Attack==True:
                    Charge=Charge+1
                    if Charge%3==0:
                        Life=Life+1 
                explosion=Actor("explosion1")
                explosions.append(explosion)
                explosion.pos=enemy.pos
                enemies.remove(enemy)    
def update_explosion():
    global explosions
    for explosion in explosions:
        if explosion.image=="explosion1":
            explosion.image=="explosion2"
        elif explosion.image=="explosion2":
            explosion.image=="explosion3"
        elif explosion.image=="explosion3":
            explosion.image=="explosion4"
        elif explosion.image=="explosion4":
            explosion.image=="explosion5"
        elif explosion.image=="explosion5":
            explosion.image=="explosion6"
        elif explosion.image=="explosion6":
            explosions.remove(explosion)
    clock.schedule(update_explosion, 0.1)             
clock.schedule(update_explosion, 0.1)

def attack_end():
    global Attack 
    Attack=False
def on_mouse_down(pos):
    global game
    global Attack
    if game==True:
        animate(spaceship, angle=spaceship.angle_to(pos)-90, duration=0.1)  
        animate(spaceship, pos=pos, duration=1, on_finished=attack_end)
    if Attack==False:
        Attack=True
        
def make_enemies():
    global game
    global enemies
    image=random.choice(enemy_images)
    enemy=Actor(random.choice(enemy_images))
    if image=="redenemy":
        enemy.pos=(0, 544)
    elif image=="blueenemy":
        enemy.pos=(512, 0)
    elif image=="greenenemy":
        enemy.pos=(0, 0)
    elif image=="greyenemy":
        enemy.pos=(512, 544)
    enemies.append(enemy)

pgzrun.go()