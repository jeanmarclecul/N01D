from model.paddle import paddle, player_paddle
from model.ball import ball
from model.brick import brick
from model.brick import brick
import settings
import pygame
import sys
import json, os


settings.init()


def load_level():
    fichier = open("levels/level1.json", "r+")

    # create paddles
    settings.paddles.append(
        player_paddle(
            settings.WIDTH / 2, settings.HEIGHT - 100, 7, 7, 50, 10, 5, "player", 0
        )
    )
    settings.paddles.append(
        paddle(settings.WIDTH / 3, 20, 7, 7, 70, 15, 7, "ennemi1", 1)
    )

    # create balls
    settings.balls.append(ball(200, 300, 8, 5, 5, settings.WHITE))

    # create bricks
    json_bricks = json.load(fichier)["bricks"]
    for one_json_brick in json_bricks:
        settings.bricks.append(
            brick(
                one_json_brick["xpos"],
                one_json_brick["ypos"],
                one_json_brick["xspeed"],
                one_json_brick["yspeed"],
                one_json_brick["xsize"],
                one_json_brick["ysize"],
                one_json_brick["life"],
            )
        )


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def paddles_management():
    for onepaddle in settings.paddles:
        onepaddle.draw(screen)


def balls_management():
    for oneball in settings.balls:
        oneball.collide()
        oneball.move()
        oneball.draw(screen)


def bricks_management():
    for onebrick in settings.bricks:
        onebrick.collide()
        onebrick.status()
        onebrick.draw(screen)


def init_game():
    # Initialize Pygame
    pygame.init()

    # Create the screen
    global screen
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("NOID")

    # Main game loop
    global clock
    clock = pygame.time.Clock()


def clear_screen():
    # Clear the screen
    screen.fill(settings.BLACK)


def key_managment():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_q]:
        settings.paddles[0].move("LEFT")
    if keys[pygame.K_d]:
        settings.paddles[0].move("RIGHT")
    if keys[pygame.K_z]:
        settings.paddles[0].move("UP")
    if keys[pygame.K_s]:
        settings.paddles[0].move("DOWN")


def update_display():
    pygame.display.flip()
    clock.tick(60)


def main():
    init_game()

    load_level()

    while True:
        check_events()

        clear_screen()

        key_managment()

        paddles_management()
        balls_management()
        bricks_management()

        update_display()


if __name__ == "__main__":
    main()
