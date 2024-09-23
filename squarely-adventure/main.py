import pygame, random, os
from pygame.constants import QUIT
from pygame.locals import Rect
from pygame.surface import Surface
from classes.player import Player


def main():
    pygame.init()
    pygame.font.init()

    font = pygame.font.Font("fonts/game_over.ttf", 75)
    pygame.display.set_caption("Squarely Journey Inc.")
    pygame.mouse.set_cursor(pygame.cursors.diamond)


    # MAIN WINDOW
    WIDTH = 800 #pygame.display.Info().current_w
    HEIGHT = 600 #pygame.display.Info().current_h

    HORIZONTAL_CENTER = WIDTH  // 2
    VERTICAL_CENTER = HEIGHT // 2

    window = pygame.display.set_mode((WIDTH, HEIGHT)) #, pygame.FULLSCREEN)


    # CLOCK
    clock = pygame.time.Clock()


    # PLAYER
    PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150
    PLAYER_X, PLAYER_Y = 0, 0

    # player_state = {
    #     "is_player_walking": False,
    #     "position": "DOWN",
    #     "direction": "still", # ["still", "moving"]
    #     "vertical_leg_position": "left" # [None, "left", "right"]
    # }

    player_sprites = {
        "idle": {
            "left": "images/blu-guy/left.png",
            "up": "images/blu-guy/up.png",
            "right": "images/blu-guy/right.png",
            "down": "images/blu-guy/down.png"
        },
        "walk": {
            "left": "images/blu-guy/left-walk.png",
            "up_left": "images/blu-guy/up-walk-left.png",
            "up_right": "images/blu-guy/up-walk-right.png",
            "right": "images/blu-guy/right-walk.png",
            "down_left": "images/blu-guy/down-walk-left.png",
            "down_right": "images/blu-guy/down-walk-right.png",
        }
    }


    PLAYER_SPEED = 7

    player = Player(
        window,
        PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED,
        player_sprites
    )

    player.center(HORIZONTAL_CENTER, VERTICAL_CENTER)

    last_player_walk_switch_time = pygame.time.get_ticks()
    player_walk_switch_interval = 250


    score = 0


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


    # MAIN LOOP
    running = True
    while running:
        window.fill("olivedrab3")
        clock.tick(60)

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


        player.is_walking = False

        # a może np. if keys..., then player.direction = "LEFT" (?)
        if keys[pygame.K_LEFT]:
            player.move("LEFT")
        if keys[pygame.K_RIGHT]:
           player.move("RIGHT")
        if keys[pygame.K_UP]:
            player.move("UP")
        if keys[pygame.K_DOWN]:
            player.move("DOWN")


        collide = pygame.Rect.colliderect(player.rect, enemy)
        if collide:
            score += 1
            RANDOM_X = random.randint(0 + ENEMY_WIDTH, WIDTH - ENEMY_WIDTH)
            RANDOM_Y = random.randint(0+ ENEMY_HEIGHT, HEIGHT - ENEMY_HEIGHT)
            enemy.center = (RANDOM_X, RANDOM_Y)


        # image_path = ...

        current_player_switch_time = pygame.time.get_ticks()

        if player.is_walking:
            if current_player_switch_time >= \
            last_player_walk_switch_time + player_walk_switch_interval:
                if player.position == "LEFT":
                    if player.direction == "still":
                        image_path = player.sprites["idle"]["left"]
                        player.direction = "moving"
                    elif player.direction == "moving":
                        image_path = player.sprites["walk"]["left"]
                        player.direction = "still"
                elif player.position == "RIGHT":
                    if player.direction == "still":
                        image_path = player.sprites["idle"]["right"]
                        player.direction = "moving"
                    elif player.direction == "moving":
                        image_path = player.sprites["walk"]["right"]
                        player.direction = "still"
                elif player.position == "UP":
                    if player.direction == "still":
                        image_path = player.sprites["idle"]["up"]
                        player.direction = "moving"
                    elif player.direction == "moving":
                       if player.vertical_leg_position == "left":
                           image_path = player.sprites["walk"]["up_left"]
                           player.direction = "still"
                           player.vertical_leg_position = "right"
                       elif player.vertical_leg_position == "right":
                           image_path = player.sprites["walk"]["up_right"]
                           player.direction = "still"
                           player.vertical_leg_position = "left"
                elif player.position == "DOWN":
                    if player.direction == "still":
                        image_path = player.sprites["idle"]["down"]
                        player.direction = "moving"
                    elif player.direction == "moving":
                       if player.vertical_leg_position == "left":
                           image_path = player.sprites["walk"]["down_left"]
                           player.direction = "still"
                           player.vertical_leg_position = "right"
                       elif player.vertical_leg_position == "right":
                           image_path = player.sprites["walk"]["down_right"]
                           player.direction = "still"
                           player.vertical_leg_position = "left"

                last_player_walk_switch_time = current_player_switch_time
        else:
            if player.position == "LEFT":
                image_path = player.sprites["idle"]["left"]
            elif player.position == "UP":
                image_path = player.sprites["idle"]["up"]
            elif player.position == "RIGHT":
                image_path = player.sprites["idle"]["right"]
            elif player.position == "DOWN":
                image_path = player.sprites["idle"]["down"]


        player.render(image_path)



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
