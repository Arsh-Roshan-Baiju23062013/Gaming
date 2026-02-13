import pygame
import math
import random

# --- Configuration ---
WIDTH, HEIGHT = 1200, 800
FPS = 60
PLAYER_SPEED = 5
BULLET_SPEED = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
CYAN = (0, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.pos = pygame.math.Vector2(x, y)
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.rect(self.image, CYAN, (0, 0, 40, 40))
        self.rect = self.image.get_rect(center=self.pos)
        self.angle = 0

    def update(self):
        # Movement
        keys = pygame.key.get_pressed()
        move = pygame.math.Vector2(0, 0)
        if keys[pygame.K_w]: move.y -= 1
        if keys[pygame.K_s]: move.y += 1
        if keys[pygame.K_a]: move.x -= 1
        if keys[pygame.K_d]: move.x += 1
        
        if move.length() > 0:
            move = move.normalize() * PLAYER_SPEED
            self.pos += move

        # Rotation toward Mouse
        m_x, m_y = pygame.mouse.get_pos()
        # Adjust mouse pos based on camera if you implement scrolling
        rel_x, rel_y = m_x - self.pos.x, m_y - self.pos.y
        self.angle = math.degrees(math.atan2(-rel_y, rel_x))
        
        self.rect.center = self.pos

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        self.health = 100

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.player = Player(WIDTH//2, HEIGHT//2)
        self.all_sprites = pygame.sprite.Group(self.player)
        self.enemies = pygame.sprite.Group()
        
        # Spawn some test enemies
        for _ in range(5):
            en = Enemy(random.randint(100, 1100), random.randint(100, 700))
            self.enemies.add(en)
            self.all_sprites.add(en)

    def shoot(self):
        """Advanced Hitscan Logic"""
        start_pos = self.player.pos
        mouse_pos = pygame.mouse.get_pos()
        direction = (pygame.math.Vector2(mouse_pos) - start_pos).normalize()
        
        # Check for hits along a line (Simplified Raycast)
        # We check collisions against the enemy rects
        shot_fired = False
        for enemy in self.enemies:
            # Check if the line intersects the enemy's rect
            if enemy.rect.clipline(start_pos, start_pos + direction * 1000):
                enemy.take_damage(50)
                shot_fired = True
        
        # Draw a temporary muzzle flash/tracer
        pygame.draw.line(self.screen, (255, 255, 0), start_pos, start_pos + direction * 1000, 2)

    def run(self):
        while self.running:
            self.screen.fill(BLACK)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.shoot()

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    Game().run()