import random, pygame


def get_random_character_position(character_width, character_height):
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h

    x = random.randint(0 + character_width, screen_width - character_width)
    y = random.randint(0 + character_height, screen_height - character_height)

    return (x, y)
