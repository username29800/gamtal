import pygame as pg
pg.init()
screen=pg.display.set_mode((1280,720))
clock=pg.time.Clock()
running=True
dt=0
while running:
  for event in pg.event.get():
    if event.type==pg.QUIT:
      running=False
  r1=pg.Rect((0,10),(100,100))
#  pg.image.load("gamtal.jpeg")
  pg.draw.rect(screen,"white",r1)
  pg.display.flip()
