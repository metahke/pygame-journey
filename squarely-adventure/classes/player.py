import pygame
from pygame.locals import Rect


class Player:
    def __init__(self, window, x, y, width, height, speed):
        self.window = window
        self.rect = Rect(x, y , width, height)
        self.speed = speed

        self.state = {
            "direction": "down",
            "is_walking": 0
        }

    def center(self, x, y):
        self.rect.center = (x, y)

    # UPROŚCIĆ
    def move(self, direction):

        match direction:
            case "down-left":
                self.rect.x -= self.speed
                self.rect.y += self.speed

                if self.rect.x < 0 - self.rect.width:
                    self.rect.x = self.window.get_width()
                if self.rect.y > self.window.get_height():
                    self.rect.y = 0 - self.rect.width
            case "left":
                self.rect.x -= self.speed

                if self.rect.x < 0 - self.rect.width:
                    self.rect.x = self.window.get_width()
            case "up-left":
                self.rect.x -= self.speed
                self.rect.y -= self.speed

                if self.rect.x < 0 - self.rect.width:
                    self.rect.x = self.window.get_width()
                if self.rect.y < 0 - self.rect.height:
                    self.rect.y = self.window.get_height()
            case "up":
                self.rect.y -= self.speed

                if self.rect.y < 0 - self.rect.height:
                    self.rect.y = self.window.get_height()
            case "up-right":
                self.rect.x += self.speed
                self.rect.y -= self.speed

                if self.rect.x > self.window.get_width():
                    self.rect.x = 0 - self.rect.width
                if self.rect.y < 0 - self.rect.height:
                    self.rect.y = self.window.get_height()
            case "right":
                self.rect.x += self.speed

                if self.rect.x > self.window.get_width():
                    self.rect.x = 0 - self.rect.width
            case "down-right":
                self.rect.x += self.speed
                self.rect.y += self.speed

                if self.rect.x > self.window.get_width():
                    self.rect.x = 0 - self.rect.width
                if self.rect.y > self.window.get_height():
                    self.rect.y = 0 - self.rect.width
            case "down":
                self.rect.y += self.speed

                if self.rect.y > self.window.get_height():
                    self.rect.y = 0 - self.rect.width

        self.state["is_walking"] = 1
        self.state["direction"] = direction

    def render(self, image_path):
        image = pygame.transform.scale(
            pygame.image.load(image_path),
            (self.rect.width, self.rect.height)
        )

        self.window.blit(image, self.rect)
