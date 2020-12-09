class Flor:
    def __init__(self,color,posicion,polen):
        self.color = color
        self.posicion = posicion
        self.polen = polen
        self.polenRecogido = []

    def agregarPolen(self,nuevoPolen):
        self.polenRecogido.append(nuevoPolen)

