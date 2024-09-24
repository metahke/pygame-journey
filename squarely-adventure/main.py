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
    WIDTH = 800
    HEIGHT = 600

    HORIZONTAL_CENTER = WIDTH  // 2
    VERTICAL_CENTER = HEIGHT // 2

    window = pygame.display.set_mode((WIDTH, HEIGHT)) #, pygame.FULLSCREEN)


    # CLOCK
    clock = pygame.time.Clock()


    # SCORE
    score = 0


    # PLAYER
    PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150
    PLAYER_X, PLAYER_Y = 0, 0
    PLAYER_SPEED = 7

    # player_state = {
    #     "is_walking": False,
    #     "position": "idle", # ["idle", "walk"],
    #     "direction":  "down",
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

    player = Player(
        window,
        PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED,
        player_sprites
    )

    player.center(HORIZONTAL_CENTER, VERTICAL_CENTER)

    last_player_walk_switch_time = pygame.time.get_ticks()
    player_walk_switch_interval = 250


    # ENEMY
    enemy_positions = ["left", "right"]
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

        # - a może np. if keys..., then player.direction = "left" (?)
        # - można też rozwinąć o kierunki, np. left-up, right-down
        # - może warto definiować player.is_walking w głównej pętli, poniżej
        # - nie zmiana z walk/idle/walk/idle, tylko raczej walk/1 walk/2 walk/1
        # - zamiast player.is_walking, tp player.position "idle" lub "walk" ?
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
           player.move("right")
        if keys[pygame.K_UP]:
            player.move("up")
        if keys[pygame.K_DOWN]:
            player.move("down")


        # COLLISION DETECTION
        collide = pygame.Rect.colliderect(player.rect, enemy)
        if collide:
            score += 1
            RANDOM_X = random.randint(0 + ENEMY_WIDTH, WIDTH - ENEMY_WIDTH)
            RANDOM_Y = random.randint(0+ ENEMY_HEIGHT, HEIGHT - ENEMY_HEIGHT)
            enemy.center = (RANDOM_X, RANDOM_Y)


        # PLAYER LOGIC
        if player.position == "walk":
            if player.direction == "up" or player.direction == "down":
                if player.vertical_leg_position == "left":
                    player.direction = f"{player.direction}_left"
                    player.vertical_leg_position = "right"
                elif player.vertical_leg_position == "right":
                    player.direction = f"{player.direction}_right"
                    player.vertical_leg_position = "left"

        # here error, np. 'idle down_left'
        try:
            player.render(player.sprites[player.position][player.direction])
        except:
            print(player.position, player.direction)

        current_player_switch_time = pygame.time.get_ticks()

        if player.is_walking:
            if current_player_switch_time >= \
                last_player_walk_switch_time + player_walk_switch_interval:
                    if player.position == "idle":
                        player.position = "walk"
                    elif player.position == "walk":
                        player.position = "idle"

                    last_player_walk_switch_time = current_player_switch_time


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


        pygame.display.update()

    pygame.font.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
