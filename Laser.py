import Constantes,pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/laser.png").convert()
        self.image.set_colorkey(Constantes.BLACK)
        self.rect = self.image.get_rect()
        self.disparo = pygame.mixer.Sound("music/laser5.ogg")
    def update(self):
        self.rect.y -= 20