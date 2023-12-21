import pygame as pg
pg.init()
screen=pg.display.set_mode((1280,720))
clock=pg.time.Clock()
running=True
a=0
dt=0
l1=["red","blue","green"]
while running:
  for event in pg.event.get():
    if event.type==pg.QUIT:
      running=False
  screen.fill(l1[a])
  pg.display.flip()
  if a>1:
    a=0
  else:
    a+=1
