import pygame
WIDTH=700
HEIGHT=700

pygame.init()

class Rectangle():
    def __init__(self, x, y, width, height, color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def up(self):
        self.y=self.y-5
    def down(self):
        self.y=self.y+5
    def left(self):
        self.x=self.x-5
    def right(self):
        self.x=self.x+5        

screen=pygame.display.set_mode((WIDTH, HEIGHT))
r1=Rectangle(5, 5, 500, 200, "Red")
r2=Rectangle(5, 210, 500, 200, "Black")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                r1.up() 
            if event.key==pygame.K_s:
                r1.down() 
            if event.key==pygame.K_a:
                r1.left()
            if event.key==pygame.K_d:
                r1.right() 
            if event.key==pygame.K_UP:
                r2.up() 
            if event.key==pygame.K_DOWN:
                r2.down() 
            if event.key==pygame.K_LEFT:
                r2.left()
            if event.key==pygame.K_RIGHT:
                r2.right()
        if r1.y>=700:
            r1.y=r1.y-100
        elif r1.y<=0:
            r1.y=r1.y+100
        elif r1.x>=700:
            r1.x=r1.x-100
        elif r1.x<=0:
            r1.x=r1.x+100
        if r2.y>=700:
            r2.y=r2.y-100
        elif r2.y<=0:
            r2.y=r2.y+200
        elif r2.x>=700:
            r2.x=r2.x-100
        elif r2.x<=0:
            r2.x=r2.x+100
    screen.fill("Forest Green")
    r1.draw()
    r2.draw()
    pygame.display.update()
