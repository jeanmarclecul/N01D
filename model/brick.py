import pygame
import settings

brick_type = ["basic", "invul"]


class brick:
    def __init__(self, xpos, ypos, xspeed, yspeed, xsize, ysize, life, color, type):
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.xsize = xsize
        self.ysize = ysize
        self.life = life
        self.color = color
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

    def draw_brick(self, screen):
        pybrick = pygame.Rect(self.xpos, self.ypos, self.xsize, self.ysize)
        pygame.draw.rect(screen, self.color, pybrick)
