import pygame
from random import randint
from random import choice

pygame.init()

hScreen = 600
wScreen = 600
clock = pygame.time.Clock()

RBoundary = wScreen - 30
LBoundary = -2
DBoundary = hScreen - 30
UBoundary = 50

global high

try:
    highscorefile = open("highscore.txt", "r+")
    high = highscorefile.read()
    highscorefile.close()
except:
    highscorefile = open("highscore.txt", "w+")
    highscorefile.write("0")
    highscorefile.close()
    highscorefile = open("highscore.txt", "r+")
    high = highscorefile.read()
    highscorefile.close()


run = True

screen = pygame.display.set_mode((wScreen,hScreen))

class snake:
    
    global snakeLength
    global snakeHead
    
    def __init__(self, vel, x, y, w ,h,):
        self.vel = vel
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.score = 0

    def draw(self):
        for XnY in snakeLength:
            pygame.draw.rect(screen, (20,155,10), (XnY[0], XnY[1], self.w, self.h))
        
    def move(self):   
        if self.left == True:
            self.x -= self.vel
        if self.right == True:
            self.x += self.vel
        if self.up == True:
            self.y -= self.vel
        if self.down == True:
            self.y += self.vel
        
    def eat(self):
        global foodx
        global foody
        global snakemax
        snake = pygame.Rect(snakeHead[0], snakeHead[1], self.w, self.h)
        food = pygame.Rect(foodx, foody, 15,15)
    #snakes head collides with the food
        if snake.colliderect(food):
            self.score += 5
            snakemax += 2
            foodx = randint(LBoundary + 10,RBoundary - 10) 
            foody = randint(UBoundary + 10,DBoundary - 10)
    #if food spawns in the snakes body
        for part in snakeLength[:-1]:
            bodyPart = pygame.Rect(part[0], part[1], self.w, self.h)
            if bodyPart.colliderect(food):
                foodx = randint(LBoundary + 10,RBoundary - 10) 
                foody = randint(UBoundary + 10,DBoundary - 10)
            

snakeLength = []
snakemax = 1
foodx = randint(LBoundary + 10,RBoundary - 10)
foody = randint(UBoundary + 10,DBoundary - 10)

player = snake(20, 300,300,20,20)

            
#main loop
while run:

    pygame.display.update()
    clock.tick(20)
    screen.fill((255,255,255))
    
#score background and window outline
    pygame.draw.rect(screen, (200,200,200), (0, 0 , 620, 45))
    pygame.draw.rect(screen, (0,0,0), (0, 0 , 620, 46), 2)
    pygame.draw.rect(screen, (0,0,0), (0, 46, 620, 553), 3)

#score text
    font2 = pygame.font.SysFont("comicsans", 30, True)
    highscoreText = font2.render("high score: " + high, 1, (0,0,0))
    scoreText = font2.render("score: " + str(player.score), 1, (0,0,0))
    screen.blit(highscoreText, (30, 13))
    screen.blit(scoreText, (470,10))

#Reset length and max length
    if player.score == 0:
        snakeLength = []
        snakemax = 1

    player.move()
    
#drawing snake and food
    if len(snakeLength) > snakemax:
        del snakeLength[0]
    snakeHead = []
    snakeHead.append(player.x)
    snakeHead.append(player.y)
    snakeLength.append(snakeHead)

    pygame.draw.rect(screen, (150,10,100), (foodx, foody, 15,15))
    player.draw()

#To exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if player.right != True:
            player.left = True
            player.down = False
            player.up = False
    if key[pygame.K_RIGHT]:
        if player.left != True:
            player.right = True
            player.down = False
            player.up = False
    if key[pygame.K_UP]:
        if player.down != True:
            player.up = True
            player.left = False
            player.right = False
    if key[pygame.K_DOWN]:
        if player.up != True:
            player.down = True
            player.left = False
            player.right = False         

    player.eat()
    
#Snake collides with the boundaries or itself
    for eachSegment in snakeLength[:-1]:
        head = pygame.Rect(snakeHead[0], snakeHead[1], player.w, player.h)
        body = pygame.Rect(eachSegment[0], eachSegment[1], player.w, player.h)
        if (head.colliderect(body)):
            font1 =  pygame.font.SysFont("comicsans", 100, True)
            gameOverText = font1.render("Game Over", 1, (0,0,0))
            screen.blit(gameOverText, (60,200))
            HScore = int(high)
            if player.score > HScore:
                HScore = player.score
                high = str(HScore)
                highscorefile = open("highscore.txt", "w+")
                highscorefile.write(high)
                highscorefile.close()
            player.left = False
            player.right = False
            player.up = False
            player.down = False
            player.score = 0
            player.vel = 20
            player.x = 300
            player.y = 300
            pygame.display.update()
            pygame.time.delay(1000)

    if (player.x > RBoundary or player.x < LBoundary or player.y < UBoundary or player.y > DBoundary):
            font1 =  pygame.font.SysFont("comicsans", 100, True)
            gameOverText = font1.render("Game Over", 1, (0,0,0))
            screen.blit(gameOverText, (60,200))
            HScore = int(high)
            if player.score > HScore:
                HScore = player.score
                high = str(HScore)
                highscorefile = open("highscore.txt", "w+")
                highscorefile.write(high)
                highscorefile.close()
            player.left = False
            player.right = False
            player.up = False
            player.down = False
            player.score = 0
            player.vel = 20
            player.x = 300
            player.y = 300
            pygame.display.update()
            pygame.time.delay(1000)

pygame.quit()
