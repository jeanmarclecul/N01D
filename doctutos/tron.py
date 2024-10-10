import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tron Light Cycles")

# Colors
COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (128, 0, 0),
    (0, 128, 0),
    (0, 0, 128),
    (128, 128, 0),
]


# Player class
class Player:
    def __init__(self, x, y, color, is_ai=True):
        self.x = x
        self.y = y
        self.color = color
        self.is_ai = is_ai
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

    def move(self):
        if self.is_ai:
            # Simple AI: randomly change direction occasionally
            if random.random() < 0.05:
                self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.x += self.direction[0]
        self.y += self.direction[1]


# Create players
players = [
    Player(random.randint(0, WIDTH), random.randint(0, HEIGHT), COLORS[i], i != 0)
    for i in range(10)
]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not players[0].is_ai:
            if event.key == pygame.K_UP:
                players[0].direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                players[0].direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                players[0].direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                players[0].direction = (1, 0)

    # Move players
    for player in players:
        player.move()

    # Draw
    for player in players:
        pygame.draw.rect(screen, player.color, (player.x, player.y, 2, 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
