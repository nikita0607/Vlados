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
heroImg = pygame.image.load('chief.png')
player_x = WIDTH // 2
player_y = HEIGHT // 2

player_width = 32
player_height = 32

player_x_moving = 0
player_y_moving = 0

last_player_moving = 2
player_hand = None

# Игровые обекты
game_objects = [{"name": "unfire", "type": "draggable", "x": "-20", "y": "-40"}]

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill(WHITE)


def draw_screen():
    screen.fill(WHITE)
    
    screen.blit(heroImg, (player_x, player_y))
    for game_object in game_objects:
        pygame.draw.rect(screen, ORANGE, (game_objects["x"], game_objects["y"]), (30, 30))

    pygame.display.update()


def player_see_on(obj):
    if (player_x + player_width // 2 > obj["x"] != player_x + player_width // 2 + player_x_moving > obj["x"]) and (
        player_y + player_height // 2 > obj["y"] != player_y + player_height // 2 + player_y_moving > obj["y"]
    ):
        return True

    return False


running = True
while running:
    moving_x = True
    moving_y = True 

    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.a]:
        player_x -= player_speed
        player_x_moving = 10
    elif keys[pygame.d]:
        player_x += player_speed
        player_x_moving = -10
    else:
        player_x_moving = 0
        moving_x = False

    if keys[pygame.w]:
        player_y -= player_speed
        player_y_moving = -10
    elif keys[pygame.s]:
        player_y += player_spee
        player_y_moving = 10
    else:
        player_y_moving = 0
        moving_y = False

    if moving_y and not moving_x:
        player_x_moving = 0
    elif moving_x and not moving_y:
        player_y_moving = 0 

    if keys[pygame.E] and player_hand is None:

        for game_object in game_objects:
            if player_see_on(game_objects):
                print("See on me!")
    
    screen.fill(WHITE)
    draw_screen()
    clock.tick(FPS)

pygame.quit()







































