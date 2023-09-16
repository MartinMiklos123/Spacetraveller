import pygame as py

class Bullet:
    def __init__(self, image, x_cords, y_cords):
        self.image = image
        self.x_cords = x_cords
        self.y_cords = y_cords


    def create_rect(self):
        bullet_rect = self.image.get_rect()
        bullet_rect.x = self.x_cords + 35
        bullet_rect.y = self.y_cords
        return bullet_rect




