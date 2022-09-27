from tkinter import *

import numpy as np 
raiz=Tk()


miFrame=Frame(raiz)
miFrame.pack()



#--....... cosas

numelement=3#input('Numero de lados de la cuadricula= ')

element=np.arange(1,numelement**2+1)
element[-1]=0

XX=element.reshape(numelement,numelement)
x0=numelement-1
y0=numelement-1
print(x0,y0)
from mod_movimientos import *
#---------- espacio de juego ---------------

boton1=Button(miFrame,text=str(XX[0][0]),width=3,height=2)
boton1.grid(row=2,column=1)

boton2=Button(miFrame,text=str(XX[0][1]),width=3,height=2)
boton2.grid(row=2,column=2)

boton3=Button(miFrame,text=str(XX[0][2]),width=3,height=2)
boton3.grid(row=2,column=3)


boton4=Button(miFrame,text=str(XX[1][0]),width=2,height=2)
boton4.grid(row=3,column=1)

boton5=Button(miFrame,text=str(XX[1][1]),width=3,height=2)
boton5.grid(row=3,column=2)

boton6=Button(miFrame,text=str(XX[1][2]),width=3,height=2)
boton6.grid(row=3,column=3)


boton7=Button(miFrame,text=str(XX[2][0]),width=3,height=2)
boton7.grid(row=4,column=1)

boton8=Button(miFrame,text=str(XX[2][1]),width=3,height=2)
boton8.grid(row=4,column=2)

boton0=Button(miFrame,text=str(XX[2][2]),width=3,height=2,command=mvrigth())
boton0.grid(row=4,column=3)




raiz.mainloop()
