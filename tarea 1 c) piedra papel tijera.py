P1 = int(input("Jugador 1, ingrese una opcion: \n 1) Piedra \n 2) Papel \n 3) Tijeras \n "))
P2 = int(input("Jugador 2, ingrese una opcion: \n 1) Piedra \n 2) Papel \n 3) Tijeras \n "))
if P1 > 3 :
    print("por favor que jugador 1 elija una opción valida")
if P2 > 3 :
    print("por favor que jugador 2 elija una opción valida")
if P1 == 1:
    if P2 == 1:
        print("Es un empate")
    elif P2 == 2:
        print("El jugador 2 gana")
    elif P2 == 3:
        print("El jugador 1 gana")
elif P1 == 2:
    if P2 == 1:
        print("El jugador 1 gana")
    elif P2 == 2:
        print("Es un empate")
    elif P2 == 3:
        print("El jugador 2 gana")
elif P1 == 3:
    if P2 == 1:
        print("El jugador 2 gana")
    elif P2 == 2:
        print("El jugador 1 gana")
    elif P2 == 3:
         print("Es un empate")
