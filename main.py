#Proyecto 3 Analisis de algoritmos
# Daniel Calderon
# Daniel Villatoro

import pygame
import numpy as np
from PIL import Image


imagen1 = np.array(Image.open('fondo.jpg'))

def modificarPixeles():
    # for i in range(100):
    #     for j in range(100):
    #         if j % 2 == 0:
                imagen1[50, 50] = 0


screen_width, screen_height = 250, 120

scaling_factor = 6

x, y = 10, 10
rect_width, rect_height = 2, 2
vel = 2
black = (0, 0, 0)
white = (255, 255, 255)
pygame.init()
win = pygame.display.set_mode((screen_width*scaling_factor, screen_height*scaling_factor))

screen = pygame.Surface((screen_width, screen_height))



run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(white)
    modificarPixeles()
    surface1 = pygame.surfarray.make_surface(imagen1)
    screen.blit(surface1, (0, 0))
    # pygame.draw.rect(screen, white, (x, y, rect_width, rect_height))

    win.blit(pygame.transform.scale(surface1, (600,600)), (0, 0))
    # win.blit(screen, (0, 0))


    pygame.display.update()
pygame.quit()

