import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('C:\Users\rocco\Desktop\python\lab10\libro1.xlsx')

#se forman los datos (en este caso siendo al azar)
np.random.seed(3)
x=4+np.random.normal(0,2,24)
y=4+np.random.normal(0,2,len(x))
#se define el tamaño del grafico y los colores que se van a utilizar
sizes=np.random.uniform(15,80,len(x))
colors=np.random.uniform(15,80,len(x))

#cuerpo del grafico, que toma todol sol datos anteriores y forma el grafico con tamaño y color
fig, ax=plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)#define el tipo de grafico que se va a formar

ax.set(xlim=(0, 8), xticks=np.arange(1,8),
       ylim=(0, 8), yticks=np.arange(1,8)) #estas dos lineas ponen los limites de vista de los ejes del grafico

plt.show() #muestra el grafico en la consola
