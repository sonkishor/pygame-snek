import pygame
import time
import random
from pygame import font
from pygame import display
from pygame.constants import K_1

from pygame.font import SysFont

#initialize the pygame module
pygame.init()

width, height = 600, 400

#define colors 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snek")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)

def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0,0])
    
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])
    
def run_game():    
    gameOver = False
    gameClose = False    
    
    x = width/2;
    y = height/2;
    
    x_speed = 0;
    y_speed = 0;
    
    snakePixels = []
    snakeLength = 1;
    
    foodX = round (random.randrange(0,width) / 10) * 10
    foodY = round (random.randrange(0,height) / 10) * 10
    
    while not gameOver:
        while gameClose:
            game_display.fill(black)
            gameOvermessage = message_font.render("GameOver", True, red)
            replayMessage = message_font.render("R to Replay, Q to Exit", True, orange)
            
            game_display.blit(gameOvermessage, [width/3, height/3])
            game_display.blit(replayMessage, [width/3, height/2])
            print_score(snakeLength-1)
            display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_r:
                        run_game()  
                    if event.key == pygame.QUIT:
                        gameOver = True
                        gameClose = False
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
            
        if x>= width or x < 0 or y >= height or y < 0:
            gameClose = True
        
        x += x_speed
        y += y_speed
        
        game_display.fill(black)
        
        pygame.draw.rect(game_display, orange, [foodX,foodY, snake_size, snake_size])
        
        snakePixels.append([x,y])
        
        if len(snakePixels) > snakeLength:
            del snakePixels[0]
        
        for pixel in snakePixels[:-1]:
            if pixel == [x,y]:
                gameClose = True
        
        draw_snake(snake_size, snakePixels)
        print_score(snakeLength-1)
        
        pygame.display.update()
        
        if x == foodX and y == foodY:
            foodX = round (random.randrange(0,width) / 10) * 10
            foodY = round (random.randrange(0,height) / 10) * 10
            snakeLength += 1
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()
    
run_game()

