import pygame
from pygame.constants import QUIT
from pygame.locals import Rect
# from classes.character import Character
import random


def main():
    pygame.init()
    pygame.font.init()

    font = pygame.font.Font("fonts/game_over.ttf", 75)

    pygame.display.set_caption("Squarely Journey Inc.")

    # TEST STATE
    # player_posititions = ["LEFT", "UP", "RIGHT", "DOWN"]
    current_player_position = None

    # MAIN WINDOW + CONSTANTS
    WIDTH = pygame.display.Info().current_w
    HEIGHT = pygame.display.Info().current_h

    window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

    HORIZONTAL_CENTER = WIDTH  // 2
    VERTICAL_CENTER = HEIGHT // 2

    # CLOCK
    clock = pygame.time.Clock()

    # CHARACTER
    CHARACTER_WIDTH, CHARACTER_HEIGHT = 75, 75
    CHARACTER_X, CHARACTER_Y = 0, 0

    character = Rect(
        CHARACTER_X, CHARACTER_Y , CHARACTER_WIDTH, CHARACTER_HEIGHT
    )
    character.center = (HORIZONTAL_CENTER, VERTICAL_CENTER)

    skull_image_left = pygame.transform.scale(
        pygame.image.load("images/skull-left.png"),
        (character.width, character.height)
    )
    skull_image_right = pygame.transform.flip(skull_image_left, 1, 0)

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
        window.fill("pink")
        #pygame.time.delay(2)
        clock.tick(60)

        # ZDARZENIA
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # LOGIKA
        keys = pygame.key.get_pressed()

        SPEED = 7

        if keys[pygame.K_LEFT]:
            character.x -= SPEED
            current_player_position = "LEFT"
        if keys[pygame.K_RIGHT]:
           character.x += SPEED
           current_player_position = "RIGHT"
        if keys[pygame.K_UP]:
            character.y -= SPEED
            current_player_position = "UP"
        if keys[pygame.K_DOWN]:
            character.y += SPEED
            current_player_position = "DOWN"

        if character.x < 0 - character.width:
            character.x = window.get_width()
        if character.x > window.get_width() + character.width:
            character.x = 0
        if character.y < 0 - character.height:
            character.y = window.get_height()
        if character.y > window.get_height() + character.height:
            character.y = 0

        collide = pygame.Rect.colliderect(character, enemy)
        if collide:
            score += 1
            RANDOM_X = random.randint(0 + ENEMY_WIDTH, WIDTH - ENEMY_WIDTH)
            RANDOM_Y = random.randint(0+ ENEMY_HEIGHT, HEIGHT - ENEMY_HEIGHT)
            enemy.center = (RANDOM_X, RANDOM_Y)

        textsurface = font.render(f"Wynik: {score}", True, "black")
        window.blit(textsurface, (10, 10))

        if current_player_position == "LEFT":
            window.blit(skull_image_left, character)
        elif current_player_position == "RIGHT":
            window.blit(skull_image_right, character)
        else:  # if None
            window.blit(skull_image_left, character)


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
