import pygame 
import random 

FPS = 60
WIDTH = 500
HEIGHT = 100

#Настройка цвета
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
ORANGE = (255, 150, 100)

# Персонаж
player_speed = 1


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill(WHITE)


def draw_screen():
    pygame.display.update()

running = True
while running:
    moving = ""

    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                moving = 'LEFT'
            if i.key == pygame.K_RIGHT:
                moving = 'RIGHT'
            if i.key == pygame.K_UP:
                moving = 'UP'
            if i.key == pygame.K_DOWN:
                moving = 'DOWN'
    
    draw_screen()
    clock.tick(FPS)
pygame.quit()







































