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
hero = pygame.Rect(player_x, player_y, 60, 50)
heroImg = pygame.image.load('chief.png')
player_x = WIDTH // 2
player_y = HEIGHT // 2

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill(WHITE)


def draw_screen():


    pygame.display.update()

running = True
while running:
    moving = 0

    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                moving = -1
            if i.key == pygame.K_RIGHT:
                moving = 1
            if i.key == pygame.K_UP:
                moving = -2
            if i.key == pygame.K_DOWN:
                moving = 2

    player_x += moving%2 * player_speed
    player_y += moving//2 * player_speed
    
    screen.blit(heroImg, (hero.left, hero.top))
    screen.fill(WHITE)
    draw_screen()
    clock.tick(FPS)
pygame.quit()







































