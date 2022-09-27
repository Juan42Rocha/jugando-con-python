
# Cliclo para un rango dado un inicio y un final
for i in range(0,3):
    print("Iteration : " +str(i))

print(" ")

# Cliclo con solo el rango
for i in range(3):
    print("Iteration: "+str(i))

print(" ")
# Cliclo sobre una arreglo
for i in [1,3]:  # A esto tambien le llaman lista
    print("Iteration: " + str(i))

print(" ")
# Funciona para cualquier tipo de arreglo
for i  in ["abcd"]:
    print(i+ "\n")

print(" ")
# tambien tenemos while's
icontador = 0
while icontador<3:
    print("El contador es menor a: "+str(icontador))
    icontador +=1   # esto es icontador=icontador+1
    
# Para condicionales nos apoyamos de un while
jcont=0
while jcont<100:
    if jcont<50:
        print("El contador es menor que 50")
    elif jcont<75:
        print("El contador es menro que 75")
    else:
        print("El contador no es ninguno de los anteriores")
    jcont+=1

