import os
data = open("nombres.csv") #se importa el archivo
lista=[]
print("funciona") #solo un indicador de que el archivo de ha leido exitosamente, es opcional
print("nombres del curso") #titulo de la lista que se vá a dar
lineas = data.readlines() #código que lee linea a linea y las imprime 
for line in lineas:
    lista.append(line)
    limpio_full=lista[0].replace(",","\n")
    print (limpio_full)
data.close() #cierra el archivo una vez terminado de usarlo 
