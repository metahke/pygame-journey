import pygame, random, os, json
from pygame.constants import QUIT
from pygame.locals import Rect
from pygame.surface import Surface
from classes.player import Player
from classes.enemy import Enemy
from classes.spritesheet import SpriteSheet
from helpers.helpers import get_random_character_position

def main():
    pygame.init()
    pygame.font.init()

    font = pygame.font.Font("fonts/game_over.ttf", 75)
    pygame.display.set_caption("Squarely Adventure")
    pygame.mouse.set_visible(False)


    # MAIN WINDOW
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    HORIZONTAL_CENTER = SCREEN_WIDTH  // 2
    VERTICAL_CENTER = SCREEN_HEIGHT // 2

    BACKGROUND_COLOR = "olivedrab3"
    FPS = 60

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #  , pygame.FULLSCREEN)


    # CLOCK
    clock = pygame.time.Clock()


    # SCORE
    score = 0


    # PLAYER
    PLAYER_X, PLAYER_Y = 0, 0
    PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150
    PLAYER_SPEED = 7
    PLAYER_BACKWARD_SPEED = -1 * PLAYER_SPEED

    directions = [
        "bottom", "bottom-left", "left", "top-left",
        "top", "top-right", "right", "bottom-right"
    ]

    directions_speeds = {
        "bottom": (0, PLAYER_SPEED),
        "bottom-left": (PLAYER_BACKWARD_SPEED, PLAYER_SPEED),
        "left": (PLAYER_BACKWARD_SPEED, 0),
        "top-left": (PLAYER_BACKWARD_SPEED, PLAYER_BACKWARD_SPEED),
        "top": (0, PLAYER_BACKWARD_SPEED),
        "top-right": (PLAYER_SPEED, PLAYER_BACKWARD_SPEED),
        "right": (PLAYER_SPEED, 0),
        "bottom-right": (PLAYER_SPEED, PLAYER_SPEED)
    }

    player_spritesheet_image = pygame.image.load("images/green-guy/sprites.png").convert_alpha()
    player_spritesheet_colorkey =  (48, 104, 80)
    player_spritesheet = SpriteSheet(player_spritesheet_image, player_spritesheet_colorkey)

    player = Player(
        window=window,
        x=PLAYER_X, y=PLAYER_Y,
        width=PLAYER_WIDTH, height=PLAYER_HEIGHT, speed=PLAYER_SPEED
    )

    player.center(HORIZONTAL_CENTER, VERTICAL_CENTER)

    last_player_walk_switch_time = pygame.time.get_ticks()
    player_walk_switch_interval = 300
    player_walk_position = 0


    # ENEMY
    current_enemy_position = "left"

    ENEMY_X, ENEMY_Y = 0, 0
    ENEMY_WIDTH, ENEMY_HEIGHT = 75, 75

    enemy = Enemy(
        window,
        ENEMY_X, ENEMY_Y, ENEMY_WIDTH, ENEMY_HEIGHT, PLAYER_SPEED,
        state={}, sprites={}
    )

    enemy = Rect(
        ENEMY_X, ENEMY_Y, ENEMY_WIDTH, ENEMY_HEIGHT
    )

    enemy.center = get_random_character_position(ENEMY_WIDTH, ENEMY_HEIGHT)

    goth_image_left = pygame.transform.scale(
        pygame.image.load("images/girl-left.png"),
        (enemy.width, enemy.height)
    )
    goth_image_right = pygame.transform.flip(goth_image_left, 1, 0)

    last_switch_time = pygame.time.get_ticks()
    switch_interval = 1000


    # MAIN LOOP
    running = True
    while running:
        window.fill(BACKGROUND_COLOR)
        clock.tick(FPS)

        textsurface = font.render(f"Wynik: {score}", True, "black")
        window.blit(textsurface, (10, 10))


        # ZDARZENIA
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # LOGIKA
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            os.system('clear')
            exit()


        # PLAYER LOGIC

        ## MANAGE ARROW KEYS
        new_direction = ""

        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            new_direction = "top-left"
        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            new_direction = "top-right"
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            new_direction = "bottom-left"
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            new_direction = "bottom-right"
        elif keys[pygame.K_LEFT]:
            new_direction = "left"
        elif keys[pygame.K_RIGHT]:
           new_direction = "right"
        elif keys[pygame.K_UP]:
            new_direction = "top"
        elif keys[pygame.K_DOWN]:
            new_direction = "bottom"

        ## MANAGE ANIMATIONS MOVEMENT
        current_player_switch_time = pygame.time.get_ticks()

        if player.is_walking:
            if current_player_switch_time >= \
            last_player_walk_switch_time + player_walk_switch_interval:
                player_walk_position += 1
                player_walk_position %= 4

                last_player_walk_switch_time = current_player_switch_time
        else:
            player_walk_position = 0

        player_direction_index = directions.index(player.direction)
        player_image = player_spritesheet.get_image(
            16, 16, player_walk_position, player_direction_index)

        ## MOVE PLAYER
        if new_direction != "":
            player_x_speed, player_y_speed  = directions_speeds[new_direction]
            player.move(new_direction, player_x_speed, player_y_speed)
        else:
            player.is_walking = False

        ## DISPLAY PLAYER
        player.render(player_image)


        # ENEMY LOGIC
        current_time = pygame.time.get_ticks()

        if current_time >= last_switch_time + switch_interval:
            if current_enemy_position == "left":
                current_enemy_position = "right"
            elif current_enemy_position == "right":
                current_enemy_position = "left"
            else:
                current_enemy_position = "left"

            last_switch_time = current_time

        if current_enemy_position == "left":
            window.blit(goth_image_left, enemy)
        elif current_enemy_position == "right":
            window.blit(goth_image_right, enemy)
        else:  # if None
            window.blit(goth_image_left, enemy)


        # COLLISION DETECTION
        collide = pygame.Rect.colliderect(player.rect, enemy)
        if collide:
            score += 1
            enemy.center = get_random_character_position(ENEMY_WIDTH, ENEMY_HEIGHT)

        pygame.display.update()

    pygame.font.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
