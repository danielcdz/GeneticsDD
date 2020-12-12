#Proyecto 3 Analisis de algoritmos
# Daniel Calderon
# Daniel Villatoro

import pygame
import numpy as np
from PIL import Image
from abeja import *
from flor import *
import  random

imagen1 = np.array(Image.open('fondo.jpg'))
cantFlores = 500
cantColores = 16
matrizFlores = []
colores = []

def guardarColores():
    global colores
    for i in range(cantFlores):
        R = random.randint(1, 255)
        G = random.randint(1, 255)
        B = random.randint(1, 255)
        colores+=[(R,G,B)]


def crearMatrizFlores():
    res = []
    temp = []
    for i in range(100):
        for j in range(100):
            temp+=[0]
        res+=[temp]
        temp=[]
    global matrizFlores
    matrizFlores = res

def generacion1Flores():
    global matrizFlores
    for i in range(cantFlores):
        X = random.randint(0, 99)
        Y = random.randint(0, 99)
        color = colores[random.randint(0, 15)]
        pos = (X, Y )
        flor = Flor(color,pos,[])
        imagen1[pos[0]][pos[1]] = color
        matrizFlores[pos[0]][pos[1]] = flor


def modificarPixeles():
    # for i in range(100):
    #     for j in range(100):
    #         if j % 2 == 0:
                imagen1[50, 50] = 0

# ------------------------------------ PYGAME ------------------------------------------------------
screen_width, screen_height = 110, 110

scaling_factor = 6

x, y = 10, 10
rect_width, rect_height = 2, 2
vel = 2
black = (0, 0, 0)
white = (100, 100, 100)
pygame.init()
win = pygame.display.set_mode((screen_width*scaling_factor, screen_height*scaling_factor))

screen = pygame.Surface((screen_width, screen_height))



run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                guardarColores()
                crearMatrizFlores()
                generacion1Flores()

    win.fill(white)
    modificarPixeles()
    surface1 = pygame.surfarray.make_surface(imagen1)
    screen.blit(surface1, (0, 0))
    # pygame.draw.rect(screen, white, (x, y, rect_width, rect_height))

    win.blit(pygame.transform.scale(surface1, (600,600)), (30, 30))
    # win.blit(screen, (0, 0))


    pygame.display.update()
pygame.quit()

