import pygame
from math import sqrt

pygame.init()

FPS = 60
WIDTH = 1000
HEIGHT = 500

# Настройка цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 150, 100)

# Игрок
MAX_DISTANCE_TO_OBJECT = 30  # Макс. дист. до объекта
score = 0  # Сколько печенек было съедено

player_speed = 1  # Скорость игрока
heroImg = pygame.image.load('chief.png')  # Текстура игрока
player_x = WIDTH // 2
player_y = HEIGHT // 2

player_width = 32
player_height = 32

player_x_moving = 1  # В какую сторону смотрит по оси X

player_hand = None  # Рука игрока


def player_hand_x():  # Координата руки по X
    return player_x + player_width // 2


def player_hand_y():  # Координата руки по Y
    return player_y + player_height // 2 + 8


def player_move_up(speed):
    global player_y

    for obj in game_objects:
        if obj["type"] == "draggable":
            continue

        if not(obj["x"] <= player_x <= obj["x"] + obj["width"] or
               obj["x"] <= player_x + player_width <= obj["x"] + obj["width"] or
               obj["x"] <= player_x + player_width // 2 <= obj["x"] + obj["width"]
              ):
            continue

        if player_y + player_height - 5 > obj["height"] + obj["y"]:
            player_y -= speed




"""
cockie: {"name": "cockie", "type": "draggable", "x": 400, "y": 240,
                 "width": 8, "height": 5, "model": pygame.image.load("cockie.png")}


"""

# Игровые обекты
game_objects = [{"name": "cockie", "type": "draggable", "x": 400, "y": 240,
                 "width": 8, "height": 5, "model": pygame.image.load("cockie.png")},

                {"name": "fatman", "type": "usable", "x": 600, "y": 250,
                 "width": 39, "height": 30, "model": pygame.image.load("fatman.png")},

                {"name": "furnance", "type": "usable", "x": 500, "y": 300,
                 "width": 60, "height": 100, "model": pygame.image.load("furnance.png"),
                 "has_chocolate": False, "has_testo": False, "timer": -1},

                {"name": "chocolate", "type": "draggable", "x": 400, "y": 250,
                 "width": 8, "height": 5, "model": pygame.image.load("chocolate.png")},

                {"name": "testo", "type": "draggable", "x": 400, "y": 260,
                 "width": 11, "height": 7, "model": pygame.image.load("testo.png")}
                ]

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill(WHITE)


def delete_object(object, handed=False):
    global player_hand

    game_objects.remove(object)
    if handed:
        player_hand = None


def draw_screen():  # Отрисовка экрана
    screen.fill(WHITE)

    for obj in game_objects:
        if obj["type"] != "draggable":
            if obj["y"] + obj["height"] // 2 <= player_y + player_height:
                screen.blit(obj["model"], (obj["x"], obj["y"]))

    screen.blit(heroImg, (player_x, player_y))

    for obj in game_objects:
        if obj["type"] != "draggable":
            if obj["y"] + obj["height"] // 2 > player_y + player_height:
                screen.blit(obj["model"], (obj["x"], obj["y"]))
        else:
            screen.blit(obj["model"], (obj["x"], obj["y"]))

    pygame.display.update()


def player_see_on(obj):  # Смотрит ли игрок на объект
    obj_x_center = obj["x"] + obj["width"] // 2
    obj_y_center = obj["y"] + obj["height"] // 2

    ply_x_center = player_x + player_width // 2
    ply_y_center = player_y + player_height // 2

    if (player_x_moving > 0) == (ply_x_center < obj_x_center) and (
            (obj["y"] <= ply_y_center <= obj["y"] + obj["height"]) or
            (player_y <= obj_y_center <= player_y + player_height)) and (

            (abs(ply_x_center-obj["x"]) <= MAX_DISTANCE_TO_OBJECT) or
            (abs(ply_x_center-obj["x"]-obj["width"]) <= MAX_DISTANCE_TO_OBJECT)):
        return True

    return False


def interact_with_item(obj):  # Когда игрок нажал клавишу E...
    global player_hand
    global score

    if player_hand is None:
        if obj["type"] == "draggable":  # Если объект можно взять, то помещаем в руку
            player_hand = obj
            return

    if obj["type"] == "usable":
        if obj["name"] == "fatman":  # Кормим или говорим, что нужно печенье
            if player_hand is not None and player_hand["name"] == "cockie":
                score += 1
                delete_object(player_hand, True)
                print("Score = ", score)
            else:
                print("GIVE ME A COCKIE!!!")
            return

        if obj["name"] == "furnance":
            if not obj["timer"] and player_hand is None:
                game_objects.append(
                    {"name": "cockie", "type": "draggable", "x": game_object['x'] - 50,
                     "y": game_object["y"] + game_object["height"],
                     "width": 8, "height": 5, "model": pygame.image.load("cockie.png")})
                player_hand = game_objects[-1]

            if player_hand is not None:
                if player_hand["name"] == "chocolate" and not obj["has_chocolate"]:
                    delete_object(player_hand, True)
                    obj["has_chocolate"] = True
                elif player_hand["name"] == "testo" and not obj["has_testo"]:
                    delete_object(player_hand, True)
                    obj["has_testo"] = True

                if obj["has_chocolate"] and obj["has_testo"]:
                    obj["timer"] = 100


E_clicked = False

running = True
while running:  # Главный цикл

    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # Получаем все кнопки
    if keys[pygame.K_a]:  # Движение влево
        player_x -= player_speed
        player_x_moving = -1
    elif keys[pygame.K_d]:  # Движение вправо
        player_x += player_speed
        player_x_moving = 1

    if keys[pygame.K_w]:
        player_move_up(player_speed)
    elif keys[pygame.K_s]:
        player_y += player_speed

    if keys[pygame.K_g] and player_hand is not None:  # Выбросить предмет из рук
        player_hand["y"] = player_y + player_height - player_hand["height"]
        player_hand = None

    if not keys[pygame.K_e]:
        E_clicked = False

    for game_object in game_objects:
        if game_object["name"] == "furnance":
            if game_object["timer"] > 0:
                game_object["timer"] -= 1

        if keys[pygame.K_e] and player_see_on(game_object) and not E_clicked:
            interact_with_item(game_object)

    if keys[pygame.K_e]:
        E_clicked = True

    if player_hand is not None:  # Если рука игрока не пустая, двигаем предмет к координатам руки
        player_hand["x"] = player_hand_x() - player_hand["width"] // 2
        player_hand["y"] = player_hand_y() - player_hand["height"] // 2

    draw_screen()
    clock.tick(FPS)

pygame.quit()
