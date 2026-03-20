import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bahubali's Tiger Escape")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
font = pygame.font.SysFont("Arial", 36)
big_font = pygame.font.SysFont("Arial", 72)

high_score = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"Gaming\Pygames\human.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 10

    def update(self, game_state):
        if game_state == "PLAYING":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
                self.rect.x += self.speed

class Tiger(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"Gaming\Pygames\tiger.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 70))
        self.rect = self.image.get_rect()
        self.reset_pos()

    def reset_pos(self):
        self.rect.y = random.randint(-400, -50)
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.speedy = random.randint(5, 12)

    def update(self, game_state):
        if game_state == "PLAYING":
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT:
                global score
                score += 1
                self.reset_pos()

def run_game():
    global score, high_score
    score = 0
    game_state = "PLAYING" 
    all_sprites = pygame.sprite.Group()
    tigers = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    for i in range(4): 
        t = Tiger()
        all_sprites.add(t)
        tigers.add(t)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False 
            
            if event.type == pygame.KEYDOWN:
                if game_state == "GAME_OVER" and event.key == pygame.K_r:
                    return True 

        if game_state == "PLAYING":
            all_sprites.update(game_state)

            if pygame.sprite.spritecollide(player, tigers, False):
                game_state = "GAME_OVER"
                if score > high_score:
                    high_score = score

        screen.fill(WHITE)
        all_sprites.draw(screen)
        score_surface = font.render(f"Score: {score}  High: {high_score}", True, BLACK)
        screen.blit(score_surface, (10, 10))

        if game_state == "GAME_OVER":
            over_surface = big_font.render("CAUGHT!", True, RED)
            retry_surface = font.render("Press 'R' to Try Again", True, BLACK)
            
            screen.blit(over_surface, (WIDTH//2 - 140, HEIGHT//2 - 50))
            screen.blit(retry_surface, (WIDTH//2 - 130, HEIGHT//2 + 30))

        pygame.display.flip()

continue_playing = True
while continue_playing:
    continue_playing = run_game()

pygame.quit()