import pygame

pygame.init()

HEIGHT = 700
WIDTH = 1200
FONT = pygame.font.SysFont('comicsans', 40)
WIN_FONT = pygame.font.SysFont('comicsans', 80)


space = pygame.image.load("Oniverse.png")
spacebg = pygame.transform.scale(space, (WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Oniverse Battle")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.color = color
        self.health = 100  
        
        if self.color == "red":
            self.image = pygame.image.load("attack1.png")
            self.image = pygame.transform.scale(self.image, (100, 85))
            self.image = pygame.transform.rotate(self.image, 270)
        else:
            self.image = pygame.image.load("attack2.png")
            self.image = pygame.transform.scale(self.image, (100, 85))
            self.image = pygame.transform.rotate(self.image, 90)
            
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, keys):
        if self.color == "red":
            if keys[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= 5
            if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
                self.rect.y += 5
            if keys[pygame.K_LEFT] and self.rect.left > 610: 
                self.rect.x -= 5
            if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
                self.rect.x += 5

        if self.color == "yellow":
            if keys[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= 5
            if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
                self.rect.y += 5
            if keys[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= 5
            if keys[pygame.K_d] and self.rect.right < 600: 
                self.rect.x += 5

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((50, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        if self.color == "red":
            self.rect.x -= 10
        else:
            self.rect.x += 10
            
        if self.rect.x < 0 or self.rect.x > WIDTH:
            self.kill()

def draw_winner(text):
    draw_text = WIN_FONT.render(text, 1, "white")
    screen.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000) 

red_ship = Player(1100, 350, "red")
yellow_ship = Player(100, 350, "yellow")
players = pygame.sprite.Group(red_ship, yellow_ship)
red_bullets = pygame.sprite.Group()
yellow_bullets = pygame.sprite.Group()

clock = pygame.time.Clock() 
run = True

while run:
    clock.tick(60) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l: 
                bullet = Bullet(red_ship.rect.left, red_ship.rect.centery, "red")
                red_bullets.add(bullet)
            if event.key == pygame.K_LSHIFT:
                bullet = Bullet(yellow_ship.rect.right, yellow_ship.rect.centery, "yellow")
                yellow_bullets.add(bullet)
    for bullet in red_bullets:
        if bullet.rect.colliderect(yellow_ship.rect):
            yellow_ship.health -= 10
            bullet.kill()

    for bullet in yellow_bullets:
        if bullet.rect.colliderect(red_ship.rect):
            red_ship.health -= 10
            bullet.kill()

    screen.blit(spacebg, (0, 0))
    pygame.draw.rect(screen, "white", (600, 0, 10, HEIGHT)) 
    
    red_text = FONT.render(f"Health: {red_ship.health}", 1, "white")
    yellow_text = FONT.render(f"Health: {yellow_ship.health}", 1, "white")
    screen.blit(red_text, (WIDTH - red_text.get_width() - 20, 20))
    screen.blit(yellow_text, (20, 20))

    keys = pygame.key.get_pressed()
    players.update(keys)
    red_bullets.update()
    yellow_bullets.update()
    
    players.draw(screen)
    red_bullets.draw(screen)
    yellow_bullets.draw(screen)

    winner_text = ""
    if red_ship.health <= 0:
        winner_text = "Yellow Wins!"
    if yellow_ship.health <= 0:
        winner_text = "Red Wins!"

    if winner_text != "":
        draw_winner(winner_text)
        break

    pygame.display.update()

pygame.quit()


