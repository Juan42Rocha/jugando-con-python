import math as mat

class Figura:
    def __init__(self,snombre,scolor):
        self.scolor=snombre
        self.snombre=scolor

    def getNombre(self):
        print('La figura se llama '+ self.snombre)
        
    def getColor(self):
        print('La figura se llama '+ self.scolor)


class Circulo(Figura):
    def __init__(self,fradio):
        self.fradio=fradio

     
    def getArea(self):
        print('El area es '+ str(3.1415926*self.fradio**2))

    def getPerimetro(self):
        print('El perimetro es '+ str(3.1415926*self.fradio**2))

cir=Circulo(3,'Juan','rojo')
