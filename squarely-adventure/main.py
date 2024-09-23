import pygame, random, os
from pygame.constants import QUIT
from pygame.locals import Rect
from pygame.surface import Surface
from classes.character import Character


def main():
    pygame.init()
    pygame.font.init()

    font = pygame.font.Font("fonts/game_over.ttf", 75)

    pygame.display.set_caption("Squarely Journey Inc.")

    # MAIN WINDOW + CONSTANTS
    WIDTH = 800 #pygame.display.Info().current_w
    HEIGHT = 600 #pygame.display.Info().current_h

    HORIZONTAL_CENTER = WIDTH  // 2
    VERTICAL_CENTER = HEIGHT // 2

    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

    # CLOCK
    clock = pygame.time.Clock()

    # PLAYER
    PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150
    PLAYER_X, PLAYER_Y = 0, 0

    current_player_position = "DOWN"
    is_player_walking = False

    direction_state = "still" # ["still", "moving"]
    vertical_leg_position = "left" # [None, "left", "right"]


    player = Character(
        PLAYER_X, PLAYER_Y , PLAYER_WIDTH, PLAYER_HEIGHT,
        {
            "sprites": {
                "idle": {
                    "left": "/images/blu-guy/left.png",
                    "up": "/images/blu-guy/up.png",
                    "right": "/images/blu-guy/right.png",
                    "down": "/images/blu-guy/down.png"
                },
                "walk": {
                    "left": "/images/blu-guy/left-walk.png",
                    "up_left": "/images/blu-guy/up-walk-left.png",
                    "up_right": "/images/blu-guy/up-walk-right.png",
                    "right": "/images/blu-guy/right-walk.png",
                    "down_left": "/images/blu-guy/down-walk-left.png",
                    "down_right": "/images/blu-guy/down-walk-right.png",
                }
            }
        },
    )


    player = Rect(
        PLAYER_X, PLAYER_Y , PLAYER_WIDTH, PLAYER_HEIGHT
    )
    player.center = (HORIZONTAL_CENTER, VERTICAL_CENTER)

    last_player_walk_switch_time = pygame.time.get_ticks()
    player_walk_switch_interval = 250

    # np. do klasy: path: /images - i auto szukanie left, right itp
    player_left = pygame.transform.scale(
        pygame.image.load("images/blu-guy/left.png"),
        (player.width, player.height)
    )
    player_left_walk = pygame.transform.scale(
        pygame.image.load("images/blu-guy/left-walk.png"),
        (player.width, player.height)
    )

    player_up = pygame.transform.scale(
        pygame.image.load("images/blu-guy/up.png"),
        (player.width, player.height)
    )
    player_up_walk_left = pygame.transform.scale(
        pygame.image.load("images/blu-guy/up-walk-left.png"),
        (player.width, player.height)
    )
    player_up_walk_right = pygame.transform.scale(
        pygame.image.load("images/blu-guy/up-walk-right.png"),
        (player.width, player.height)
    )

    player_right = pygame.transform.scale(
        pygame.image.load("images/blu-guy/right.png"),
        (player.width, player.height)
    )
    player_right_walk = pygame.transform.scale(
        pygame.image.load("images/blu-guy/right-walk.png"),
        (player.width, player.height)
    )

    player_down = pygame.transform.scale(
        pygame.image.load("images/blu-guy/down.png"),
        (player.width, player.height)
    )
    player_down_walk_left = pygame.transform.scale(
        pygame.image.load("images/blu-guy/down-walk-left.png"),
        (player.width, player.height)
    )
    player_down_walk_right = pygame.transform.scale(
        pygame.image.load("images/blu-guy/down-walk-right.png"),
        (player.width, player.height)
    )


    # ENEMY
    enemy_positions = ["LEFT", "RIGHT"]
    current_enemy_position = None

    ENEMY_WIDTH, ENEMY_HEIGHT = 75, 75
    enemy = Rect(
        0, 0, ENEMY_WIDTH, ENEMY_HEIGHT
    )
    RANDOM_X = random.randint(0 + ENEMY_WIDTH, WIDTH - ENEMY_WIDTH)
    RANDOM_Y = random.randint(0+ ENEMY_HEIGHT, HEIGHT - ENEMY_HEIGHT)
    enemy.center = (RANDOM_X, RANDOM_Y)

    goth_image_left = pygame.transform.scale(
        pygame.image.load("images/girl-left.png"),
        (enemy.width, enemy.height)
    )
    goth_image_right = pygame.transform.flip(goth_image_left, 1, 0)

    last_switch_time = pygame.time.get_ticks()
    switch_interval = 1000


    score = 0

    running = True
    while running:
        window.fill("olivedrab3")
        #pygame.time.delay(2)
        clock.tick(60)

        # ZDARZENIA
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # LOGIKA
        keys = pygame.key.get_pressed()


        if keys[pygame.K_ESCAPE]:
            os.system('clear')
            exit()


        if keys[pygame.K_LEFT] or keys[pygame.K_DOWN] or \
        keys[pygame.K_RIGHT] or keys[pygame.K_UP]:
            is_player_walking = True
        else:
            is_player_walking = False


        SPEED = 7

        if keys[pygame.K_LEFT]:
            player.x -= SPEED
            current_player_position = "LEFT"
        if keys[pygame.K_RIGHT]:
           player.x += SPEED
           current_player_position = "RIGHT"
        if keys[pygame.K_UP]:
            player.y -= SPEED
            current_player_position = "UP"
        if keys[pygame.K_DOWN]:
            player.y += SPEED
            current_player_position = "DOWN"

        if player.x < 0 - player.width:
            player.x = window.get_width()
        if player.x > window.get_width() + player.width:
            player.x = 0 - player.width
        if player.y < 0 - player.height:
            player.y = window.get_height()
        if player.y > window.get_height() + player.height:
            player.y = 0 - player.width

        collide = pygame.Rect.colliderect(player, enemy)
        if collide:
            score += 1
            RANDOM_X = random.randint(0 + ENEMY_WIDTH, WIDTH - ENEMY_WIDTH)
            RANDOM_Y = random.randint(0+ ENEMY_HEIGHT, HEIGHT - ENEMY_HEIGHT)
            enemy.center = (RANDOM_X, RANDOM_Y)

        textsurface = font.render(f"Wynik: {score}", True, "black")
        window.blit(textsurface, (10, 10))


        # image = ...

        current_player_switch_time = pygame.time.get_ticks()

        if is_player_walking:
            if current_player_switch_time >= last_player_walk_switch_time + \
            player_walk_switch_interval:
                if current_player_position == "LEFT":
                    if direction_state == "still":
                        image = player_left
                        direction_state = "moving"
                    elif direction_state == "moving":
                        image = player_left_walk
                        direction_state = "still"
                elif current_player_position == "RIGHT":
                    if direction_state == "still":
                        image = player_right
                        direction_state = "moving"
                    elif direction_state == "moving":
                        image = player_right_walk
                        direction_state = "still"
                elif current_player_position == "UP":
                    if direction_state == "still":
                        image = player_up
                        direction_state = "moving"
                    elif direction_state == "moving":
                       if vertical_leg_position == "left":
                           image = player_up_walk_left
                           direction_state = "still"
                           vertical_leg_position = "right"
                       elif vertical_leg_position == "right":
                           image = player_up_walk_right
                           direction_state = "still"
                           vertical_leg_position = "left"
                elif current_player_position == "DOWN":
                    if direction_state == "still":
                        image = player_down
                        direction_state = "moving"
                    elif direction_state == "moving":
                       if vertical_leg_position == "left":
                           image = player_down_walk_left
                           direction_state = "still"
                           vertical_leg_position = "right"
                       elif vertical_leg_position == "right":
                           image = player_down_walk_right
                           direction_state = "still"
                           vertical_leg_position = "left"

                last_player_walk_switch_time = current_player_switch_time
        else:
            if current_player_position == "LEFT":
                image = player_left
            elif current_player_position == "UP":
                image = player_up
            elif current_player_position == "RIGHT":
                image = player_right
            elif current_player_position == "DOWN":
                image = player_down

        window.blit(image, player)


        current_time = pygame.time.get_ticks()

        if current_time >= last_switch_time + switch_interval:
            if current_enemy_position == "LEFT":
                current_enemy_position = "RIGHT"
            elif current_enemy_position == "RIGHT":
                current_enemy_position = "LEFT"
            else:
                current_enemy_position = "LEFT"

            last_switch_time = current_time

        if current_enemy_position == "LEFT":
            window.blit(goth_image_left, enemy)
        elif current_enemy_position == "RIGHT":
            window.blit(goth_image_right, enemy)
        else:  # if None
            window.blit(goth_image_left, enemy)

        pygame.display.update()

    pygame.font.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
