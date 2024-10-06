from model.paddle import paddle
import pygame
import sys

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Constants
WIDTH, HEIGHT = 800, 600


def main():
    # Initialize Pygame
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("NOID")

    p1_paddle = paddle(100, 100, 7, 1, 50, 5, "player1")
    print(p1_paddle.get_life())

    # Main game loop
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_q]:
            p1_paddle.move("LEFT")
        if keys[pygame.K_d]:
            p1_paddle.move("RIGHT")

        p1_paddle.draw_paddle(screen, BLUE)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)


if __name__ == "__main__":
    main()
