import pygame as pg
pg.init()
#background image
sti=pg.image.load("./asset/bg/back.png")
#screen Surface init
screen=pg.display.set_mode(sti.get_rect().size)
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
      pg.mouse.set_visible(True)
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
  bg=pg.image.load("./asset/bg/stg1bg.png")
  bg=pg.transform.scale(bg,(bg.get_rect().w*2.5,bg.get_rect().h*1.5))
  screen=pg.display.set_mode(bg.get_rect().size)
  screen.blit(bg,(0,0))
  pg.mouse.set_visible(False)
  tr=0
  # assign rect to character 플레이어 사각형 생성
  pci0=pg.image.load("./asset/entity/char1.png")
  pci0=pg.transform.scale(pci0,(pci0.get_rect().size[0]/8,pci0.get_rect().size[1]/8))
  pci=pg.image.load("./asset/entity/char2.png")
  pci=pg.transform.scale(pci,(pci.get_rect().size[0]/8,pci.get_rect().size[1]/8))
  pcr0=pci0.get_rect()
  pcr=pci.get_rect()
  pcu=pcr0
  piu=pci0
  # obstacle
  obs0=pg.Rect(0,pg.mouse.get_pos()[1],bg.get_rect().w/4,bg.get_rect().h/16)
  obs0.right=0
while running:
  if pg.event.get(pg.QUIT):
    running=False
  clock.tick(1024)
  #이미지 전환
  if tr<4:
    tr+=1
  else:
    if pcu==pcr0:
      pcu=pcr
      piu=pci
      tr=0
    elif pcu==pcr:
      pcu=pcr0
      piu=pci0
      tr=0
  # add code for the first stage //1스테이지 코드 추가
  # background 배경 draw
  screen.blit(bg,(0,0))  
  # player_mouse pointer tracker
  pcu.centerx,pcu.centery=pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]
  hb=0
  if hb==1:
    pg.draw.rect(screen,(0,0,0),pcu)
  screen.blit(piu,(pcu.left,pcu.top))
  # spawn obstacle 장애물(방해물) 생성
  obs0.right+=30
  if obs0.left>=bg.get_rect().size[0]:
    obs0.right=0
    #obs0.centery=(pcu.centery+obs0.centery)/2
    obs0.centery=pcu.centery
  pg.draw.rect(screen,(0,0,0),obs0)
  obs0.right+=30
  pg.draw.rect(screen,(0,0,0),obs0)
  if obs0.colliderect(pcu):
    running=False
    rc=0
  # render screen
  pg.display.flip()
