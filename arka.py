import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 15
BALL_RADIUS = 10
BRICK_WIDTH, BRICK_HEIGHT = 80, 20
BRICK_ROWS, BRICK_COLS = 5, 10
PADDLE_SPEED = 7
BALL_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")

# Paddle
paddle = pygame.Rect(
    WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT
)

# Ball
ball = pygame.Rect(
    WIDTH // 2 - BALL_RADIUS,
    HEIGHT // 2 - BALL_RADIUS,
    BALL_RADIUS * 2,
    BALL_RADIUS * 2,
)
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

# Bricks
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(
            col * (BRICK_WIDTH + 5) + 35,
            row * (BRICK_HEIGHT + 5) + 30,
            BRICK_WIDTH,
            BRICK_HEIGHT,
        )
        bricks.append(brick)

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += PADDLE_SPEED

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx = -ball_dx
    if ball.top <= 0:
        ball_dy = -ball_dy

    # Ball collision with paddle
    if ball.colliderect(paddle) and ball_dy > 0:
        ball_dy = -ball_dy

    # Ball collision with bricks
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy = -ball_dy

    # Ball out of bounds
    if ball.top >= HEIGHT:
        print("Game Over!")
        ball_dy = -ball_dy
        # pygame.quit()
        # sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddle
    pygame.draw.rect(screen, BLUE, paddle)

    # Draw ball
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
