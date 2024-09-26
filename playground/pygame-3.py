import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


class SpriteSheet:
    def __init__(self, image, colorkey):
        self.sheet = image
        self.colorkey = colorkey

    def get_image(self, width, height):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (0, 0, width, height))
        image = pygame.transform.scale(image, (75, 75))
        image.set_colorkey(self.colorkey)

        return image


spritesheet_image = pygame.image.load("sprites.png").convert_alpha()
sprite_colorkey =  (48, 104, 80)
spritesheet = SpriteSheet(spritesheet_image, sprite_colorkey)

frame_0 = spritesheet.get_image(16, 16)
frame_0 = spritesheet.get_image(16, 16)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("purple")
    screen.blit(frame_0, (0, 0))


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
