import pygame
pygame.init()
size=(600,600)
dorado=(164,107,2)
rojo=(255,0,0)
amarillo=(255,255,0)
azul=(150,255,255)
cafe=(26,13,0)
negro=(0,0,0)
blanco=(255,255,255)
screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit()

    screen.fill(negro)
    #zona dibujo
    pygame.draw.rect(screen, blanco, pygame.Rect(175, 250, 250, 250))
    pygame.draw.rect(screen, rojo, pygame.Rect(220, 35, 160, 210))
    pygame.draw.rect(screen, rojo, pygame.Rect(195, 195, 210, 55))
    pygame.draw.line(screen, azul, (220,410), (220,499,), 20)
    pygame.draw.line(screen, azul, (380,410), (380,499,), 20)
    pygame.draw.circle(screen, negro, (220,410), 10)
    pygame.draw.circle(screen, negro, (380,410), 10)
    pygame.draw.line(screen, negro, (175,460), (425,460),5)
    pygame.draw.rect(screen, cafe, pygame.Rect(225, 40, 150, 200))
    pygame.draw.rect(screen, cafe, pygame.Rect(200, 200, 200, 50))
    pygame.draw.line(screen, amarillo, (225,187), (375,187),25)
    pygame.draw.rect(screen, dorado, pygame.Rect(280, 170, 40, 30))
    pygame.draw.rect(screen, amarillo, pygame.Rect(290, 180, 20, 20))
    pygame.draw.rect(screen, rojo, pygame.Rect(200, 30, 5, 5))
    pygame.draw.rect(screen, rojo, pygame.Rect(415, 50, 5, 5))
    pygame.draw.rect(screen, rojo, pygame.Rect(300, 10, 5, 5))
    pygame.draw.rect(screen, rojo, pygame.Rect(210, 100, 5, 5))
    pygame.draw.rect(screen, rojo, pygame.Rect(205, 150, 5, 5))
    pygame.draw.rect(screen, rojo, pygame.Rect(195, 180, 5, 5))
    pygame.draw.rect(screen, rojo, pygame.Rect(385, 90, 5, 5))
    pygame.draw.rect(screen, rojo, pygame.Rect(405, 120, 5, 5))
    pygame.draw.rect(screen, rojo, pygame.Rect(395, 160, 5, 5))
    #fin zona dibujo
    pygame.display.flip()