import pygame
from pygame.constants import QUIT

def main():
    pygame.init()

    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hello World?")

    rect_width, rect_height = 30, 30
    rect_x = (window.get_width() - rect_width) // 2
    rect_y = (window.get_height() - rect_height) // 2

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            rect_x -= 1

            if rect_x < 0:
                rect_x = window.get_width()

        if keys[pygame.K_RIGHT]:
            rect_x += 1

            if rect_x > window.get_width():
                rect_x = 0

        if keys[pygame.K_UP]:
            rect_y -= 1

            if rect_y < 0:
                rect_y = window.get_height()

        if keys[pygame.K_DOWN]:
            rect_y += 1

            if rect_y > window.get_height():
                rect_y = 0

        window.fill("black")

        pygame.draw.rect(window, "white", (
            rect_x, rect_y, rect_width, rect_height
        ))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
