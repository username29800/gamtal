import pygame as pg
pg.init()
sti=pg.image.load("back.png")
screen=pg.display.set_mode((sti.get_rect().size))
clock=pg.time.Clock()
running=True
while running:
  for event in pg.event.get():
    if event.type==pg.QUIT:
      running=False
  clock.tick(1024)
  screen.blit(sti,(0,0))
  r1=pg.Rect(50,50,100,100)
  r2=pg.Rect(10,10,100,70)
  r1.move_ip(pg.mouse.get_pos()[0]-r1.left-r1.width/2,pg.mouse.get_pos()[1]-r1.top-r1.height/2)
  pg.draw.rect(screen,"white",r1)
  pg.display.flip()