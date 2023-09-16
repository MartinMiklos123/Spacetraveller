import pygame


class Background:
    def __init__(self, screen, image, screen_height):
        self.screen = screen
        self.image = image
        self.screen_height = screen_height
        self.screen_cord_x = 0
        self.screen_cord_y = 0


    def update(self, speed):
        self.screen_cord_y -= speed

        if self.screen_cord_y < -self.screen_height:
            self.screen_cord_y = 0

    def render(self):
        self.screen.blit(self.image, (self.screen_cord_x, self.screen_cord_y))
        self.screen.blit(self.image, (self.screen_cord_x, self.screen_cord_y + self.screen_height))