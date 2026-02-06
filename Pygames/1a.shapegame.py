import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def random_pos():
    return (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

running = True
screen.fill(WHITE) 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            color = random_color()
            pos = random_pos()
            size = random.randint(20, 60)

            if event.key == pygame.K_c:
                pygame.draw.circle(screen, color, pos, size)
            
            elif event.key == pygame.K_s:
                pygame.draw.rect(screen, color, (pos[0], pos[1], size, size))
            
            elif event.key == pygame.K_t:
                pts = [pos, (pos[0] + size, pos[1]), (pos[0] + size // 2, pos[1] - size)]
                pygame.draw.polygon(screen, color, pts)
            
            elif event.key == pygame.K_SPACE:
                screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()