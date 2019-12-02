import pygame
pygame.init()

#test
Screen = pygame.display.set_mode([800,600])
Clock = pygame.time.Clock()
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (217, 231, 249)
GOLD = (255, 255, 0)
PURPLE = (202, 90, 155)
GREEN = (23, 210, 155)

class Car(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

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

class Window:
    """this is where we set up all the code for the screen, but not the game logic"""
    def __init__(self):
        """set up the screen"""
        pygame.init()
        self.screen = pygame.display.set_mode([800,600])
        self.clock = pygame.time.Clock()
        self.done = False
        self.sprites = pygame.sprite.Group()  # all the sprites on the page

    def game_loop(self):
        while not self.done:
            self.screen.fill(WHITE) # clear the screen
            self.events()           # proses the events
            self.update()           # update all the game logic
            self.draw()             # draw on to the screen
            self.screen.flip()      # update the screen so the player can see
            self.clock.tick(60)     # cap the fps at 60
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.key_down(event.unicode)

    def key_down(self, key):
        pass

    def draw(self):
        pass

    def update(self):
        pass

    def quit(self):
        pygame.quit()

class Game(Window):
    """this is the class for all the game logic"""
    def __init__(self):
        self.player1 = Car(GOLD, 50, 50)
        self.sprites.add(self.player1)

    def draw(self):
        self.sprites.draw()

    def key_down(self, key):
        """this gets called when there is an event by the window class"""

        if key == "a":
            self.player1.MoveLeft(5)
        if key == "d":
            self.player1.MoveRight(5)
        if key == "w":
            self.player1.MoveUp(5)
        if key == "s":
            self.player1.MoveDown(5)


if __name__ == "__main__":  # this test if the code is running or if it imported, you can mostly ignore it
    Game().game_loop() # run the game