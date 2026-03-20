import pygame

pygame.init()

WIDTH = 1150
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
sky = pygame.image.load("backdrop.png")
bg = pygame.transform.scale(sky, (1200, 700))

ground = pygame.image.load("grass.png")
grass = pygame.transform.scale(ground, (1200, 100))
grassx = 0
Game = True

bird1 = pygame.image.load("windgup.png")
bird2 = pygame.image.load("wingdown.png")
bird3 = pygame.image.load("wingmiddle.png")
flappy = [bird1, bird2, bird3]

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        self.images = flappy
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0

    def update(self):
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
    
    screen.blit(bg, (0, 0))
    
    
    bird_group.update()
    bird_group.draw(screen)
    
    screen.blit(grass, (grassx, 625))
    
    if Game == True:
        grassx -= 2 
        if abs(grassx) > 35:
            grassx = 0
            
    pygame.display.update()
    clock.tick(60) 