import pygame
import random
WIDTH=700
HEIGHT=700
x=2
pygame.init()

class Circle():
    global x
    def __init__(self, x, y, radius, color):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def up(self):
        self.y=self.y-5
    def down(self):
        self.y=self.y+5
    def left(self):
        self.x=self.x-5
    def right(self):
        self.x=self.x+5
    
    def grow(self):
        self.radius=self.radius+(2*x)
    def change_color(self):
        r=random.randint(120, 255)
        g=random.randint(120, 255)
        b=random.randint(120, 255)
        self.color=(r, g, b)
                

screen=pygame.display.set_mode((WIDTH, HEIGHT))
c1=Circle(300, 300, 50, "Red")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                c1.up() 
            if event.key==pygame.K_s:
                c1.down() 
            if event.key==pygame.K_a:
                c1.left()
            if event.key==pygame.K_d:
                c1.right() 
        if event.type==pygame.MOUSEBUTTONDOWN:
            c1.grow()
        if event.type==pygame.MOUSEBUTTONUP:
            c1.change_color()
        if event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos() 
            xx=pos[0]
            y=pos[1]
            c2=Circle(xx, y, 50, "blue") 
            c2.draw() 
            pygame.display.update()
        if c1.y>=690:
            c1.y=c1.y-100
        elif c1.y<=0:
            c1.y=c1.y+100
        elif c1.x>=700:
            c1.x=c1.x-100
        elif c1.x<=0:
            c1.x=c1.x+100
    screen.fill("Forest Green")
    c1.draw()
    pygame.display.update()
