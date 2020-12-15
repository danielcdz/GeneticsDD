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
cantAbejas = 15
matrizFlores = []
colores = []
poblacionAbejas = []
generacion = 0

def busquedaAbejas():
    global poblacionAbejas
    global generacion
    abejas = poblacionAbejas[generacion]
    for abeja in abejas:
        if abeja.getRecorrido()[2] == 1: # random
            recorridoRandom(abeja)
        if abeja.getRecorrido()[0] == 1: # salida desde el panal
            if abeja.getRecorrido()[1] == 1: #recorrido por profundidad
                salirPanal(abeja)
            if abeja.getRecorrido()[1] == 2: #recorrido por anchura
                salirPanal(abeja)
        else:
            if abeja.getRecorrido()[1] == 1:  # recorrido por profundidad
                haciaPanal(abeja)
            if abeja.getRecorrido()[1] == 2:  # recorrido por anchura
                haciaPanal(abeja)


def recorridoRandom(abeja):
    direccion = abeja.getDireccion()
    angulo = abeja.getAngulo()
    distancia = random.randint(80, 250)
    if direccion == 1: #Norte
        recorridoRandomAux(abeja,direccion,angulo,distancia,1,-1)
    if direccion == 2:  # oeste
        recorridoRandomAux(abeja, direccion, angulo, distancia, 1, 1)
    if direccion == 3:  # sur
        recorridoRandomAux(abeja, direccion, angulo, distancia, 1, 1)
    if direccion == 4:  # este
        recorridoRandomAux(abeja, direccion, angulo, distancia, -1, 1)

def recorridoRandomAux(abeja,direccion,angulo,distancia,op1,op2):
    x = 50
    y = 50
    while distancia > 0:
        i = random.randint(1, angulo)
        j = random.randint(1, angulo)
        x = x+(i*op1)
        y = y+(j*op2)
        flor = matrizFlores[x][y]
        if flor != 0:
            flor.visitaNueva()
            flor.agregarPolen(abeja.getPolen())
            abeja.aumentarFloresVisitadas()
            abeja.nuevoPolen((x, y))
        x = 50
        y = 50
        if direccion == 1 or direccion == 3:
            op1 *= -1
        elif direccion == 2 or direccion == 4:
            op2 *= -1
        distancia -= 10


def salirPanal(abeja):
    direccion = abeja.getDireccion()
    angulo = abeja.getAngulo()
    distancia = random.randint(80, 250)
    if direccion == 1: #Norte
        recorrido(abeja,direccion,angulo,distancia, 0, 1, 50, 50,1,-1) # i,j,x,y
    if direccion == 2:  # oeste
        recorrido(abeja,direccion, angulo, distancia, 0, 1, 50, 50,1,1) # i,j,x,y
    if direccion == 3:  # sur
        recorrido(abeja,direccion, angulo, distancia, 0, 1, 50, 50,1,1) # i,j,x,y
    if direccion == 4:  # este
        recorrido(abeja,direccion, angulo, distancia, 0, 1, 50, 50,-1,1) # i,j,x,y
    abeja.setDistancia(distancia)


def recorrido(abeja,direccion,angulo,distancia,i,j,x,y,op1,op2):
    if distancia==0:
        return True
    if x>99 or y>99 or x<0 or y<0:
        i = random.randint(1, angulo)
        j = random.randint(1, angulo)
        if direccion == 1 or direccion == 3:
            op1*=-1
        elif direccion == 2 or direccion == 4:
            op2*=-1
        return recorrido(abeja,direccion,angulo,distancia,i,j,50,50,op1,op2)
    else:
        flor = matrizFlores[x][y]
        if flor != 0:
            flor.visitaNueva()
            flor.agregarPolen(abeja.getPolen())
            abeja.aumentarFloresVisitadas()
            abeja.nuevoPolen((x,y))
        return recorrido(abeja,direccion,angulo,distancia-1,i,j,x+(i*op1),y+(j*op2),op1,op2)



def guardarColores():
    global colores
    for i in range(cantColores):
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

def generacion1Abejas():
    temp = []
    for i in range(cantAbejas):
        color = colores[random.randint(0, 15)]
        direccion = random.randint(1, 4)
        angulo = random.randint(1, 30)
        recorrido = (1,1,random.randint(1, 2))#(random.randint(1, 2),random.randint(1, 2),random.randint(1, 2))
        distancia = random.randint(1,50)
        abeja = Abeja(color,direccion,angulo,recorrido,distancia)
        temp+=[abeja]
    poblacionAbejas.append(temp)


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
                generacion1Abejas()
                busquedaAbejas()
                1+1


    win.fill(white)
    modificarPixeles()
    surface1 = pygame.surfarray.make_surface(imagen1)
    screen.blit(surface1, (0, 0))
    # pygame.draw.rect(screen, white, (x, y, rect_width, rect_height))

    win.blit(pygame.transform.scale(surface1, (600,600)), (30, 30))
    # win.blit(screen, (0, 0))


    pygame.display.update()
pygame.quit()

