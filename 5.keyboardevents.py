import pgzrun
import random
import time

WIDTH=600
HEIGHT=500
game=True
cat=Actor("cat")
cat.pos= 200, 10
mouse=Actor("mouse")
mouse.pos=150, 200
score=0
def timer():
    global game
    game=False
def draw():
    screen.blit("hills", (0,0))
    cat.draw()
    mouse.draw()
    screen.draw.text(str(score), (495,10))
    if game==False:
        screen.fill("red")
        screen.draw.text("You Lose", (300,250))
        screen.draw.text("Your Highscore is: {} ".format(score), (300, 270))
        
def update():
    global score
    if keyboard.w:
        cat.y-=5
    elif keyboard.s:
        cat.y+=5
    elif keyboard.a:
        cat.x-=5
    elif keyboard.d:
        cat.x+=5
        
    if cat.x<=0:
        cat.x=(0+25)
    elif cat.x>=600:
        cat.x=600-25
    elif cat.y>=500:
        cat.y=500-25
    elif cat.y<=0:
        cat.y=0+25
    if cat.colliderect(mouse):
        mouse.x=random.randint(5, 500)
        mouse.y=random.randint(5,600)
        score=score+1
        #print("Your score is:", score)
           
clock.schedule(timer, 10)   
        

pgzrun.go()
    
