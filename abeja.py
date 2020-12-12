class Abeja:
    def __init__(self,color,direccion,genDireccion,angulo,recorrido,distancia):
        self.genColor = genColor #0
        self.genDireccion = genDireccion
        self.color = color # (0,0,0)
        self.direccion = direccion #N,S,O,E .... NE,NO,SE,SO
        self.angulo =  angulo #0
        self.recorrido =  recorrido # [(punto,inicio),ordenrecorrido,random]
        self.distancia =  distancia #0
        self.floresVisitadas = 0
        self.distanciaRecorrida = 0
        self.polenRecogido = []

    def busqueda(self):
        pass





