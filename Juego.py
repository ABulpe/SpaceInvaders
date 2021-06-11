import pygame,Constantes,random
from Player import *
from Meteor import *
from Laser import  *
class Juego(object):

    def __init__(self):
        self.screen = pygame.display.set_mode([Constantes.ANCHO,Constantes.ALTO])
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.Score = 0
        self.background =pygame.image.load("img/space_backgroud.jpg").convert()
        self.player = Player()
        self.all_sprite_list = pygame.sprite.Group()
        self.meteor_list = pygame.sprite.Group()
        self.laser_list = pygame.sprite.Group()
        self.all_sprite_list.add(self.player)
        for i in range(30):
            meteor = Meteor()
            meteor.rect.x = random.randrange(50, 1050)
            meteor.rect.y = random.randrange(-500, -10)
            self.meteor_list.add(meteor)
            self.all_sprite_list.add(meteor)



    def process_events(self): #Metodo que controla los eventos del juego...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-10,0)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(10,0)
                if event.key == pygame.K_UP:
                    self.player.changespeed(0,-10)
                if event.key == pygame.K_DOWN:
                    self.player.changespeed(0,10)

                if event.key == pygame.K_SPACE:
                    laser = Laser()
                    laser.rect.x = self.player.rect.x + 70
                    laser.rect.y = self.player.rect.y - 20

                    self.all_sprite_list.add(laser)
                    self.laser_list.add(laser)
                    laser.disparo.play()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(10,0)
                if event.key == pygame.K_RIGHT:
                    self.player.changespeed(-10,0)
                if event.key == pygame.K_UP:
                    self.player.changespeed(0,10)
                if event.key == pygame.K_DOWN:
                    self.player.changespeed(0,-10)

    def run_logic(self): #Metodo que controla la logica del juego...
        self.all_sprite_list.update() #Llamada al metodo update de todos los sprite

        for laser in self.laser_list:  # Bucle que controlara los impactos de los laseres y su comportamiento.
            meteor_hit_list = pygame.sprite.spritecollide(laser, self.meteor_list, True)
            for meteor in meteor_hit_list:
                self.all_sprite_list.remove(laser)
                self.laser_list.remove(laser)
                self.Score += 1
                print(self.Score)

            if laser.rect.y == -10:  # Los laser que superen el alto de la pantalla tienen que ser eliminados para que no ocupen espacio en memoria.
                self.all_sprite_list.remove(laser)
                self.laser_list.remove(laser)

    def display_frame(self): #Metodo que controla la pantalla del juego...
        self.screen.blit(self.background, [0, 0])  # Establecemos la pantalla
        self.all_sprite_list.draw(self.screen)  # Pintamos en ella los Sprite
        pygame.display.flip()  # Updatea la pantalla
        self.clock.tick(60)  # Frame por segundo en los que se Updatea
