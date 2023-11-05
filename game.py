import pygame
from random import randint
WIDTH = 1200
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
window = pygame.display.set_mode(SIZE)
bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
score = 0
pygame.font.init()
font2 = pygame.font.Font(None, 40)
clock = pygame.time.Clock()
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, coords, size, speed):
        self.image = pygame.transform.scale(pygame.image.load(filename), size)
        self.original = pygame.transform.scale(pygame.image.load(filename), size)
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
class Tube(GameSprite):
    def update1(self):
        self.rect.x -= self.speed
        if self.rect.x <= 0:
            self.rect.x = WIDTH + randint(0, 100)
            self.rect = pygame.Rect(self.rect.x,self.rect.y, self.rect.width, randint(50, HEIGHT/2-50))
            self.image = pygame.transform.scale(self.original, (self.rect.width,self.rect.height))
            global score
            score += 1
            self.speed = randint(3, 10)
    def update2(self):
        self.rect.x -= self.speed
        if self.rect.x <= 0:
            self.rect.x = WIDTH + randint(0, 100)
            self.rect = pygame.Rect(self.rect.x,randint(HEIGHT/2, HEIGHT-100), self.rect.width, self.rect.height)
            self.image = pygame.transform.scale(self.original, (self.rect.width,self.rect.height))
            global score
            score += 1
            self.speed = randint(3, 10)
bird = Bird('bird.png', (50, HEIGHT/2), (50, 50), 5)
tube1 = Tube('tube_up.png', (WIDTH, 100), (75, 200), 4)
tube2 = Tube('tube_down.png', (WIDTH, HEIGHT+100), (75, 600), 4)
game = True
finish = False
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if not finish:
        window.blit(bg, (0, 0))
        bird.reset()
        bird.update()
        tube1.update1()
        tube1.reset()
        tube2.update2()
        tube2.reset()
        if pygame.sprite.collide_rect(bird, tube1) or pygame.sprite.collide_rect(bird, tube2) or bird.rect.y < 0 or bird.rect.y > HEIGHT:
            finish = True
            pygame.font.init()
            font1 = pygame.font.Font(None, 60)
            text1 = font1.render('Ти програв!', True, (255, 0, 0))
            window.blit(text1, (WIDTH/2, HEIGHT/2))
        score_text = font2.render('Очки:' + str(score), True, (255, 255, 255))
        window.blit(score_text, (0, 0))
    pygame.display.update()
    clock.tick(60)