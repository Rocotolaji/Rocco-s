ancho_base = int(input("Ingrese ancho de la base: "))
simbolo = "*"
if  ancho_base > 8 :
    print("El numero ingresado debe ser 8 o menor")
else:
    contador = 0
    while contador < ancho_base:
        triangulo = simbolo*(contador+1)
        print(triangulo)
        contador += 1
