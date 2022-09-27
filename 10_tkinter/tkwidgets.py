#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # Python 2.x
    from Tkinter import *
    from ttk import *
    from tkMessageBox import *
except ImportError:
    # Python 3.x
    from tkinter import *
    from tkinter.ttk import *
    from tkinter.messagebox import *

# Ver http://www.python-course.eu/tkinter_dialogs.php

contador = 0

def contar():
    global contador
    contador += 1
    etiqueta.configure(text=contador)

def saludar():
    showinfo(title='Saludo', message='Hola '+texto.get())

ventana = Tk()

ventana.title('Título de la ventana')
ventana.geometry('300x400')

imagen = PhotoImage(file='imagen.png') # Conseguir una de ejemplo
Label(ventana, image=imagen).grid()

etiqueta = Label(ventana, text='Etiqueta')
etiqueta.grid()

Button(ventana, text='Contar', command=contar).grid()

texto = StringVar()
Entry(ventana, textvariable=texto).grid()

Button(ventana, text='Saludar', command=saludar).grid()

ventana.mainloop()