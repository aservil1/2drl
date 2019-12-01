import pygame
pygame.init()

#test 
Screen = pygame.display.set_mode([800,600])
Clock = pygame.time.Clock()
BLACK = (0,   0,   0)
WHITE = (255,255,255)
BLACK = (0 , 0, 0)
BLUE = (217, 231, 249)
GOLD = (255, 255, 0)
PURPLE = (202, 90, 155)
GREEN = ( 23, 210, 155)

class Car(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    keys = pygame.key.get_pressed() #I learnt to use methods which help because i don't have to use a condition in the if statetements each time
    def MoveRight(self, pixels):
        if self.rect.x < 780:
            self.rect.x += pixels

    def MoveLeft(self, pixels):
        if self.rect.x > 10:
            self.rect.x -= pixels

    def MoveUp(self, pixels):
        if self.rect.y > 10:
            self.rect.y -= pixels

    def MoveDown(self, pixels):
        if self.rect.y < 580:
            self.rect.y += pixels

PCar1 = Car(GOLD, 50,50)
PCar1.rect.x = 200
PCar1.rect.y = 300
AllSpritesList = pygame.sprite.Group()
AllSpritesList.add(PCar1)


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

    Screen.fill(WHITE)
    AllSpritesList.draw(Screen)
    pygame.display.flip()
    Clock.tick(60)

pygame.quit()