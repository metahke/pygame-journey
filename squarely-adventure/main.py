import pygame, random, os, json
from pygame.constants import QUIT
from pygame.locals import Rect
from pygame.surface import Surface
from classes.player import Player
from classes.enemy import Enemy
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

    window = pygame.display.set_mode((WIDTH, HEIGHT)) #, pygame.FULLSCREEN)


    # CLOCK
    clock = pygame.time.Clock()


    # SCORE
    score = 0


    # PLAYER
    PLAYER_X, PLAYER_Y = 0, 0
    PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150
    PLAYER_SPEED = 7

    with open("data/player.json", "r", encoding="utf-8") as file:
        player_data = json.load(file)

    player = Player(
        window=window,
        x=PLAYER_X, y=PLAYER_Y,
        width=PLAYER_WIDTH, height=PLAYER_HEIGHT, speed = PLAYER_SPEED,
        state=player_data["state"], sprites=player_data["sprites"]
    )

    player.center(HORIZONTAL_CENTER, VERTICAL_CENTER)

    last_player_walk_switch_time = pygame.time.get_ticks()
    player_walk_switch_interval = 250


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


        """
        1. Jeśli player stoi, to jest "idle", a jeśli idzie, to jest "walk".
        2. Gdy player się zatrzymuje (żadna ze strzałek nie jest naciśnięta),
        to wtedy sprite zmienia się od razu na "idle".
        3. Jeśli strzałki są naciśnięte (poza góra i dół na raz i w boki), to
        wtedy liczony jest czas zmiany animacji
        """

        player.state["is_walking"] = 0

        # - a może np. if keys..., then player.direction = "left" (?)
        # - można też rozwinąć o kierunki, np. left-up, right-down
        # - może warto definiować player.is_walking w głównej pętli, poniżej
        # - nie zmiana z walk/idle/walk/idle, tylko raczej walk/1 walk/2 walk/1
        # - zamiast player.is_walking, to player.position "idle" lub "walk" ?
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
            enemy.center = get_random_character_position(ENEMY_WIDTH, ENEMY_HEIGHT)


        # PLAYER LOGIC
        # wartości zmiennych lokalne: position, direction
        # !! get_sprite(position, direction, vertical_leg_position)
        if player.state["position"] == "walk":
            if player.state["direction"] in ["up", "down"]:
                if player.state["vertical_leg_position"] == "left":
                    player.state["direction"] = f"{player.state["direction"]}_left"
                    player.state["vertical_leg_position"] = "right"
                elif player.state["vertical_leg_position"] == "right":
                    player.state["direction"] = f"{player.state["direction"]}_right"
                    player.state["vertical_leg_position"] = "left"

        # here error, np. 'idle down_left'
        try:
            player_image = player.sprites[player.state["position"]][player.state["direction"]]
            player.render(player_image)
        except:
            print(player.state["position"], player.state["direction"])

        current_player_switch_time = pygame.time.get_ticks()

        if player.state["is_walking"]:
            if current_player_switch_time >= \
                last_player_walk_switch_time + player_walk_switch_interval:
                    if player.state["position"] == "idle":
                        player.state["position"] = "walk"
                    elif player.state["position"] == "walk":
                        player.state["position"] = "idle"

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
