import pgzrun
import random
WIDTH=600
HEIGHT=600
def draw():
    screen.fill("black")
    for i in range(20):
        width = 150 - (i * 15)
        height = 50 + (i * 15)
        x = random.randint(0, WIDTH - width)
        y = random.randint(0, HEIGHT - height)
        r1=Rect((400, 200), (width, height))
        r1.center=300, 300
        r=random.randint(50, 255)
        g=random.randint(50, 255)
        b=random.randint(50, 2aaaaa55)
        color=(r, g, b)
        screen.draw.rect(r1, color)
# def update():
#     pass
pgzrun.go()

