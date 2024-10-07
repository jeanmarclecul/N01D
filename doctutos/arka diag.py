import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BRICK_WIDTH = 60
BRICK_HEIGHT = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arkanoid")

# Ball
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
xspeed = 4
yspeed = -4

# Paddle
paddle_pos = [SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10]

# Bricks
bricks = []
for y in range(5):
    for x in range(SCREEN_WIDTH // BRICK_WIDTH):
        bricks.append(
            pygame.Rect(x * BRICK_WIDTH, y * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT)
        )


def reflect(velocity, normal):
    dot_product = sum(v * n for v, n in zip(velocity, normal))
    return [v - 2 * dot_product * n for v, n in zip(velocity, normal)]


def check_collision(ball_rect, rect):
    global xspeed, yspeed
    dx = ball_rect.centerx - rect.centerx
    dy = ball_rect.centery - rect.centery
    angle = math.atan2(dy, dx)
    if abs(dx) > abs(dy):
        normal = [1 if dx > 0 else -1, 0]
    else:
        normal = [0, 1 if dy > 0 else -1]
    xspeed, yspeed = reflect([xspeed, yspeed], normal)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move ball
    ball_pos[0] += xspeed
    ball_pos[1] += yspeed
    ball_rect = pygame.Rect(
        ball_pos[0] - BALL_RADIUS,
        ball_pos[1] - BALL_RADIUS,
        2 * BALL_RADIUS,
        2 * BALL_RADIUS,
    )

    # Collision with walls
    if ball_rect.left < 0 or ball_rect.right > SCREEN_WIDTH:
        xspeed = -xspeed
    if ball_rect.top < 0 or ball_rect.bottom > SCREEN_HEIGHT:
        yspeed = -yspeed

    # Collision with paddle
    paddle_rect = pygame.Rect(paddle_pos[0], paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT)
    if ball_rect.colliderect(paddle_rect):
        check_collision(ball_rect, paddle_rect)

    # Collision with bricks
    new_bricks = []
    for brick in bricks:
        if ball_rect.colliderect(brick):
            check_collision(ball_rect, brick)
        else:
            new_bricks.append(brick)
    bricks = new_bricks

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, ball_pos, BALL_RADIUS)
    pygame.draw.rect(screen, WHITE, paddle_rect)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
