import pygame, random, os
from pygame.constants import QUIT
from pygame.locals import Rect
from pygame.surface import Surface
from classes.character import Character




    # PLAYER
    PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150
    PLAYER_X, PLAYER_Y = 0, 0

    player_state = {
        "is_player_walking": False,
        "position": "DOWN",
        "direction": "still", # ["still", "moving"]
        "vertical_leg_position": "left" # [None, "left", "right"]
    }

    player_sprites = {
        "sprites": {
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
    }

    player = Rect(
        PLAYER_X, PLAYER_Y , PLAYER_WIDTH, PLAYER_HEIGHT
    )
    player.center = (HORIZONTAL_CENTER, VERTICAL_CENTER)

    last_player_walk_switch_time = pygame.time.get_ticks()
    player_walk_switch_interval = 250

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_DOWN] or \
        keys[pygame.K_RIGHT] or keys[pygame.K_UP]:
            player_state["is_player_walking"] = True
        else:
            player_state["is_player_walking"] = False


        SPEED = 7

        if keys[pygame.K_LEFT]:
            player.x -= SPEED
            player_state["position"] = "LEFT"
        if keys[pygame.K_RIGHT]:
           player.x += SPEED
           player_state["position"] = "RIGHT"
        if keys[pygame.K_UP]:
            player.y -= SPEED
            player_state["position"] = "UP"
        if keys[pygame.K_DOWN]:
            player.y += SPEED
            player_state["position"] = "DOWN"

        if player.x < 0 - player.width:
            player.x = window.get_width()
        if player.x > window.get_width() + player.width:
            player.x = 0 - player.width
        if player.y < 0 - player.height:
            player.y = window.get_height()
        if player.y > window.get_height() + player.height:
            player.y = 0 - player.width


        # image_path = ...

        current_player_switch_time = pygame.time.get_ticks()

        if player_state["is_player_walking"]:
            if current_player_switch_time >= \
            last_player_walk_switch_time + player_walk_switch_interval:
                if player_state["position"] == "LEFT":
                    if player_state["direction"] == "still":
                        image_path = "images/blu-guy/left.png"
                        player_state["direction"] = "moving"
                    elif player_state["direction"] == "moving":
                        image_path = "images/blu-guy/left-walk.png"
                        player_state["direction"] = "still"
                elif player_state["position"] == "RIGHT":
                    if player_state["direction"] == "still":
                        image_path = "images/blu-guy/right.png"
                        player_state["direction"] = "moving"
                    elif player_state["direction"] == "moving":
                        image_path = "images/blu-guy/right-walk.png"
                        player_state["direction"] = "still"
                elif player_state["position"] == "UP":
                    if player_state["direction"] == "still":
                        image_path = "images/blu-guy/up.png"
                        player_state["direction"] = "moving"
                    elif player_state["direction"] == "moving":
                       if player_state["vertical_leg_position"] == "left":
                           image_path = "images/blu-guy/up-walk-left.png"
                           player_state["direction"] = "still"
                           player_state["vertical_leg_position"] = "right"
                       elif player_state["vertical_leg_position"] == "right":
                           image_path = "images/blu-guy/up-walk-right.png"
                           player_state["direction"] = "still"
                           player_state["vertical_leg_position"] = "left"
                elif player_state["position"] == "DOWN":
                    if player_state["direction"] == "still":
                        image_path = "images/blu-guy/down.png"
                        player_state["direction"] = "moving"
                    elif player_state["direction"] == "moving":
                       if player_state["vertical_leg_position"] == "left":
                           image_path = "images/blu-guy/down-walk-left.png"
                           player_state["direction"] = "still"
                           player_state["vertical_leg_position"] = "right"
                       elif player_state["vertical_leg_position"] == "right":
                           image_path = "images/blu-guy/down-walk-right.png"
                           player_state["direction"] = "still"
                           player_state["vertical_leg_position"] = "left"

                last_player_walk_switch_time = current_player_switch_time
        else:
            if player_state["position"] == "LEFT":
                image_path = "images/blu-guy/left.png"
            elif player_state["position"] == "UP":
                image_path = "images/blu-guy/up.png"
            elif player_state["position"] == "RIGHT":
                image_path = "images/blu-guy/right.png"
            elif player_state["position"] == "DOWN":
                image_path = "images/blu-guy/down.png"


        player_image = pygame.transform.scale(
            pygame.image.load(image_path),
            (player.width, player.height)
        )

        window.blit(player_image, player)
