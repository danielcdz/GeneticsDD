# Proyecto 3 Analisis de algoritmos
# Daniel Calderon
# Daniel Villatoro

import pygame
import numpy as np
from PIL import Image
from abeja import *
from flor import *
import random
import time

imagen1 = np.array(Image.open('fondo.jpg'))
cantFlores = 500
cantColores = 16
cantAbejas = 16
matrizFlores = []
colores = []
poblacionAbejas = []
generacion = 0
promediosAdaptabilidad = []
poblacionesFlores = [] #historial del campo de flores
floresXCruces = [] #flores seleccionadas para cruzar
floresNOCruces = [] #flores no visitadas
porcentajeSeleccionAbejas = 40
porcentajeSeleccionFlores = 30
porcentajeMutacion = 15
cantGeneraciones = 20




def cruces():
    global generacion
    seleccionAbejas = cantAbejas * porcentajeSeleccionAbejas // 100
    seleccionFlores = cantFlores * porcentajeSeleccionFlores // 100
    cruceFlores(seleccionFlores)
    cruceAbejas(seleccionAbejas)



def cruceFlores(indiceSeleccion):
    flores = poblacionesFlores[generacion]
    floresSeleccionadas = flores[indiceSeleccion:]  #
    cantNoSeleccionadas = indiceSeleccion
    cantSeleccionadas = len(floresSeleccionadas)
    posPadre = 0
    posMadre = 1
    temp = []
    while posMadre <= cantFlores-1:
        padre = flores[posPadre]
        madre = flores[posMadre]
        if posMadre == cantSeleccionadas:
            padre = flores[random.randint(0, cantSeleccionadas)]
            madre = flores[random.randint(0, cantSeleccionadas)]
        genesPadre = padre.getGenes()
        genesMadre = madre.getGenes()
        cromosomasCruce = random.randint(1, 4)
        genPadre = genesPadre[cromosomasCruce]
        genMadre = genesMadre[cromosomasCruce]
        genesPadre[cromosomasCruce] = genMadre
        genesMadre[cromosomasCruce] = genPadre

        # Hijo 1
        R1 = int(genesMadre[0], 2)
        G1 = int(genesMadre[1], 2)
        B1 = int(genesMadre[2], 2)
        color1 = (R1, G1, B1)
        X1 = int(genesMadre[3], 2)
        Y1 = int(genesMadre[4], 2)
        pos1 = (X1,Y1)

        # Hijo 2
        R2 = int(genesPadre[0], 2)
        G2 = int(genesPadre[1], 2)
        B2 = int(genesPadre[2], 2)
        color2 = (R1, G1, B1)
        X2 = int(genesPadre[3], 2)
        Y2 = int(genesPadre[4], 2)
        pos2 = (X1, Y1)

        flor1 = Flor(color1, pos1, [])
        flor1.setGenes()

        flor2 = Flor(color2, pos2, [])
        flor2.setGenes()

        temp += [flor1]
        temp += [flor2]

        posPadre += 2
        posMadre += 2
    poblacionesFlores.append(temp)


def mutacionFlores():
    flores = poblacionAbejas[generacion]
    indiceMutacion = cantFlores * porcentajeMutacion // 100
    cantMutadas = 0
    while cantMutadas <= indiceMutacion:
        flor = flores[random.randint(0,len(flores)-1)]
        flor.mutacion()
        cantMutadas+=1


def cruceAbejas(indiceSeleccion):
    abejas = poblacionAbejas[generacion]
    abejasSeleccionadas = abejas[indiceSeleccion:] #abejas seleccionadas para el cruce
    cantNoSeleccionadas = indiceSeleccion
    cantSeleccionadas = len(abejasSeleccionadas)
    posPadre=0
    posMadre=1
    temp=[]

    while posMadre<=cantAbejas-1:
        padre = abejas[posPadre]
        madre = abejas[posMadre]
        if posMadre == cantSeleccionadas:
            padre = abejas[random.randint(0,cantSeleccionadas)]
            madre = abejas[random.randint(0,cantSeleccionadas)]
        genesPadre = padre.getGenes()
        genesMadre = madre.getGenes()
        cromosomasCruce = random.randint(1,4)
        genPadre = genesPadre[cromosomasCruce]
        genMadre = genesMadre[cromosomasCruce]
        genesPadre[cromosomasCruce] = genMadre
        genesMadre[cromosomasCruce] = genPadre

        # Hijo 1
        R1 = int(genesMadre[0],2)
        G1 = int(genesMadre[1],2)
        B1 = int(genesMadre[2],2)
        color1 = (R1,G1,B1)
        direccion1 = int(genesMadre[3],2)
        angulo1 = int(genesMadre[4],2)
        recorrido1 = (1, 1, random.randint(1, 2))
        distancia1 = random.randint(1, 50)

        # Hijo 2
        R2 = int(genesPadre[0],2)
        G2 = int(genesPadre[1],2)
        B2 = int(genesPadre[2],2)
        color2 = (R2,G2,B2)
        direccion2 = int(genesPadre[3],2)
        angulo2 = int(genesPadre[4],2)
        recorrido2 = (1, 1, random.randint(1,2))
        distancia2 = random.randint(1, 50)

        abeja1 =Abeja(color1, direccion1, angulo1, recorrido1, distancia1)
        abeja1.setGenes()
        abeja1.setPadres((generacion,posPadre),(generacion,posMadre))
        abeja1.setAncestros(padre.getAncestros())

        abeja2 = Abeja(color2, direccion2, angulo2, recorrido2, distancia2)
        abeja2.setGenes()
        abeja2.setPadres((generacion,posPadre),(generacion,posMadre))
        abeja2.setAncestros(madre.getAncestros())

        temp += [abeja1]
        temp += [abeja2]

        posPadre+=2
        posMadre+=2

    poblacionAbejas.append(temp)

def mutacionAbejas():
    abejas = poblacionAbejas[generacion]
    indiceMutacion = cantAbejas * porcentajeMutacion // 100
    cantMutadas = 0
    while cantMutadas <= indiceMutacion:
        abeja = abejas[random.randint(0,len(abejas)-1)]
        abeja.mutacion()
        cantMutadas+=1


def agruparFlores():
    cruce = []
    noCruce = []
    poblacion = []
    for i in matrizFlores:
        for j in i:
            if j != 0:
                poblacion += [j]
                if j.getVisitas() != 0:
                    cruce += [j]
                else:
                    noCruce += [j]
    poblacionesFlores.append(poblacion)
    floresXCruces.append(cruce)
    floresNOCruces.append(noCruce)

def ordenarFloresCruce():
    flores = poblacionesFlores[generacion]
    n = len(flores)
    flores = quickSortFlores(flores,0,n-1)

#tomado de: https://www.geeksforgeeks.org/python-program-for-quicksort/
# Python program for implementation of Quicksort Sort
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partitionFlores(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high].getVisitas()  # pivot
    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j].getVisitas() <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index
# Function to do Quick sort
def quickSortFlores(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partitionFlores(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        quickSortFlores(arr, low, pi - 1)
        quickSortFlores(arr, pi + 1, high)


def calcularDistanciaXFlores():
    abejas = poblacionAbejas[generacion]
    for abeja in abejas:
        flores = abeja.getCantidadFlores()
        distanciaRecorrida = abeja.getDistanciaRecorrida()
        valor = flores / distanciaRecorrida
        abeja.setDistanciaXFlores(valor)

def ordenarAbejas():
    # global poblacionAbejas
    abejas = poblacionAbejas[generacion]
    n = len(abejas)
    abejas = quickSortAbejas(abejas,0,n-1)

def sumatoriaAdaptabilidad():
    global promediosAdaptabilidad
    res = 0
    abejas = poblacionAbejas[generacion]
    for abeja in abejas:
        valor = abeja.getDistanciaXFlores()
        res+=valor
    promediosAdaptabilidad+=[res]

def asignarAdaptabilidadNormalizada():
    abejas = poblacionAbejas[generacion]
    promedio = promediosAdaptabilidad[generacion]
    for abeja in abejas:
        valor = abeja.getDistanciaXFlores()
        adaptabilidadNormalizada = valor/promedio
        abeja.setAdaptabilidad(adaptabilidadNormalizada)


#tomado de: https://www.geeksforgeeks.org/python-program-for-quicksort/
# Python program for implementation of Quicksort Sort
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partitionAbejas(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high].getDistanciaXFlores()  # pivot
    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j].getDistanciaXFlores() <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index
# Function to do Quick sort
def quickSortAbejas(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partitionAbejas(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        quickSortAbejas(arr, low, pi - 1)
        quickSortAbejas(arr, pi + 1, high)


def busquedaAbejas():
    global poblacionAbejas
    global generacion
    abejas = poblacionAbejas[generacion]
    for abeja in abejas:
        if abeja.getRecorrido()[2] == 1:  # random
            recorridoRandom(abeja)
        if abeja.getRecorrido()[0] == 1:  # salida desde el panal
            if abeja.getRecorrido()[1] == 1:  # recorrido por profundidad
                salirPanal(abeja)
            if abeja.getRecorrido()[1] == 2:  # recorrido por anchura
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
    if direccion == 1:  # Norte
        recorridoRandomAux(abeja, direccion, angulo, distancia, 1, -1)
    if direccion == 2:  # oeste
        recorridoRandomAux(abeja, direccion, angulo, distancia, 1, 1)
    if direccion == 3:  # sur
        recorridoRandomAux(abeja, direccion, angulo, distancia, 1, 1)
    if direccion == 4:  # este
        recorridoRandomAux(abeja, direccion, angulo, distancia, -1, 1)


def recorridoRandomAux(abeja, direccion, angulo, distancia, op1, op2):
    x = 50
    y = 50
    while distancia > 0:
        i = random.randint(1, angulo)
        j = random.randint(1, angulo)
        x = x + (i * op1)
        y = y + (j * op2)
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
    if direccion == 1:  # Norte
        recorrido(abeja, direccion, angulo, distancia, 0, 1, 50, 50, 1, -1)  # i,j,x,y
    if direccion == 2:  # oeste
        recorrido(abeja, direccion, angulo, distancia, 0, 1, 50, 50, 1, 1)  # i,j,x,y
    if direccion == 3:  # sur
        recorrido(abeja, direccion, angulo, distancia, 0, 1, 50, 50, 1, 1)  # i,j,x,y
    if direccion == 4:  # este
        recorrido(abeja, direccion, angulo, distancia, 0, 1, 50, 50, -1, 1)  # i,j,x,y
    abeja.setDistancia(distancia)


def recorrido(abeja, direccion, angulo, distancia, i, j, x, y, op1, op2):
    if distancia == 0:
        return True
    if x > 99 or y > 99 or x < 0 or y < 0:
        i = random.randint(1, angulo)
        j = random.randint(1, angulo)
        if direccion == 1 or direccion == 3:
            op1 *= -1
        elif direccion == 2 or direccion == 4:
            op2 *= -1
        return recorrido(abeja, direccion, angulo, distancia, i, j, 50, 50, op1, op2)
    else:
        flor = matrizFlores[x][y]
        if flor != 0:
            flor.visitaNueva()
            flor.agregarPolen(abeja.getPolen())
            abeja.aumentarFloresVisitadas()
            abeja.nuevoPolen((x, y))
        return recorrido(abeja, direccion, angulo, distancia - 1, i, j, x + (i * op1), y + (j * op2), op1, op2)


def guardarColores():
    global colores
    for i in range(cantColores):
        R = random.randint(1, 255)
        G = random.randint(1, 255)
        B = random.randint(1, 255)
        colores += [(R, G, B)]

def limpiarMatrices():
    global matrizFlores
    for i in range(0,100):
        for j in range(0,100):
            matrizFlores[i][j] = 0
            imagen1[i][j] = (255,255,255)

def actualizarMatrizFlores():
    for flor in poblacionesFlores[generacion]:
        x,y = flor.getPos()
        matrizFlores[x][y] = flor
        imagen1[x][y] = flor.getColor()


def crearMatrizFlores():
    res = []
    temp = []
    for i in range(100):
        for j in range(100):
            temp += [0]
        res += [temp]
        temp = []
    global matrizFlores
    matrizFlores = res


def generacion1Flores():
    global matrizFlores
    for i in range(cantFlores):
        X = random.randint(0, 99)
        Y = random.randint(0, 99)
        while not disponible(X,Y):
            X = random.randint(0, 99)
            Y = random.randint(0, 99)
        color = colores[random.randint(0, 15)]
        pos = (X, Y)
        flor = Flor(color, pos, [])
        flor.setGenes()
        imagen1[pos[0]][pos[1]] = color
        matrizFlores[pos[0]][pos[1]] = flor

def disponible(x,y):
    if matrizFlores[x][y] == 0:
        return True
    return False

def generacion1Abejas():
    temp = []
    for i in range(cantAbejas):
        color = colores[random.randint(0, 15)]
        direccion = random.randint(1, 4)
        angulo = random.randint(1, 30)
        recorrido = (1, 1, random.randint(1,2))  # (random.randint(1, 2),random.randint(1, 2),random.randint(1, 2)) #(1,1,random.randint(1, 2))
        distancia = random.randint(1, 50)
        abeja = Abeja(color, direccion, angulo, recorrido, distancia)
        abeja.setGenes()
        # abeja.setPadres((-1,-1))
        # abeja.setAncestros([])
        temp += [abeja]
    poblacionAbejas.append(temp)


def ciclo():
    global generacion
    busquedaAbejas()
    calcularDistanciaXFlores()
    ordenarAbejas()
    sumatoriaAdaptabilidad()
    asignarAdaptabilidadNormalizada()
    agruparFlores()
    ordenarFloresCruce()
    cruces()
    mutacionAbejas()
    # mutacionFlores()
    limpiarMatrices()
    actualizarMatrizFlores()
    generacion += 1


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
win = pygame.display.set_mode((screen_width * scaling_factor, screen_height * scaling_factor))

screen = pygame.Surface((screen_width, screen_height))

# modificarPixeles()
contGeneraciones = 0
run = True
flagInicio = False
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
                flagInicio = True
                # inicio
                1 + 1

    # time.sleep(1)
    # guardarColores()
    # crearMatrizFlores()
    # generacion1Flores()
    # generacion1Abejas()

    if flagInicio:
        if contGeneraciones <= cantGeneraciones:
            ciclo()
            contGeneraciones+=1
            time.sleep(1)

    1+1
    win.fill(white)
    surface1 = pygame.surfarray.make_surface(imagen1)
    screen.blit(surface1, (0, 0))
    # pygame.draw.rect(screen, white, (x, y, rect_width, rect_height))

    win.blit(pygame.transform.scale(surface1, (600, 600)), (30, 30))
    # win.blit(screen, (0, 0))

    pygame.display.update()
pygame.quit()
