import pygame
import sys

sys.path.append("..")
import settings

settings.init()

brick_color = [
    settings.YELLOW,
    settings.GREEN,
    settings.CYAN,
    settings.BLUE,
    settings.RED,
]


class brick:
    def __init__(self, xpos, ypos, xspeed, yspeed, xsize, ysize, life):
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.xsize = xsize
        self.ysize = ysize
        self.life = life
        self.color = brick_color[self.life]
        pybrick = pygame.Rect(self.xpos, self.ypos, self.xsize, self.ysize)
        self.pybrick = pybrick

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

    def draw(self, screen):
        pybrick = pygame.Rect(self.xpos, self.ypos, self.xsize, self.ysize)
        self.pybrick = pybrick
        pygame.draw.rect(screen, self.color, pybrick)

    def damage(self):
        if self.life > 0:
            self.life -= 1
            self.color = brick_color[self.life]

    def collide(self):
        for oneball in settings.balls:
            if self.pybrick.colliderect(oneball.pyball):
                oneball.speed[1] = -oneball.speed[1]
                if self.life > 0:
                    self.damage()
                    self.status()

    def status(self):
        if self.life == 0:
            settings.bricks.remove(self)
