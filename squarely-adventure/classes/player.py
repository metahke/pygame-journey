import pygame
from pygame.locals import Rect


class Player:
    def __init__(self, window, x, y, width, height, speed):
        self.window = window
        self.rect = Rect(x, y , width, height)
        self.speed = speed
        self.direction = "bottom"
        self.is_walking = False

    # player.update_x(), player.update_y()?
    # @staticmethod
    # def check_for_screen_passage(window, rectangle):
    #     def wrapper(*args, **kwargs):
    #         if rectangle.right < 0:
    #             rectangle.left = window.get_width()
    #         elif rectangle.left > window.get_width():
    #             rectangle.right = 0

    #         if rectangle.bottom < 0:
    #             rectangle.top = window.get_height()
    #         elif rectangle.top > window.get_height():
    #             rectangle.bottom = 0

    #     return wrapper

    def center(self, x, y):
        self.rect.center = (x, y)

    # @check_for_screen_passage
    def move(self, direction, new_x, new_y):
        self.direction = direction
        self.is_walking = True

        self.rect.move_ip(new_x, new_y)


    def render(self, player_image):
        self.window.blit(player_image, self.rect)
