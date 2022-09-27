import math as mat

class Figura:
    def __init__(self,snombre,scolor):
        self.scolor=scolor
        self.snombre=snombre

    def getNombre(self):
        print('La figura se llama '+ self.snombre)
        
    def getColor(self):
        print('La figura es de color '+ self.scolor)


class Circulo(Figura):
    def __init__(self,fradio,scolor):
        super().__init__('Circulo',scolor)
        self.fradio=fradio
     
    def getArea(self):
        print('El area es '+ str(3.1415926*self.fradio**2))

    def getPerimetro(self):
        print('El perimetro es '+ str(3.1415926*self.fradio**2))


        
class Cuadrado(Figura):
    def __init__(self,fbase,faltura,scolor):
        super().__init__('Cudrado',scolor)
        self.fbase=fbase
        self.faltura=faltura 
        
    def getArea(self):
        print('El area es '+ str(self.fbase*self.faltura))

    def getPerimetro(self):
        print('El perimetro es '+ str((self.fbase+self.faltura)*2))

        
class TrianguloR(Figura):
    def __init__(self,fbase,faltura,scolor):
        super().__init__('Triangulo',scolor)
        self.fbase=fbase
        self.faltura=fatura 
    def getArea(self):
        print('El area es '+ str(self.fbase*self.faltura/2.0))

    def getPerimetro(self):
        print('El perimetro es '+ str((self.fbase+self.faltura+mat.sqrt(self.fbase**2+self.faltura**2))))     




cir=Circulo(3,'rojo')
cir.getNombre()
cir.getColor()
cir.getArea()
cir.getPerimetro()

cua=Cuadrado(1,2,'verde')
cua.getNombre()
cua.getColor()
cua.getArea()
cua.getPerimetro()

tri=Cuadrado(1,2,'azul')
tri.getNombre()
tri.getColor()
tri.getArea()
tri.getPerimetro()
