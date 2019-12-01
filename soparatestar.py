import pygame
import numpy as np
pygame.init()

Screen = pygame.display.set_mode([800,600])
Clock = pygame.time.Clock()
BLACK = (0,   0,   0)
WHITE = (255,255,255)
BLACK = (0 , 0, 0)
BLUE = (217, 231, 249)
GOLD = (255, 255, 0)
PURPLE = (202, 90, 155)
GREEN = ( 23, 210, 155)
RIGHT = np.array([1, 0])
UP = np.array([0, -1])
LEFT = np.array([-1, 0])
DOWN = np.array([0, 1])
UPRIGHT = np.array([1,1])
UPLEFT = np.array([-1,1])
DOWNRIGHT = np.array([1,-1])
DOWNLEFT = np.array([-1,-1])


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racecar1.png").convert_alpha()
        self.rect = self.image.get_rect()


    keys = pygame.key.get_pressed() #I learnt to use methods which help because i don't have to use a condition in the if statetements each time
    def MoveRight(self, pixels):
        if self.rect.x < 720:
            self.rect.x += pixels

    def MoveLeft(self, pixels):
        if self.rect.x > 10:
            self.rect.x -= pixels

    def MoveUp(self, pixels):
        if self.rect.y > 20:
            self.rect.y -= pixels

    def MoveDown(self, pixels):
        if self.rect.y < 520:
            self.rect.y += pixels
    def RotateSprite(self):
        self.image = pygame.transform.rotate(self.image, 180)

class Ball(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()



ball = Ball()
PCar1 = Car()
PCar1.rect.x = 600
PCar1.rect.y = 300
PCar2 = Car()
PCar2.rect.x = 100
PCar2.rect.y = 300
PCar1.RotateSprite()
AllSpritesList = pygame.sprite.Group()
AllSpritesList.add(PCar1)
AllSpritesList.add(PCar2)
AllSpritesList.add(ball)


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        PCar1.MoveLeft(5)
    if keys[pygame.K_RIGHT]:
        PCar1.MoveRight(5)
    if keys[pygame.K_UP]:
        PCar1.MoveUp(5)
    if keys[pygame.K_DOWN]:
        PCar1.MoveDown(5)
    if keys[pygame.K_a]:
        PCar2.MoveLeft(5)
    if keys[pygame.K_d]:
        PCar2.MoveRight(5)
    if keys[pygame.K_w]:
        PCar2.MoveUp(5)
    if keys[pygame.K_s]:
        PCar2.MoveDown(5)


    Screen.fill(WHITE)
    AllSpritesList.draw(Screen)
    pygame.display.flip()
    Clock.tick(60)


pygame.quit()
