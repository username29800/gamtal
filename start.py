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
sto=pg.image.load("./asset/others/cursorstart.png")
stc=sto.get_rect()
#start button
stbtn=pg.Rect(65,605,980,106)
#cursor
pg.mouse.set_cursor(pg.cursors.diamond)
#tick regulator init
tr=0 
rc=0
while running:
  if pg.event.get(pg.QUIT):
    running=False
  clock.tick(1024)
  screen.blit(sti,(0,0))
  # start the game
  if stbtn.collidepoint(pg.mouse.get_pos()):
    if pg.event.get(pg.MOUSEBUTTONDOWN):
      print("game start signal")
      rc=1
      running=False
    else:
     stc.centerx,stc.centery=pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]
     pg.mouse.set_visible(False)
     screen.blit(sto,(stc.left,stc.top))
  else:
    pg.mouse.set_visible(True)
  pg.display.flip()
if rc==1:
  running=True
pg.display.set_caption("STAGE 1")
while running:
  if pg.event.get(pg.QUIT):
    running=False
  clock.tick(1024)
  # add code for the first stage //1스테이지 코드 추가
