import pygame
WIDTH = 600
HEIGHT = 800
FPS = 144
#colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#hp bar
BAR_WIDTH = 250
BAR_HEIGHT = 20
BAR_X = 330
BAR_Y = 20

health = 100

back = pygame.image.load('image/galaxyback.png')

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reach For The Stars")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    screen.blit(back, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, RED, (BAR_X, BAR_Y, health / 100 * BAR_WIDTH, BAR_HEIGHT))
    pygame.display.update()

pygame.quit()