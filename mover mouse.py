import pygame #se importa pygame

screen = pygame.display.set_mode([720, 720]) #se define el tamaño de la pantalla
clock = pygame.time.Clock()

done = False

background = pygame.image.load("Background_253.png").convert() #se importa un fondo

player = pygame.image.load("hatty.png").convert()
player.set_colorkey([255, 255, 255])                #se importa la imagen y la segunda linea se utiliza para eliminar el fondo (indicando el color que debe ser eliminado)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True             #estas 4 lineas se usan para definir el cierre de la ventana al presionar la X roja

	mouse_pos = pygame.mouse.get_pos() #se establece que la posición de la imagen es igual a la del mouse
	x = mouse_pos[0]
	y = mouse_pos[1]

	screen.blit(background, [0, 0])
	screen.blit(player, [x, y])


	pygame.display.flip() #se actualiza la imagen
	clock.tick(60) #cantidad de veces que esto ocurre (frames por segundo)

pygame.quit() #se cierra el juego
