

class persona:
    """ESTO ES UNA PRUEBA"""
    nombre='aaaaa'
    numero=3
    cosas= True

    def hablar(self,mensaje):
        """Habla lo que quieras"""
        print mensaje


juan=persona


juan.nombre='Juan Gomez'
numero=0
cosas=False

print juan.nombre
print juan.__name__

print juan.__doc__
print juan

#juan.hablar("Dice cosas")
