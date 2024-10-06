projet jeu arkanoid like rpg

tas de briques fixes
lo. indestructibles
. plusieurs coups
. passage vers niveau suivant
. mangent la balle

raquette styles
. vie = taille de la raquette, possible d’en regagner
. speed
. x et y dans zone limitée 

juballs effects
. multiple
. fire perforant
. fussy
. fantom
. mode berserk 3 sec selon brique spéciale détruite

level design
. scrolling horizontal et vertical
. fond qui rétrécit, obligé de détruire briques spéciales
. déplacements par le joueur quel intérêt ?
. golf avec limite de temps
. tetris : briques qui tombent et restent au sol et bloquent la raquette, au début formes simple unique puis variété avec indication du prochain, musique avant pour teaser
. envoyer la balle a different endroit pour prochain level

boss fights
. multiples raquettes à éliminer
. grosse raquette avec hachoir qui coupe balle
. serpent nibbler

modes de jeux
tout est scale avec niveau de difficulté
niveaux legacy fixes
mode infini avec randomize pour les niveau et les bosses avec scale progressif


















lass player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("bienvenu au joueur {} ayant {} vie et {} attack".format(self.pseudo, self.health, self.attack))
    def get_pseudo(self):
        return self.pseudo
    def get_health(self):
        return self.health
    def get_attack(self):
        return self.attack
    def damage(self, damage):
        self.health -= damage
    def attack_player(self, target_player):
        target_player.damage(self.attack)
    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.attack += weapon.get_damage()
        
class warrior(player):
    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.armor = 3
        print("bienvenu au guerrier {} ayant {} vie {} armure et {} attack".format(self.pseudo, self.health, self.armor,self.attack))
    def damage(self, damage):
        if self.armor > 0:
            self.armor -=1
            damage = 0
        super().damage(damage)
    def blade(self):
        self.armor = 3
        print ("armure rechargée")
    def get_armor_point(self):
        return self.armor


from model.paddle import paddle
import pygame
import sys


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# Constants
WIDTH, HEIGHT = 800, 600




def main():
    # Initialize Pygame
    pygame.init()


    # Create the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("NOID")


    p1_paddle = paddle(100, 100, 7, 1, 50, 5, "player1")
    print(p1_paddle.get_life())


    # Main game loop
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # Clear the screen
        screen.fill(BLACK)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_q]:
            p1_paddle.move("LEFT")
        if keys[pygame.K_d]:
            p1_paddle.move("RIGHT")


        p1_paddle.draw_paddle(screen, BLUE)


        # Update the display
        pygame.display.flip()


        # Cap the frame rate
        clock.tick(60)




if __name__ == "__main__":
    main()




import pygame




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



