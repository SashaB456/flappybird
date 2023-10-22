import pygame
WIDTH = 1200
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
window = pygame.display.set_mode(SIZE)
bg_col = (0, 255, 0)
window.fill(bg_col)
clock = pygame.time.Clock()
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, coords, size, speed):
        self.image = pygame.Surface(size=size, masks=(255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Bird(GameSprite):
    def update(self):
        self.rect.y += self.speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.rect.y -= 10
bird = Bird(None, (50, HEIGHT/2), (50, 50), 5)
game = True
finish = False
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    window.fill(bg_col)
    bird.reset()
    bird.update()
    pygame.display.update()
    clock.tick(60)