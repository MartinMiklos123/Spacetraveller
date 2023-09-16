import pygame as py
import time
from spaceship import Spaceship
from background_image import Background
from Asteroid import Asteroid

py.init()
WIDTH = 500
HEIGHT = 800
screen = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()
background_image = py.image.load("img.png")
background_image = py.transform.scale(background_image, (WIDTH, HEIGHT))

fire_image_1 = py.image.load("START_1.png")
fire_image_2 = py.image.load("START_2.png")
fire_image_3 = py.image.load("START_3.png")
fire_image_4 = py.image.load("START_4.png")
fire_image_5 = py.image.load("START_5.png")
fire_image_6 = py.image.load("START_6.png")
fire_image_7 = py.image.load("START_7.png")
e1 = py.image.load("E1.png")
e2 = py.image.load("E2.png")
e3 = py.image.load("E3.png")
e4 = py.image.load("E4.png")
e5 = py.image.load("E5.png")
e6 = py.image.load("E6.png")
e7 = py.image.load("E7.png")
e8 = py.image.load("E8.png")
e9 = py.image.load("E9.png")
e10 = py.image.load("E10.png")
e11 = py.image.load("E11.png")
e12 = py.image.load("E12.png")
e13 = py.image.load("E13.png")
e14 = py.image.load("E14.png")
e15 = py.image.load("E15.png")
e16 = py.image.load("E16.png")
e17 = py.image.load("E17.png")
f1 = py.image.load("f1.png")
f2 = py.image.load("f2.png")
f3 = py.image.load("f3.png")
f4 = py.image.load("f4.png")
f5 = py.image.load("f5.png")
f6 = py.image.load("f6.png")


spaceship_image = py.image.load("sp.png")
spaceship_image = py.transform.scale(spaceship_image, (100, 100))
bullet_image = py.image.load("BULLET_IMG.png")
bullet_image = py.transform.scale(bullet_image, (30, 30))
as_image = py.image.load("AST.png")
as_image = py.transform.scale(as_image, (30, 30))


cool_down_time = 0.15


lst_images = [fire_image_4, fire_image_5,  fire_image_7]
lst_images = [py.transform.rotate(i, 180) for i in lst_images]
lst_images = [py.transform.scale(i, (30, 30)) for i in lst_images]
lst_e = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14]
lst_e = [py.transform.scale(i, (30, 30)) for i in lst_e]
list_f = [f1, f2, f3, f4, f5, f6]
list_f = [py.transform.scale(i, (30, 50)) for i in list_f]
list_f = [py.transform.rotate(i, 180) for i in list_f]



game_on = True

BG = Background(screen=screen, image=background_image, screen_height=HEIGHT)
SP = Spaceship(surface=screen, image_spaceship=spaceship_image, begin_cords=(200, 550), image_bullets=bullet_image)
AS = Asteroid(image=as_image, surface=screen)

def main(running):
    begin_time = time.time()
    begin_time_2 = time.time()
    frame = 0
    bg_speed = 1
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        keys = py.key.get_pressed()

        BG.update(bg_speed)
        BG.render()

        spaceship_x = SP.x
        spaceship_y = SP.y

        if SP.check_for_turbo(keys):
            screen.blit(list_f[frame], (spaceship_x + 35.5, spaceship_y + 82))
            bg_speed = 5
            as_speed = 3
            bullet_speed = 10

        else:
            screen.blit(lst_images[frame], (spaceship_x + 35.5, spaceship_y + 82))
            bg_speed = 1
            as_speed = 1
            bullet_speed = 5


        SP.change_cords(keys)
        SP.draw_spaceship()
        SP.shoot_bullets(keys)
        SP.adjust(bullet_speed)
        AS.draw()
        AS.move(as_speed)
        AS.collision_check()

        if not AS.COLLISION:
            begin_time_2 = time.time()

        if AS.COLLISION:
            if begin_time_2 + 0.05 <= time.time():
                if AS.frame < len(lst_e) - 1:
                    AS.frame += 1
                else:
                    AS.frame = 0
                    AS.COLLISION = False
                begin_time_2 += 0.05
            screen.blit(lst_e[AS.frame], (AS.ANIMATION_X, AS.ANIMATION_Y))


        if begin_time + cool_down_time <= time.time():
            if frame < len(lst_images) - 1:
                frame += 1
            else:
                frame = 0
            begin_time += cool_down_time


        py.display.update()
        clock.tick(60)


main(game_on)
