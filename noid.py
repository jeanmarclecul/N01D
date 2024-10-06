from model.paddle import paddle, player_paddle
from model.ball import ball
import settings
import pygame
import sys


settings.init()


def main():
    # Initialize Pygame
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("NOID")

    # create paddles
    paddles = []
    paddles.append(
        player_paddle(
            settings.WIDTH / 2,
            settings.HEIGHT - 100,
            7,
            7,
            50,
            10,
            5,
            "player",
            settings.BLUE,
        )
    )
    paddles.append(
        paddle(settings.WIDTH / 3, 100, 7, 7, 70, 15, 7, "ennemi1", settings.RED)
    )

    # create balls
    balls = []
    balls.append(ball(200, 200, 10, 5, 5, settings.WHITE))

    # Main game loop
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(settings.BLACK)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_q]:
            paddles[0].move("LEFT")
        if keys[pygame.K_d]:
            paddles[0].move("RIGHT")
        if keys[pygame.K_z]:
            paddles[0].move("UP")
        if keys[pygame.K_s]:
            paddles[0].move("DOWN")

        for onepaddle in paddles:
            onepaddle.draw_paddle(screen)

        for oneball in balls:
            oneball.draw_ball(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)


if __name__ == "__main__":
    main()
