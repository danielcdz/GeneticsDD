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






