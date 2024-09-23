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
