import pygame,Constantes

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/spacecraft.png").convert()
        self.image.set_colorkey(Constantes.BLACK)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
        self.rect.y = 500
        self.rect.x = 500



    def changespeed(self, x,y):
        self.speed_x += x
        self.speed_y += y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x >= 1060:
            self.rect.x = 1060
        if self.rect.x <= -10:
            self.rect.x = -10
        if self.rect.y <=0:
            self.rect.y = 0
        if self.rect.y >= 650:
            self.rect.y = 650

