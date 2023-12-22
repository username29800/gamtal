import pygame as pg
pg.init()
sti=pg.image.load("./asset/bg/back.png")
screen=pg.display.set_mode((sti.get_rect().size))
clock=pg.time.Clock()
running=True
r1=pg.Rect(50,50,100,100)
r2=pg.Rect(10,10,100,70)
pg.mouse.set_visible(False)
tr=0
while running:
  for event in pg.event.get():
    if event.type==pg.QUIT:
      running=False
  clock.tick(1024)
  screen.blit(sti,(0,0))
  r1.centerx,r1.centery=pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]
  if tr<7:
    tr+=1
  else:
    r2.y+=1
    tr=0
  pg.draw.rect(screen,"white",r1)
  pg.draw.rect(screen,"blue",r2)
  pg.display.flip()
