class Flor:
    def __init__(self,color,posicion,polen):
        self.color = color #(0,0,0)
        self.posicion = posicion #(0,0)
        self.polen = polen #posicion
        self.polenRecogido = []
        self.cantidadVisitas = 0

    # def determinarColor(self,gen):
    #     color = (gen,gen//2,gen//3)
    #     return color
    #
    # def determinarPos(self,gen):
    #     pos = (gen,gen//2)
    #     return pos

    def visitaNueva(self):
        self.cantidadVisitas += 1

    def agregarPolen(self,nuevoPolen):
        self.polenRecogido.append(nuevoPolen)

    def color(self):
        return self.color

    def posicion(self):
        return self.posicion