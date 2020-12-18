class Flor:
    def __init__(self,color,posicion,polen):
        self.color = color #(0,0,0)
        self.posicion = posicion #(0,0)
        self.polen = posicion #posicion
        self.polenRecogido = []
        self.cantidadVisitas = 0
        self.genes = []

    def setGenes(self):
        R = bin(self.color[0])[2:]
        G = bin(self.color[1])[2:]
        B = bin(self.color[2])[2:]
        X = bin(self.posicion[0])[2:]
        Y = bin(self.posicion[1])[2:]
        self.genes.append(R)
        self.genes.append(G)
        self.genes.append(B)
        self.genes.append(X)
        self.genes.append(Y)

    def getGenes(self):
        return self.genes

    def getVisitas(self):
        return self.cantidadVisitas

    def visitaNueva(self):
        self.cantidadVisitas += 1

    def agregarPolen(self,nuevoPolen):
        self.polenRecogido.append(nuevoPolen)

    def color(self):
        return self.color

    def posicion(self):
        return self.posicion