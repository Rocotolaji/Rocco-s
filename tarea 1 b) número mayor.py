import random
n1 = random.randint(1,25)
print("Su numero es: ",n1)
n2 = random.randint(1,25)
print("El numero del computador es: ",n2)
if n1 > n2:
    print("usted es el ganador")
if n1 < n2:
    print("el computador es el ganador")
if n1 == n2:
    print("es un empate")
