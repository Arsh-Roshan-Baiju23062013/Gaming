import pygame

pygame.init()
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg_off = pygame.image.load('off.jpg').convert()
bg_on = pygame.image.load('on.jpg').convert()

bg_off = pygame.transform.scale(bg_off, (WIDTH, HEIGHT))
bg_on = pygame.transform.scale(bg_on, (WIDTH, HEIGHT))

is_on = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_on = not is_on 
    if is_on:
        screen.blit(bg_on, (0, 0))
    else:
        screen.blit(bg_off, (0, 0))
    pygame.display.update()

pygame.quit()
