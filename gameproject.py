import pygame
pygame.init()
import math

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
        self.texture = pygame.Surface([15, 15])
        self.image = self.texture
        self.texture.fill(BLACK)
        self.texture.set_colorkey(WHITE)
        pygame.draw.rect(self.texture, color, [0, 0, width, height])
        self.rect = self.texture.get_rect()
        self.angle = 0

    def update(self):
        self.image = pygame.transform.rotate(self.texture, (self.angle/(2*math.pi))*360)

    def MoveRight(self, pixels):
        self.angle += 0.09

    def MoveLeft(self, pixels):
        self.angle -= 0.09

    def MoveUp(self, pixels):
        y = self.rect.y + (pixels * math.sin(self.angle))
        x = self.rect.x - (pixels * math.cos(self.angle))

        if x > 5 and x < 600:
            self.rect.x = x

        if y > 5 and y < 600:
            self.rect.y = y

    def MoveDown(self, pixels):

        y = self.rect.y + (pixels * math.sin(self.angle + math.pi))
        x = self.rect.x - (pixels * math.cos(self.angle + math.pi))
        if x > 5 and x < 600:
            self.rect.x = x
        if y > 5 and y < 600:
            self.rect.y = y

class Window:
    """this is where we set up all the code for the screen, but not the game logic"""
    def __init__(self):
        """set up the screen"""
        pygame.init()
        self.screen = pygame.display.set_mode([800, 600])
        self.clock = pygame.time.Clock()
        self.done = False
        self.sprites = pygame.sprite.Group()  # all the sprites on the page
        self.down = []

    def game_loop(self):
        while not self.done:
            self.screen.fill(WHITE) # clear the screen
            self.events()           # proses the events
            self.update()           # update all the game logic
            self.draw()             # draw on to the screen
            pygame.display.flip()   # update the screen so the player can see
            self.clock.tick(60)     # cap the fps at 60
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.key_down(chr(event.key))
                self.down.append(chr(event.key))
            elif event.type == pygame.KEYUP:
                self.down.remove(chr(event.key))

    def key_down(self, key):
        pass

    def key_up(self, key):
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
        Window.__init__(self)
        self.player1 = Car(GOLD, 50, 50)
        self.player1.rect.x = 100
        self.player1.rect.y = 100
        self.sprites.add(self.player1)

    def draw(self):
        self.sprites.draw(self.screen)

    def update(self):
        self.player1.update()
        if "a" in self.down:
            self.player1.MoveLeft(5)
        if "d" in self.down:
            self.player1.MoveRight(5)
        if "w" in self.down:
            self.player1.MoveUp(5)
        if "s" in self.down:
            self.player1.MoveDown(5)

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