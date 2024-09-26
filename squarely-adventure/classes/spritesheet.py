import pygame

class SpriteSheet:
    def __init__(self, image, colorkey):
        self.sheet = image
        self.colorkey = colorkey

    def get_image(self, width, height, x, y):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((x * 16), (y * 16), width, height))
        image = pygame.transform.scale(image, (75, 75))
        image.set_colorkey(self.colorkey)

        return image
