#solución problema 4 lab3
import random
dado=random.randint(1,6)
print("se tiene un dado de 6 caras, cual cree usted que va a ser el siguiente número:")
ingreso=int(input())
print(dado)
if dado==ingreso:
    print("ganaste")
elif ingreso>6:
    print("no existe esta cara")
else:
    print("perdiste")
