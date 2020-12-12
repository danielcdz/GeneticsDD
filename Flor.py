class Flor:
    def __init__(self,color,genColor,posicion,genPosicion,polen):
        self.genColor = genColor
        self.genPosicion = genPosicion
        self.color = color
        self.posicion = posicion
        self.polen = polen
        self.polenRecogido = []

    def agregarPolen(self,nuevoPolen):
        self.polenRecogido.append(nuevoPolen)

