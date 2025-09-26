import pgzrun
import random

WIDTH=300
HEIGHT=300
#Making a sprite
mole=Actor("mole")
mole.pos= 200, 100
def draw():
    screen.fill("white")
    mole.draw()
def set_mole():
    mole.image="mole"  
def set_hole():
    mole.image="hole"
    clock.schedule_unique(set_mole, 1)   
def on_mouse_down(pos):
    print(mole.collidepoint(pos))  
    if mole.collidepoint(pos):
        sounds.eep.play()
        set_hole()
        mole.x=random.randint(20, 290)
        mole.y=random.randint(20, 290)
pgzrun.go()