class Operacion():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2


    def suma(self):
        return self.num1+self.num2

        
    def resta(self):
        return self.num1-self.num2

        
    def multi(self):
        return self.num1*self.num2

        
    def div(self):
        try :
            return float(self.num1)/self.num2
        except:
            return 'no se pudo'

calc=Operacion(1,2)

print(calc.suma())
print(calc.resta())
print(calc.multi())
print(calc.div())
