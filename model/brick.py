import pygame
import sys

sys.path.append("..")
import settings

settings.init()

brick_type = ["basic", "invul"]
brick_color = [
    settings.YELLOW,
    settings.GREEN_LOW,
    settings.GREEN_MID,
    settings.GREEN,
]


class brick:
    def __init__(self, xpos, ypos, xspeed, yspeed, xsize, ysize, life, type):
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.xsize = xsize
        self.ysize = ysize
        self.life = life
        self.color = brick_color[self.life]
        self.type = type

    def get_xpos(self):
        return self.xpos

    def get_ypos(self):
        return self.ypos

    def get_xspeed(self):
        return self.xspeed

    def get_yspeed(self):
        return self.yspeed

    def get_xsize(self):
        return self.xsize

    def get_ysize(self):
        return self.ysize

    def get_life(self):
        return self.life

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def draw(self, screen):
        pybrick = pygame.Rect(self.xpos, self.ypos, self.xsize, self.ysize)
        pygame.draw.rect(screen, self.color, pybrick)
