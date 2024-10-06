import pygame
import settings


class ball:
    def __init__(self, xpos, ypos, radius, xspeed, yspeed, color):
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.radius = radius
        self.color = color

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

    def draw_ball(self, screen):
        pyball = pygame.Rect(self.xpos, self.ypos, self.radius * 2, self.radius * 2)
        pygame.draw.ellipse(screen, self.color, pyball)
