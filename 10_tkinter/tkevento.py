#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

ventana = Tk()

def boton(evento):
    print "Puntero en", str(evento.x), str(evento.y)

marco = Frame(ventana, width=640, height=480)
marco.bind("<Button-1>", boton)
marco.pack()

ventana.mainloop()