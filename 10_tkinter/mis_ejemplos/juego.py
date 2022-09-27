from tkinter import *
from mod_movimientos import *

class Nodo:
    
    def __init__(self,value,ant=None,sig=None,up=None,down=None):
        self.value=value
        self.ant=ant
        self.sig=sig
        self.up=up
        self.down=down

    def agregarsig(self,sig):
        self.sig=sig

    def agregarant(self,ant):
        self.ant=ant

    def agregarup(self,up):
        self.up=up

    def agregardown(self,down):
        self.down=down
#------------------------

class Juego():

    def __init__(self):  
        self.nodo1=Nodo(1)
        self.nodo2=Nodo(2)
        self.nodo3=Nodo(3)

        self.nodo4=Nodo(4)
        self.nodo5=Nodo(5)
        self.nodo6=Nodo(6)

        self.nodo7=Nodo(7)
        self.nodo8=Nodo(8)
        self.nodo9=Nodo(0)

        self.XX=np.array([[1,2,3],[4,5,6],[7,8,0]])
        self.x0=2
        self.y0=2
        
        self.nodo1.agregarsig(self.nodo2)
        self.nodo1.agregardown(self.nodo4)
        
        self.nodo2.agregarant(self.nodo1)
        self.nodo2.agregarsig(self.nodo3)
        self.nodo2.agregardown(self.nodo5)

        self.nodo3.agregarant(self.nodo2)
        self.nodo3.agregardown(self.nodo6)

        self.nodo4.agregardown(self.nodo7)
        self.nodo4.agregarsig(self.nodo5)
        self.nodo4.agregarup(self.nodo1)        

        self.nodo5.agregarant(self.nodo4)
        self.nodo5.agregardown(self.nodo8)
        self.nodo5.agregarsig(self.nodo6)
        self.nodo5.agregarup(self.nodo2)

        self.nodo6.agregarant(self.nodo5)
        self.nodo6.agregardown(self.nodo9)
        self.nodo6.agregarup(self.nodo3)

        self.nodo7.agregarsig(self.nodo8)
        self.nodo7.agregarup(self.nodo4)

        self.nodo8.agregarant(self.nodo7)
        self.nodo8.agregarsig(self.nodo9)
        self.nodo8.agregarup(self.nodo5)

        self.nodo9.agregarant(self.nodo8)
        self.nodo9.agregarup(self.nodo6)

        
        self.root=Tk()
        self.root.title("Juego")
        self.miFrame=Frame(self.root)
        self.miFrame.pack()

        
        self.botonmix=Button(self.miFrame,
                             text="Mix",width=2,height=1,
                             command=self.mixernod)
        self.botonmix.grid(row=1,column=1)
        
        self.boton1=Button(self.miFrame,
                           text=self.nodo1.value,width=2,height=2,
                           command=lambda:self.mastermov(self.nodo1))
        self.boton1.grid(row=2,column=1)

        self.boton2=Button(self.miFrame,
                           text=self.nodo2.value,width=2,height=2,
                           command=lambda:self.mastermov(self.nodo2))
        self.boton2.grid(row=2,column=2)

        self.boton3=Button(self.miFrame,
                           text=self.nodo3.value,width=2,height=2,
                           command=lambda:self.mastermov(self.nodo3))
        self.boton3.grid(row=2,column=3)


        self.boton4=Button(self.miFrame,
                           text=self.nodo4.value,width=2,height=2,
                           command=lambda:self.mastermov(self.nodo4))
        self.boton4.grid(row=3,column=1)

        self.boton5=Button(self.miFrame,
                           text=self.nodo5.value,width=2,height=2,
                           command=lambda:self.mastermov(self.nodo5))
        self.boton5.grid(row=3,column=2)

        self.boton6=Button(self.miFrame,
                           text=self.nodo6.value,width=2,height=2,
                           command=lambda:self.mastermov(self.nodo6))
        self.boton6.grid(row=3,column=3)

        self.boton7=Button(self.miFrame,
                           text=self.nodo7.value,width=2,height=2,
                           command=lambda:self.mastermov(self.nodo7))
        self.boton7.grid(row=4,column=1)

        self.boton8=Button(self.miFrame,
                           text=self.nodo8.value,width=2,height=2,
                           command=lambda:self.mastermov(self.nodo8))
        self.boton8.grid(row=4,column=2)

        self.boton9=Button(self.miFrame,
                           text=self.nodo9.value,width=2,height=2,
                           command=lambda:self.mastermov(self.nodo9))
        self.boton9.grid(row=4,column=3)

        
        self.root.mainloop()

        

    def updatebotones(self):
        self.boton1.config(text=self.nodo1.value)
        self.boton2.config(text=self.nodo2.value) 
        self.boton3.config(text=self.nodo3.value)

        self.boton4.config(text=self.nodo4.value)
        self.boton5.config(text=self.nodo5.value) 
        self.boton6.config(text=self.nodo6.value)

        self.boton7.config(text=self.nodo7.value)
        self.boton8.config(text=self.nodo8.value) 
        self.boton9.config(text=self.nodo9.value)
       # print(self.nodo1.value,self.nodo2.value,self.nodo3.value)
       # print(self.nodo4.value,self.nodo5.value,self.nodo6.value)
       # print(self.nodo7.value,self.nodo8.value,self.nodo9.value)
       # print(" ")
        
    def swapsig(self,n1):
        tmp=n1.value
        n1.value=n1.sig.value
        n1.sig.value=tmp
        self.updatebotones()
     
        
    def swapant(self,n1):
        tmp=n1.value
        n1.value=n1.ant.value
        n1.ant.value=tmp
        self.updatebotones()

    def swapdown(self,n1):
        tmp=n1.value
        n1.value=n1.down.value
        n1.down.value=tmp
        self.updatebotones()
     
        
    def swapup(self,n1):
        tmp=n1.value
        n1.value=n1.up.value
        n1.up.value=tmp
        self.updatebotones()
        
    def mastermov(self,n1):
        try:
            if(n1.sig.value==0):
                self.swapsig(n1)
        except:
            a=1
        try:
            if(n1.ant.value==0):
                self.swapant(n1)
        except:
            a=1
        try:
            if(n1.down.value==0):
                self.swapdown(n1)
        except:
            a=1
        try:
            if(n1.up.value==0):
                self.swapup(n1)
        except:
            a=1


    def mixernod(self):
        
        for i in range(500):
            self.nodtoXX()
            self.XX,self.x0,self.y0=mixer(self.XX,self.x0,self.y0)
            self.XXtonod()
            self.updatebotones()


    def nodtoXX(self):
        
        self.XX[0][0]=self.nodo1.value
        self.XX[0][1]=self.nodo2.value
        self.XX[0][2]=self.nodo3.value

        self.XX[1][0]=self.nodo4.value
        self.XX[1][1]=self.nodo5.value
        self.XX[1][2]=self.nodo6.value

        self.XX[2][0]=self.nodo7.value
        self.XX[2][1]=self.nodo8.value
        self.XX[2][2]=self.nodo9.value     

    
    
    def XXtonod(self):
        
        self.nodo1.value=self.XX[0][0]
        self.nodo2.value=self.XX[0][1]
        self.nodo3.value=self.XX[0][2]

        self.nodo4.value=self.XX[1][0]
        self.nodo5.value=self.XX[1][1]
        self.nodo6.value=self.XX[1][2]

        self.nodo7.value=self.XX[2][0]
        self.nodo8.value=self.XX[2][1]
        self.nodo9.value=self.XX[2][2]            

       
#--------MAIN----------------


juego=Juego()



