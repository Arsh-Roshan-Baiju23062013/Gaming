import pygame
import time

pygame.init()
pygame.mixer.init()

WIDTH=800
HEIGHT=600
WHITE=(255, 255, 255)
running=True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE) 
font=pygame.font.SysFont("Comic San MS", 48, True, True)
text=font.render("Happy Birthday to YOU", True, "Black")

one=pygame.image.load("Pygames\images\Birthday_border.jpg")
one=pygame.transform.scale(one, (800, 600))
two=pygame.image.load("Pygames\images\cake.jpg")
two=pygame.transform.scale(two, (800, 600))
three=pygame.image.load("Pygames\images\Father's_day_Image.jpg")
three=pygame.transform.scale(three, (800, 600))
four=pygame.image.load("Pygames\images\Fathers_day_cake.png")
four=pygame.transform.scale(four, (800, 600))
five=pygame.image.load("Pygames\images\gift_opening.jpg")
five=pygame.transform.scale(five, (800, 600))
six=pygame.image.load("Pygames\images\party_color_confetti.jpg")
six=pygame.transform.scale(six, (800, 600))
hbd=pygame.mixer.Sound("Pygames\sounds\happy-birthday.mp3")

while running:
    hbd.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(one,(0, 0))
    screen.blit(text, (210, 170))
    pygame.display.flip()
    time.sleep(3)
    screen.blit(two, (0, 0))
    pygame.display.flip()
    time.sleep(3)
    screen.blit(three, (0, 0))
    pygame.display.flip()
    time.sleep(3)
    screen.blit(four, (0, 0))
    pygame.display.flip()
    time.sleep(3)
    screen.blit(five, (0, 0))
    pygame.display.flip()
    time.sleep(3)
    screen.blit(six, (0, 0))
    pygame.display.flip()
    time.sleep(3)


pygame.quit()