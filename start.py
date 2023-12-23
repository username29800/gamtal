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
  screen=pg.display.set_mode(bg.get_rect().size)
  screen.blit(bg,(0,0))
  #tick regulator 실행 속도 조절기
  #tr=외부 변수 입력 (위 코드에서 tr)
  #m=tr값 한계치(tr변수 리셋 기준점)
  def treg(tr,m):
    if tr<=m:
      tr+=1
    else:
      tr=0
    return tr
  #init
  tr=0
  # assign rect to character 플레이어 사각형 생성
  pci0=pg.image.load("./asset/entity/char1.png")
  pci=pg.image.load("./asset/entity/char2.png")
  pcr0=pci0.get.rect()
  pcr=pci.get.rect()
while running:
  if pg.event.get(pg.QUIT):
    running=False
  clock.tick(1024)
  #이미지 전환
  prt=clock.get_fps()/2
  # add code for the first stage //1스테이지 코드 추가
  # player_mouse pointer tracker
  
