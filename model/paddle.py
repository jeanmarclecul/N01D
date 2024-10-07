import pygame
import settings


class paddle:
    def __init__(
        self, xpos, ypos, xspeed, yspeed, xsize, ysize, life, controler, color
    ):
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.xsize = xsize
        self.ysize = ysize
        self.life = life
        self.controler = controler
        self.color = color

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

    def get_controler(self):
        return self.controler

    def get_color(self):
        return self.color

    def draw(self, screen):
        pypaddle = pygame.Rect(self.xpos, self.ypos, self.xsize, self.ysize)
        pygame.draw.rect(screen, self.color, pypaddle)

    def move(self, dir):
        if dir == "LEFT":
            self.xpos -= self.xspeed
        if dir == "RIGHT":
            self.xpos += self.xspeed
        if dir == "UP":
            self.ypos -= self.yspeed
        if dir == "DOWN":
            self.ypos += self.yspeed
        if self.xpos < 0:
            self.xpos = 0
        if self.ypos < 0:
            self.ypos = 0
        if self.xpos > settings.WIDTH - self.xsize:
            self.xpos = settings.WIDTH - self.xsize
        if self.ypos > settings.HEIGHT - self.ysize:
            self.ypos = settings.HEIGHT - self.ysize


class player_paddle(paddle):
    def __init__(
        self, xpos, ypos, xspeed, yspeed, xsize, ysize, life, controler, color
    ):
        super().__init__(
            xpos, ypos, xspeed, yspeed, xsize, ysize, life, controler, color
        )
