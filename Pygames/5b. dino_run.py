import pygame

pygame.init()

WIDTH = 1150
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
sky = pygame.image.load("backdrop.png")
bg = pygame.transform.scale(sky, (1200, 700))

ground = pygame.draw.rect(screen, "black", (x, 680, 10, 100))
x = 0
Game = True
Jumping=False

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        self.images = flappy
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0
        self.velocity=0
        self.clicked=False

    def update(self):
        if Flying==True:
            self.velocity+=0.25
            if self.rect.bottom<630:
                self.rect.y+=self.velocity
        if Game==True:
            Key=pygame.key.get_pressed()
            if Key[pygame.K_SPACE] and self.clicked==False:
                self.velocity=-5
                self.clicked=True
            else:
                self.clicked=False
            self.counter += 1
            if self.counter >= 5:
                self.counter = 0   
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]


bird_group = pygame.sprite.Group()
flappy_bird = Bird(100, HEIGHT // 2)
bird_group.add(flappy_bird)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and Game==True and flappy_bird.clicked==False and Flying==False:
                Flying=True

    screen.blit(bg, (0, 0))
    
    bird_group.draw(screen)
    
    screen.blit(grass, (grassx, 625))

    if flappy_bird.rect.bottom>630:
        Game=False
        Flying=False
        
    if Game == True:
        grassx -= 2 
        if abs(grassx) > 35:
            grassx = 0
        if flappy_bird.rect.top<0:
            Game=False
            Flying=False
        bird_group.update()
        


            
    pygame.display.update()
    clock.tick(60) 