import pygame
pygame.init()
size=(600,400)
verde=(74,255,21)
celeste=(0,210,210)
amarillo=(204,207,69)
azul=(150,255,255)
cafe=(114,85,24)
screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit()

    screen.fill(celeste)
    #zona dibujo
    pygame.draw.rect(screen, verde, pygame.Rect(0, 200, 800, 200))
    pygame.draw.rect(screen, amarillo, pygame.Rect(150, 100, 300, 150))
    pygame.draw.rect(screen, azul, pygame.Rect(325, 125, 75, 75))
    pygame.draw.rect(screen, cafe, pygame.Rect(200, 125, 75, 125))
    pygame.draw.rect(screen, cafe, pygame.Rect(150, 50, 300, 50))
    #fin zona dibujo
    pygame.display.flip()