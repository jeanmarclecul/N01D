import pygame
import sys

sys.path.append("..")
import settings


class ball:
    def __init__(self, xpos, ypos, radius, xspeed, yspeed, color):
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.radius = radius
        self.color = color
        pyball = pygame.Rect(self.xpos, self.ypos, self.radius * 2, self.radius * 2)
        self.pyball = pyball

    def get_xpos(self):
        return self.xpos

    def get_ypos(self):
        return self.ypos

    def get_xspeed(self):
        return self.xspeed

    def get_yspeed(self):
        return self.yspeed

    def get_radius(self):
        return self.radius

    def get_color(self):
        return self.color

    def draw(self, screen):
        pyball = pygame.Rect(self.xpos, self.ypos, self.radius * 2, self.radius * 2)
        self.pyball = pyball
        pygame.draw.ellipse(screen, self.color, pyball)

    def move(self):
        self.xpos += self.xspeed
        self.ypos += self.yspeed
        if self.xpos <= 0 or self.xpos >= settings.WIDTH:
            self.xspeed = -self.xspeed
        if self.ypos <= 0 or self.ypos >= settings.HEIGHT:
            self.yspeed = -self.yspeed
