import pgzrun
import random

WIDTH=300
HEIGHT=300
#Making a sprite
alien=Actor("alien")
alien.pos= 200, 100
def draw():
    screen.fill("white")
    alien.draw()
def set_alien():
    alien.image="alien"  
def set_hurt():
    alien.image="alien_hurt"
    clock.schedule_unique(set_alien, 1)   
def on_mouse_down(pos):
    print(alien.collidepoint(pos))  
    if alien.collidepoint(pos):
        sounds.eep.play()
        set_hurt()
        alien.x=random.randint(20, 290)
        alien.y=random.randint(20, 290)
pgzrun.go()