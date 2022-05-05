import time
import random
class luchador:
    #primero se define cómo serán las estadisticas de los luchadores
    def __init__(self,nombre, vida, daño, velocidad, resistencia, precicion):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.precicion = precicion
    def golpe (self, g):
        #luego se define la acción que va a definir el juego, el golpe
        if (random.random() <= self.precicion / 100):
            #random.random se utiliza para definir la probabilidad de que una accion pase, es enste caso que acierte, utilizando la precision dividiendola por 100 para obtener un porcentaje
            g.vida -= max([self.daño / g.resistencia])
            print("\ngolpe dado exitosamente por", self.nombre)
        else:
            print("\ngolpe errado de", self.nombre)
def simular_batalla(j1,j2):
    #ahora, se crea el cuerpo del juego, las interacciones
	golpeador,receptor = j1, j2
	if(j1.velocidad < j2.velocidad): 
		    golpeador,receptor = j2,j1
            #esto define que el que tiene la mayor velocidad es quien ataca primero
	while(j1.vida > 0 and j2.vida > 0):
		    print(j1.nombre,j1.vida,"vs",j2.vida,j2.nombre)
		    golpeador.golpe(receptor)
		    golpeador,receptor = receptor,golpeador
            #y aqui se le dice al programa que al terminar la interaccion los roles se revierten
	print(j1.nombre,j1.vida,"vs",j2.vida,j2.nombre)
	print("\nGanador:",receptor.nombre)
    #y finalmente, cuando uno de los luchadores se ha quedado sin vida se anuncia el ganador, que es el que dió el golpe final
mult = luchador('MUL_T', 200, 75, 2, 40, 100)
ghost = luchador ('ghost',75, 150, 10, 20, 150)
knight= luchador ('knight', 150, 100, 5, 30, 100)
terrarian= luchador ('terrarian',100, 125, 7, 30, 90)
civilian= luchador ('civilian',50, 50, 1, 1, 75)
lista_luchadores=(mult, ghost, knight, terrarian, civilian)
#estas 6 listas muestran las estadisticas de los 5 luchadores y una lista de los 5 juntos para usarse en la seleccion de personaje
print("selecciona un personaje: \n \n1: -MUL-T: \n    vida: 200 \n    ataque: 75 \n    velocidad: 2 \n    resistencia: 40 \n    precision: 100% \n \n2: -ghost: \n    vida: 75 \n    daño: 150 \n    velocidad: 10 \n    resistencia: 20 \n    precision: 150%\n")
print("3: -knight: \n    vida: 150 \n    ataque: 100 \n    velocidad: 5 \n    resistencia: 30\n    precision: 100% \n \n4: -terrarian: \n    vida: 100 \n    attaque: 125 \n    velocidad: 7 \n    resistencia: 30 \n    precision: 90%\n \n5: -civilian \n    vida: 50 \n    daño: 50 \n    velocidad: 1 \n    resistencia: 1\n    precision: 75%")
#se muestra al jugador los luchadores y sus estadisticas
j_1=int(input())
if j_1 >= 6:
    print("ingrese uno valido")
else:
    j_2=int(input("ingrese segundo personaje: \n"))
    if j_2 >= 6:
        print("ingrese uno valido")
        #y aquí se verifica si el numero de luchador ingresado es valido
    else:
        print("\n3")
        time.sleep(1)
        print("\n2")
        time.sleep(1)
        print("\n1")
        time.sleep(1)
        print("\nFIGHT")
        time.sleep(1)
        #aquí se tiene un pequeño contador para iniciar
j1=lista_luchadores[j_1 -1]
j2=lista_luchadores[j_2 -1]
#se le dice al programa quienes van a luchar
simular_batalla(j1, j2)
#y finalmente se inicia el combate