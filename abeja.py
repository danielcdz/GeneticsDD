import random
class Abeja:
    def __init__(self,color,direccion,angulo,recorrido,distancia):
        self.color = color # (0,0,0)
        self.direccion = direccion #N,S,O,E .... NE,NO,SE,SO
        self.angulo =  angulo #0
        self.recorrido =  recorrido # (['1 iniciar en el panal 2 iniciar lejos'],['1 anchura 2 profundidad'],['random'])
        self.distancia =  distancia #0
        self.floresVisitadas = 0
        self.distanciaRecorrida = 0
        self.polenRecogido = []
        self.adaptabilidadNormalizada = 0
        self.distanciaXflores = 0
        self.genes = []
        self.padres = []
        self.ancestros = []
        self.mutada = False


    def setPadres(self,padre,madre):
        self.padres.append((padre))
        self.padres.append((madre))

    def setAncestros(self,ancestros):
        self.ancestros.append(self.padres[0])
        self.ancestros.append(self.padres[1])
        for ancestro in ancestros:
            self.ancestros.append(ancestro)

    def getAncestros(self):
        return self.ancestros

    def getPadres(self):
        return self.padres

    def mutacion(self):
        direcciones = ['0001','0010','0011','0100']
        self.genes[3] = direcciones[random.randint(0,3)]
        # colores = self.genes[0]
        R = self.genes[0][::-1]
        G = self.genes[1][::-1]
        B = self.genes[2][::-1]
        # colores = (R,G,B)
        self.genes[0] = R
        self.genes[1] = G
        self.genes[2] = B
        angulo = self.genes[4]
        self.genes[4] = angulo[::-1]
        self.angulo = int(angulo[::-1],2)
        self.color = (int(R,2),int(G,2),int(B,2))
        self.direccion = int(self.genes[3],2)
        self.mutada = True


    def getGenes(self):
        return self.genes

    def setGenes(self):
        R = bin(self.color[0])[2:]
        G = bin(self.color[1])[2:]
        B = bin(self.color[2])[2:]
        direccion = bin(self.direccion)[2:]
        angulo = bin(self.angulo)[2:]
        self.genes.append(R)
        self.genes.append(G)
        self.genes.append(B)
        self.genes.append(direccion)
        self.genes.append(angulo)


    def setDistanciaXFlores(self,valor):
        self.distanciaXflores = valor

    def getDistanciaXFlores(self):
        return self.distanciaXflores

    def getPolen(self):
        return self.polenRecogido

    def getRecorrido(self):
        return self.recorrido

    def setDistancia(self,distancia):
        self.distanciaRecorrida = distancia

    def getDireccion(self):
        return self.direccion

    def getAngulo(self):
        return self.angulo

    def getDistancia(self):
        return self.distancia

    def setAdaptabilidad(self,valor):
        self.adaptabilidadNormalizada = valor

    def adaptabilidad(self):
        return self.adaptabilidadNormalizada

    def nuevoPolen(self,polen):
        self.polenRecogido.append(polen)

    def aumentarFloresVisitadas(self):
        self.floresVisitadas += 1

    def setDistanciaRecorrida(self,distancia):
        self.distanciaRecorrida = distancia

    def getDistanciaRecorrida(self):
        return self.distanciaRecorrida

    def getCantidadFlores(self):
        return self.floresVisitadas






