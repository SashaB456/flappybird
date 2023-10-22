import pygame
WIDTH = 1200
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
window = pygame.display.set_mode(SIZE)
bg_col = (0, 255, 0)
window.fill(bg_col)
clock = pygame.time.Clock()
game = True 
finish = False
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()
    clock.tick(60)