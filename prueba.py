import time
import random
class luchador:
    def __init__(self,nombre, vida, daño, velocidad, resistencia, precicion):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.precicion = precicion
    def golpe (self, g):
        if (random.random() <= self.precicion / 100):
            self.vida -= max([self.daño / g.resistencia])
            print("golpe dado exitosamente por", self.nombre)
        else:
            print("golpe errado de", self.nombre)
mult = luchador('MUL_T', 200, 75, 2, 20, 100)
ghost = luchador ('ghost',75, 150, 10, 10, 150)
knight= luchador ('knight', 150, 100, 5, 15, 100)
terrarian= luchador ('terrarian',100, 125, 7, 15, 90)
civilian= luchador ('civilian',50, 50, 1, 10, 60)
lista_luchadores=(mult, ghost, knight, terrarian, civilian)

print("selecciona un personaje: \n \n1: -MUL-T: \n    vida: 200 \n    ataque: 75 \n    velocidad: 2 \n    resistencia: 20 \n \n2: -ghost: \n    vida: 75 \n    daño: 150 \n    velocidad: 10 \n    resistencia: 10 \n")
print("3: -knight: \n    vida: 150 \n    ataque: 100 \n    velocidad: 5 \n    resistencia: 15 \n \n4: -terrarian: \n    vida: 100 \n    attaque: 125 \n    velocidad: 7 \n    resistencia: 15 \n \n5: -civilian \n    vida: 50 \n    daño: 50 \n    velocidad: 1 \n    resistencia: 10")
j_1=int(input())
if j_1 >= 6:
    print("ingrese uno valido")
else:
    j_2=int(input("ingrese segundo personaje: \n"))
    if j_2 >= 6:
        print("ingrese uno valido")
    else:
        print("\n3")
        time.sleep(1)
        print("\n2")
        time.sleep(1)
        print("\n1")
        time.sleep(1)
        print("\nFIGHT")
j1=lista_luchadores[j_1 -1]
j2=lista_luchadores[j_2 -1]
def simular_batalla(j1,j2):
	golpeador,receptor = j1, j2
	if(j1.velocidad < j2.velocidad): 
		golpeador,receptor = j2,j1
	while(j1.vida > 0 and j2.vida > 0):
		print("\n" + j1.nombre,j1.vida,"vs",
					j2.vida,j2.nombre)
		golpeador.golpe(receptor)
		golpeador,receptor = receptor,golpeador
	print("\n" + j1.nombre,j1.vida,"vs",
				j2.vida,j2.nombre)
	print("Ganador:",receptor.nombre)
simular_batalla(j1, j2)
