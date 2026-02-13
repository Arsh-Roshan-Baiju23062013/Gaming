import pygame
import time
WIDTH=700
HEIGHT=700

pygame.init()
r=pygame.image.load("images\Rocket.png")
space=pygame.image.load("images\Space.png")
spacebg=pygame.transform.scale(space, (WIDTH, HEIGHT))
rocket=pygame.transform.scale(r, (50, 70))

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, ):
        super().__init__()
        self.x=x
        self.y=y
        self.image=rocket
        self.rect=self.image.get_rect()
        self.rect.center=self.x, self.y
    def update(self, keys):
        if keys[pygame.K_w]:
            self.rect.y=self.rect.y-5
        if keys[pygame.K_a]:
            self.rect.x=self.rect.x-5
        if keys[pygame.K_s]:
            self.rect.y=self.rect.y+5
        if keys[pygame.K_d]:
            self.rect.x=self.rect.x+5  
     
screen=pygame.display.set_mode((WIDTH, HEIGHT))

Saucer=Spaceship(300, 200)

img=pygame.sprite.Group()
img.add(Saucer)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    if Saucer.rect.y<=0:
        break
    if Saucer.rect.x<=0:
        break
    if Saucer.rect.x>=700:
        break
    if Saucer.rect.y>=700:
        break  
    
    screen.blit(spacebg, (0, 0))
    img.draw(screen)
    Saucer.rect.y+=0.5
    keys=pygame.key.get_pressed()
    img.update(keys)
    pygame.display.update()

font=pygame.font.SysFont("Comic San MS", 48, True, True)
text=font.render("Game Over!", True, "Black")
screen.blit(spacebg, (0, 0))
screen.blit(text, (320, 320))
pygame.display.update()
time.sleep(5)
pygame.quit()
