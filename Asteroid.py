import pygame as py
import time
from spaceship import Spaceship
import random

begin_time = time.time()
cool_down_time = 0.15
frame = 0



class Asteroid:

    COLLISION = False
    ANIMATION_X = 0
    ANIMATION_Y = 0

    def __init__(self, image, surface):
        self.image = image
        self.x_cords = 0
        self.y_cords = 0
        self.screen = surface
        self.asteroid_lst = []
        self.frame = 0

    def create_rect(self):
        self.x_cords = random.randint(10, 400)
        asteroid_rect = self.image.get_rect()
        asteroid_rect.x = self.x_cords
        asteroid_rect.y = self.y_cords

        return asteroid_rect

    def move(self, speed):
        for i in self.asteroid_lst:
            i.y += speed
            self.screen.blit(self.image, (i.x, i.y))

    def draw(self):

        if len(self.asteroid_lst) < 3:
            asteroid_rect = self.create_rect()
            self.asteroid_lst.append(asteroid_rect)

        for i in self.asteroid_lst:
            if i.y > 800:
                self.asteroid_lst.remove(i)

    def collision_check(self):
        for asteroid in self.asteroid_lst:
            for bullet in Spaceship.BULLET_LIST:
                if asteroid.colliderect(bullet):
                    self.ANIMATION_X = asteroid.x
                    self.ANIMATION_Y = asteroid.y
                    self.COLLISION = True
                    self.asteroid_lst.remove(asteroid)
                    self.frame = 0







