import numpy as np

""" Make a array
arange(dx) crea un arreglo en fila  de 0 hasta dx-1
reshape(n,m) re-ordena en un arreglo de nxm
"""
print("\n Arreglo a de rango 15")
a = np.arange(15)
print("a="+str(a))

print("\n Se re-ordena a en m,n")
print("amn= "+str(a.reshape(3,5)))


# Array crea un arreglo con la cadena que se le de.
print("\n Crear array con una cadena")
c=np.array([5,6,7])
print(c)

print("\n Para crear un arreglo multidimencionalse una array([(),()]")
d=np.array([(1,2,3),(4,5,6)])
print(d)

print("\n")
print( np.zeros( (2,2) ) )

print("\n")
print( np.ones( (2,2) ) )


print("\n")
print( np.empty( (2,2) ) )

print("\n")
print(np.pi)

print("\n Con linspace(inicila,final,n de elementos)")
x=np.linspace(0,1,10)


a=np.array([-1000,1,-1000,1,-1000])

for i in a:
    print(np.abs(i)**(1/3.))


def f(x,y):
    return 10*x+y

#cosa rara
bb=np.fromfunction(f,(2,3),dtype=int)
print("\n"+str(bb)+"\n")

print(bb[:,0])
