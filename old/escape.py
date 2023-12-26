import pygame as pg
pg.init()

screen_width = 1300
screen_height = 790

screen = pg.display.set_mode((screen_width, screen_height))

pg.display.set_caption("school escape")

background = pg.image.load("./asset/bg/back.png")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.blit(background, (0, 0))
    pg.display.update()

pg.quit()
