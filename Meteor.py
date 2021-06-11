import pygame, Constantes,random
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/meteor.png").convert()
        self.image.set_colorkey(Constantes.BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        if self.rect.y > 800:
            self.rect.y = -10
            self.rect.x = random.randrange(50, 1150)
