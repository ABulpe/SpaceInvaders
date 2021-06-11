import pygame,Constantes,Juego

pygame.init()

juego = Juego.Juego()
pygame.mouse.set_visible(0)

while not juego.game_over:
    juego.process_events()
    juego.run_logic()
    juego.display_frame()


pygame.quit()