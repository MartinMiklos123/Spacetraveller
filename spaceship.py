import pygame as py
from bullets import Bullet


class Spaceship:

    BULLET_LIST = []

    def __init__(self, begin_cords, image_spaceship, surface, image_bullets):
        self.begin_cords = begin_cords
        self.image = image_spaceship
        self.screen = surface
        self.x = begin_cords[0]
        self.y = begin_cords[1]
        self.image_bullets = image_bullets
        self.bullet_cords_y = self.y
        self.bullet_list = []
        self.space_pressed = False

    def change_cords(self, key_input):
        if key_input[py.K_LEFT]:
            self.x -= 5
        elif key_input[py.K_RIGHT]:
            self.x += 5

    def draw_spaceship(self):
        self.screen.blit(self.image, (self.x, self.y))

    def shoot_bullets(self, key_input):

        if key_input[py.K_SPACE] and not self.space_pressed:
            bullet = Bullet(self.image_bullets, self.x, self.bullet_cords_y)
            self.BULLET_LIST.append(bullet.create_rect())
            self.space_pressed = True

        elif not key_input[py.K_SPACE]:
            self.space_pressed = False

    def adjust(self, speed):
        for i in Spaceship.BULLET_LIST:
            i.y -= speed
            self.screen.blit(self.image_bullets, (i.x, i.y))


    def check_for_turbo(self, key_input):
        if key_input[py.K_LSHIFT]:
            print("quack")
            return True









