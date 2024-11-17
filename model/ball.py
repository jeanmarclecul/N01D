import pygame
import sys
import math

sys.path.append("..")
import settings

ball_color = [
    settings.WHITE,
    settings.GREEN,
    settings.CYAN,
    settings.BLUE,
    settings.RED,
]


class ball:
    def __init__(self, xpos, ypos, radius, xspeed, yspeed, color):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = [xspeed, yspeed]
        self.radius = radius
        self.color = ball_color[color]
        pyball = pygame.Rect(self.xpos, self.ypos, self.radius * 2, self.radius * 2)
        self.pyball = pyball

    def get_xpos(self):
        return self.xpos

    def get_ypos(self):
        return self.ypos

    def get_speed(self):
        return self.speed

    def get_radius(self):
        return self.radius

    def get_color(self):
        return self.color

    def draw(self, screen):
        pyball = pygame.Rect(self.xpos, self.ypos, self.radius * 2, self.radius * 2)
        self.pyball = pyball
        pygame.draw.ellipse(screen, self.color, pyball)

    def bounce(self, axis):
        self.speed[axis] *= -1

    def move(self):
        self.xpos += self.speed[0]
        self.ypos += self.speed[1]
        if self.xpos <= 0 or self.xpos >= settings.WIDTH:
            self.speed[0] = -self.speed[0]
        if self.ypos <= 0 or self.ypos >= settings.HEIGHT:
            self.speed[1] = -self.speed[1]

    def collide(self):
        for onepaddle in settings.paddles:
            if self.pyball.colliderect(onepaddle.pypaddle) and self.ypos > 0:
                # self.speed[1] = -self.speed[1]
                relative_intersect_x = (
                    onepaddle.pypaddle.centerx - self.pyball.centerx
                ) / (onepaddle.xsize / 2)
                bounce_angle = relative_intersect_x * (math.pi / 3)
                speed = math.sqrt(self.speed[0] ** 2 + self.speed[1] ** 2)
                self.speed[0] = -speed * math.sin(bounce_angle)
                self.speed[1] = -speed * math.cos(bounce_angle)
            if self.ypos >= settings.HEIGHT and onepaddle.damage_zone == "BOTTOM":
                onepaddle.damage()
            if self.ypos <= 0 and onepaddle.damage_zone == "TOP":
                onepaddle.damage()
