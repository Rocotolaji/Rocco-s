##para empezar se importa pygame
import pygame

pygame.init()
#se define el tamaño de la pantalla
size = (500, 500)
win = pygame.display.set_mode(size)

#se define las coordenadas, el radio del ciculo, y las velocidades horisontal y vertical para el movimiento
x = 250
y = 250
radius = 15
vel_x = 10
vel_y = 10
#este se utiliza luego en el movimiento 
jump = False
#ver que corra
run = True
#mientras el juego corre 
while run:
    win.fill((0, 0, 0))
    circl=pygame.draw.circle(win, (255, 255, 255), (int(x), int(y)), radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #esto usa los comandos de las flechas laterales para mover a izquierda o derecha
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and x > 0:
        x -= vel_x
    if userInput[pygame.K_RIGHT] and x < 500:
        x += vel_x
    if x > 500:
        x = 0
    if x < 0:
        x = 500

    
    #pequeña "animación extra para la flecha de abajo, el circulo se hace más chico"
    if userInput[pygame.K_DOWN]:
        radius=8   
    else: 
        radius=15
         
    #el salto
    if jump is False and userInput[pygame.K_UP]:
        jump = True
    if jump is True:
        y -= vel_y*4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10
    #se define el suelo
    pygame.draw.rect(win, (0,255,0), pygame.Rect(0, 265, 500, 250))

    #utiliza un delay para hacer que la pelota se mueva más naturalmente y actualiza el tablero
    pygame.time.delay(30)
    pygame.display.update()