from  tkinter import *


class Aplicacion:
    def __init__(self):
        self.valor=1
        
        self.ventana1=Tk()
        self.ventana1.title("Control button y label")
        
        self.label1=Label(self.ventana1,text=self.valor)
        self.label1.grid(column=0,row=0)
        self.label1.configure(foreground="red")

        self.boton1=Button(self.ventana1,text='incrementar',command=self.incrementar)
        self.boton1.grid(column=0,row=1)
        
        self.boton2=Button(self.ventana1,text='decrementar',command=self.decrementar)
        self.boton2.grid(column=0,row=2)

        self.ventana1.mainloop()


    def incrementar(self):
        self.valor=self.valor +1
        self.label1.config(text=self.valor)



    def decrementar(self):
        self.valor=self.valor -1
        self.label1.config(text=self.valor)


app=Aplicacion()
