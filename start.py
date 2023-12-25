import pygame as pg
import random,time
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
    if pg.mouse.get_pressed()[0]:
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
  obs0=pg.Rect(bg.get_rect().w/2,0,bg.get_rect().w/48,bg.get_rect().h/6)
  obs0.bottom=0
  obs1=pg.Rect(0,bg.get_rect().h/2,bg.get_rect().w/8,bg.get_rect().h/32)
  obs1.right=0
  fast=0
  fct=0
  vl=0
  # escape
  #1025,336
  #1050,360
  esc1=pg.Rect(1025,250,75,75)
  nesc1=pg.Rect(0,0,950,700)
  c1=0
  c2=0
  escc=5
  cesc=0
  rc=0
  x_or_y=random.randint(0,7)
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
  if x_or_y!=0:
    if abs(obs0.bottom-pcu.top)>=2 and vl!=0:
      obs0.bottom+=int(abs(obs0.bottom-pcu.top)/2)
    else:
      obs0.bottom+=30
    if obs0.top>=bg.get_rect().size[1]:
      obs0.bottom=0
      x_or_y=random.randint(0,7)
      vl=random.randint(0,2)
      if random.randint(0,9)<=3:
        obs0.centerx=pcu.centerx
      else:
        obs0.centerx=(pcu.centerx+obs0.centerx)/random.randint(2,3)
    pg.draw.rect(screen,(233,233,233),obs0)
    if obs0.colliderect(pcu):
      running=False
      rc=0
  else:
  # spawn obstacle 장애물(방해물) 생성
    if abs(obs1.right-pcu.left)>=2 and vl!=0:
      obs1.right+=int(abs(obs1.right-pcu.left)/2)
    else:
      obs1.right+=40
    if obs1.left>=bg.get_rect().size[0]:
      obs1.right=0
      x_or_y=random.randint(0,7)
      vl=random.randint(0,3)
      if random.randint(0,9)<=3:
        obs1.centery=pcu.centery
      else:
        obs1.centery=(pcu.centery+obs1.centery)/random.randint(2,3)
    pg.draw.rect(screen,(233,233,233),obs1)
    if obs1.colliderect(pcu):
      running=False
      rc=0
  # escape point 탈출구
  hb=0
  if hb==1:
    pg.draw.rect(screen,(0,0,0),esc1)
  if cesc==0 and pcu.colliderect(esc1):
    c1=time.time()
    cesc=1
  if cesc==1 and not pcu.colliderect(esc1):
     c2=time.time()
     cesc=0
  if pcu.colliderect(nesc1):
    escc=5
  if c2-c1>0.2:
    escc-=1
    c2=0
  if escc<=1 and pcu.colliderect(esc1):
    print("escaped!")
    running=False
  # render screen
  pg.display.flip()
  print(c1,c2,cesc,escc,pg.mouse.get_pos())
