# Author: Jackie Xu
# Date: 2/15/2017
# Content: My third game using pygame (Galactic Defender)
# Special: Attempting to build an AI opponent
#===========================================================
import pygame
import random
import math
import time

# Powerup ideas
# shield
# size change
# speed change
# life
# gravity change

# Other game mechanics
# Colour gates
# multiple paths
# Projectile enemies

#pygame.mixer.pre_init(44100, -16, 2, 2048)
#pygame.mixer.init()
pygame.init()

# colours: RGB
white = (255, 255, 255)
black = (0, 0, 0)
cyan = (20, 220, 220)
pink = (255, 0, 255)
red = (255, 0, 0)
purple = (100, 0, 100)
orange = (255, 153, 51)
green = (0, 155, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

WIDTH = 1000
HEIGHT  = 600
FPS = 30
GAP = 200
BAR_DISTANCE = 200
BAR_SPEED = 10

object_width = 10
object_height = 10
walk_speed = 10
g = 0.6
clock = pygame.time.Clock()

#S Surface (Display of the game)
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chopper')

class Object:

    def __init__(self, x = WIDTH / 2, y = HEIGHT / 2, vx = 0, vy = 0, ax = 0, ay = g, friction_x = 0, friction_y = 0, width = object_width, height = object_height):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.friction_x = friction_x
        self.friction_y = friction_y
        self.width = width
        self.height = height

    def move(self):
        self.vx = self.vx + self.ax - sign(self.vx) * self.friction_x
       # vx_new = self.vx - sign(self.vx) * self.friction_x
       # self.vx = self.vx - sign(self.vx) * self.friction_x
            
        
        self.vy = self.vy + self.ay
        
        self.x = self.x + self.vx
        self.y = self.y + self.vy


    def draw (self, surface = gameDisplay):
        pygame.draw.rect(gameDisplay, white, [self.x, self.y, self.width, self.height])


# Collision detector
def collide (x1, y1, l1, w1, x2, y2, l2, w2):
    if x1 < x2 + l2 and x1 + l1 > x2 and \
       y1 < y2 + w2 and y1 + w1 > y2:
        return True

    else:
        return False
   
def sign(x):
    if x > 0:
        return 1.
    elif x < 0:
        return -1.
    elif x == 0:
        return 0.
    else:
        return False
    
def gameloop():
    gameOver = False
    gameExit = False
    player = Object(friction_x = 0.25)
    bars = []

    while not gameExit:
        gameDisplay.fill(black)
        
        keys = pygame.key.get_pressed()

        randH = random.randrange(100, 301)

        player.move()
        if player.x <= 0:
            player.x = 0
            player.vx = 0

        if len(bars) == 0:
            bars.append(Object(x = WIDTH, y = 0, vx = -BAR_SPEED, ax = 0,ay = 0, width = 10, height = randH))
            bars.append(Object(x = WIDTH, y = randH + GAP, vx = -BAR_SPEED, ax = 0,ay = 0, width = 10, height = WIDTH - (randH + GAP)))
        
        elif len(bars) < 24:
            pos = bars[-1].x + BAR_DISTANCE
            bars.append(Object(x = pos, y = 0, vx = -BAR_SPEED, ax = 0,ay = 0, width = 10, height = randH))
            bars.append(Object(x = pos, y = randH + GAP, vx = -BAR_SPEED, ax = 0,ay = 0, width = 10, height = WIDTH - (randH + GAP)))


        if bars[0].x + bars[0].width < -20:
            del bars [0]

        for bar in bars:
            bar.move()
            if collide(player.x, player.y, player.width, player.height, bar.x, bar.y, bar.width, bar.height):
                print("Crash!")
            bar.draw()

                
        
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                gameExit = True
                
        if keys [pygame.K_LEFT] and player.x + player.vx > 0:
            player.vx = player.vx - abs(walk_speed) / 5

        elif keys [pygame.K_RIGHT] and player.x + player.width + player.vx < WIDTH:
            player.vx = player.vx + abs(walk_speed) / 5
      #  else:
      #      player.vx = 0
            

        if keys [pygame.K_UP] and player.y + player.vy > 0:
            player.vy = player.vy - abs(walk_speed) / 5
                        
        elif keys [pygame.K_DOWN] and player.y + player.height + player.vy < HEIGHT:
            player.vy = player.vy + abs(walk_speed) / 5
            
      #  else:
      #      player.vy = 0

        
      #  print(player.vy)
        player.draw(gameDisplay)

        pygame.display.update()
        clock.tick(FPS)
        
    pygame.quit()
    
gameloop()
