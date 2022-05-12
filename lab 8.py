
import os
data = open("precipitaciones.csv")
print("funciona")
print("Precipitaciones diarias por Estación, primer semestre 2015")
lineas = data.readlines()
for line in lineas:
    limpio = line.strip()
    print (limpio)
data.close()
