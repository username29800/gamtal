import pygame as pg
pg.init()
#background image
sti=pg.image.load("./asset/bg/back.png")
#screen Surface init
screen=pg.display.set_mode((sti.get_rect().size))
#clock init
clock=pg.time.Clock()
running=True
#sprite rect
# r1=pg.Rect(200,200,100,100)
# r2=pg.Rect(10,10,100,70)
#start button
stbtn=pg.Rect(65,605,980,106)
#cursor
pg.mouse.set_cursor(pg.cursors.diamond)
#tick regulator init
tr=0 
while running:
  for event in pg.event.get():
    if event.type==pg.QUIT:
      running=False
  clock.tick(1024)
  screen.blit(sti,(0,0))
  # collision detection
  '''
  if r1.colliderect(r2):
    running=False
  r1.centerx,r1.centery=pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]
  '''
  # tick regulator
  '''
  if tr<7:
    tr+=1
  else:
    r2.y+=1
    tr=0
  '''
  #pg.draw.rect(screen,(0,0,0,50),stbtn)
  #pg.draw.rect(screen,"blue",r2)
  #pg.draw.rect(screen,"white",r1)
  # start the game
  if stbtn.collidepoint(pg.mouse.get_pos()) and pg.event.get(pg.MOUSEBUTTONDOWN):
    print("game start signal")
  pg.display.flip()
