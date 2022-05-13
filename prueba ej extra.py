import pygame
pygame.init()
size=(600,400)
cafe=(114,85,24)
azul=(24,239,234)
verde=(74,255,21)
hatty=pygame.image.load('hatty.jpg')
hattyX=200
hattyY=100
screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit()

    screen.fill(azul)
    #zona dibujo
    pygame.draw.rect(screen, verde, pygame.Rect(0, 200, 800, 200))
    pygame.draw.rect(screen, cafe, pygame.Rect(195, 95, 210, 210))
    screen.blit(hatty, (hattyX,hattyY))
    #fin zona dibujo
    pygame.display.flip()