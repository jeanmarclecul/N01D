import pygame
import settings


class paddle:
    def __init__(self, xpos, ypos, xspeed, yspeed, size, life, controler):
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.size = size
        self.life = life
        self.controler = controler

    def get_xpos(self):
        return self.xpos

    def get_ypos(self):
        return self.ypos

    def get_speed(self):
        return self.speed

    def get_size(self):
        return self.size

    def get_life(self):
        return self.life

    def get_controler(self):
        return self.controler

    def draw_paddle(self, screen, color):
        pypaddle = pygame.Rect(self.xpos, self.ypos, self.size, 10)
        pygame.draw.rect(screen, color, pypaddle)

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
        if self.xpos > settings.WIDTH:
            self.xpos = settings.WIDTH
        if self.ypos > settings.HEIGHT:
            self.ypos = settings.HEIGHT
