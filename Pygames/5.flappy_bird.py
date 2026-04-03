import pygame
import random
import time

pygame.init()

WIDTH = 1150
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

sky = pygame.image.load("backdrop.png")
bg = pygame.transform.scale(sky, (1200, 700))

pipe = pygame.image.load("pipe.png")

ground = pygame.image.load("grass.png")
grass = pygame.transform.scale(ground, (1200, 100))
grassx = 0

Game = True
Flying = False
score = 0

font = pygame.font.SysFont("Comic Sans MS", 48, True, True)

bird1 = pygame.image.load("windgup.png")
bird2 = pygame.image.load("wingdown.png")
bird3 = pygame.image.load("wingmiddle.png")
flappy = [bird1, bird2, bird3]

pipe_frequency = 1530
last_pipe = pygame.time.get_ticks() - pipe_frequency


class Pipes(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pipe
        self.rect = self.image.get_rect()
        self.passed = False  # for scoring

        if direction == "top":
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y - 75)

        if direction == "bottom":
            self.rect.topleft = (x, y + 75)

    def update(self):
        self.rect.x -= 4
        if self.rect.x < -100:
            self.kill()


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = flappy
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0
        self.velocity = 0
        self.clicked = False

    def update(self):
        if Flying:
            self.velocity += 0.25
            if self.rect.bottom < 630:
                self.rect.y += self.velocity

        if Game:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not self.clicked:
                self.velocity = -5
                self.clicked = True
            elif not keys[pygame.K_SPACE]:
                self.clicked = False

            # Animation
            self.counter += 1
            if self.counter >= 5:
                self.counter = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]


bird_group = pygame.sprite.Group()
flappy_bird = Bird(100, HEIGHT // 2)
bird_group.add(flappy_bird)

pipe_group = pygame.sprite.Group()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and Game and not flappy_bird.clicked and not Flying:
                Flying = True

    screen.blit(bg, (0, 0))

    pipe_group.draw(screen)
    bird_group.draw(screen)
    screen.blit(grass, (grassx, 625))

    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy_bird.rect.bottom > 630:
        Game = False
        Flying = False

    if Game:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            height = random.randint(-100, 100)
            bottom_pipe = Pipes(WIDTH, HEIGHT // 2 + height, "bottom")
            top_pipe = Pipes(WIDTH, HEIGHT // 2 + height, "top")
            pipe_group.add(bottom_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        grassx -= 2
        if abs(grassx) > 35:
            grassx = 0

        for p in pipe_group:
            if p.rect.right < flappy_bird.rect.left and not p.passed:
                score += 0.5  
                p.passed = True

        bird_group.update()
        pipe_group.update()
    else:
        game_over_text = font.render("Game Over! Press R to Restart", True, "Black")
        screen.blit(game_over_text, (300, 300))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # RESET EVERYTHING
            pipe_group.empty()
            flappy_bird.rect.center = (100, HEIGHT // 2)
            flappy_bird.velocity = 0
            score = 0
            Flying = False
            Game = True

    score_text = font.render(str(int(score)), True, "Black")
    screen.blit(score_text, (50, 50))

    pygame.display.update()
    clock.tick(60)


