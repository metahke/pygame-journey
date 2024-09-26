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
    pygame.display.set_caption("Squarely Journey Inc.")
    pygame.mouse.set_cursor(pygame.cursors.diamond)


    # MAIN WINDOW
    WIDTH = 800
    HEIGHT = 600

    HORIZONTAL_CENTER = WIDTH  // 2
    VERTICAL_CENTER = HEIGHT // 2

    window = pygame.display.set_mode((WIDTH, HEIGHT)) #  , pygame.FULLSCREEN)


    # CLOCK
    clock = pygame.time.Clock()


    # SCORE
    score = 0


    # PLAYER
    PLAYER_X, PLAYER_Y = 0, 0
    PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150
    PLAYER_SPEED = 7

    player_spritesheet_image = pygame.image.load("images/green-guy/sprites.png").convert_alpha()
    player_spritesheet_colorkey =  (48, 104, 80)
    player_spritesheet = SpriteSheet(player_spritesheet_image, player_spritesheet_colorkey)

    player = Player(
        window=window,
        x=PLAYER_X, y=PLAYER_Y,
        width=PLAYER_WIDTH, height=PLAYER_HEIGHT, speed = PLAYER_SPEED
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


        # COLLISION DETECTION
        collide = pygame.Rect.colliderect(player.rect, enemy)
        if collide:
            score += 1
            enemy.center = get_random_character_position(ENEMY_WIDTH, ENEMY_HEIGHT)


        # PLAYER LOGIC
        directions = ["down", "down-left", "left", "up-left", "up", "up-right",
            "right", "down-right"]

        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            player.move("up-left")
        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            player.move("up-right")
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            player.move("down-left")
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            player.move("down-right")
        elif keys[pygame.K_LEFT]:
            player.move("left")
        elif keys[pygame.K_RIGHT]:
           player.move("right")
        elif keys[pygame.K_UP]:
            player.move("up")
        elif keys[pygame.K_DOWN]:
            player.move("down")
        else:
            player.state["is_walking"] = 0

        current_player_switch_time = pygame.time.get_ticks()

        if player.state["is_walking"]:
            if current_player_switch_time >= \
            last_player_walk_switch_time + player_walk_switch_interval:
                player_walk_position += 1
                player_walk_position %= 4

                last_player_walk_switch_time = current_player_switch_time
        else:
            player_walk_position = 0


        player_direction_index = directions.index(player.state["direction"])
        print(player_walk_position, player_direction_index)
        player_image = player_spritesheet.get_image(
            16, 16, player_walk_position, player_direction_index)

        window.blit(player_image, player.rect)


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
