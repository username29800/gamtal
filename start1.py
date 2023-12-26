import pygame as pg
import random, time

pg.init()
pg.display.set_caption("야, 너두 탈출할수 있어")
#background image
sti = pg.image.load("./asset/bg/back.png")
#screen Surface init
screen = pg.display.set_mode(sti.get_rect().size)
#clock init
clock = pg.time.Clock()
running = True
#sprite rect
sto = pg.image.load("./asset/others/cursorstart.png")
stc = sto.get_rect()
#start button
stbtn = pg.Rect(65, 605, 980, 106)
#cursor
pg.mouse.set_cursor(pg.cursors.diamond)
#tick regulator init
tr = 0
rc = 0
while running:
  if pg.event.get(pg.QUIT):
    running = False
  clock.tick(1024)
  screen.blit(sti, (0, 0))
  # start the game
  if stbtn.collidepoint(pg.mouse.get_pos()):
    if pg.mouse.get_pressed()[0]:
      print("game start signal")
      rc = 1
      running = False
      pg.mouse.set_visible(True)
    else:
      stc.centerx, stc.centery = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
      pg.mouse.set_visible(False)
      screen.blit(sto, (stc.left, stc.top))
  else:
    pg.mouse.set_visible(True)
  pg.display.flip()
if rc == 1:
  running = True
  pg.display.set_caption("STAGE 1")
  bg = pg.image.load("./asset/bg/bg1.png")
  bg = pg.transform.scale(bg, (1180, 708))
  screen = pg.display.set_mode((1180, 708))
  screen.blit(bg, (0, 0))
  pg.mouse.set_visible(False)
  tr = 0
  # assign rect to character 플레이어 사각형 생성
  pci0 = pg.image.load("./asset/entity/char1.png")
  pci0 = pg.transform.scale(
      pci0, (pci0.get_rect().size[0] / 8, pci0.get_rect().size[1] / 8))
  pci = pg.image.load("./asset/entity/char2.png")
  pci = pg.transform.scale(
      pci, (pci.get_rect().size[0] / 8, pci.get_rect().size[1] / 8))
  pcr0 = pci0.get_rect()
  pcr = pci.get_rect()
  pcu = pcr0
  piu = pci0
  # obstacle
  ci1 = pg.image.load("./asset/entity/chalk1.png")
  ci2 = pg.image.load("./asset/entity/chalk2.png")
  ci3 = pg.image.load("./asset/entity/chalk3.png")
  ci1 = pg.transform.scale(ci1, (ci1.get_rect().w / 4, ci1.get_rect().h / 4))
  ci2 = pg.transform.scale(ci2, (ci1.get_rect().w, ci1.get_rect().h))
  ci3 = pg.transform.scale(ci3, (ci1.get_rect().w, ci1.get_rect().h))
  ci4 = pg.transform.rotate(ci1, 90)
  ci5 = pg.transform.rotate(ci2, 90)
  ci6 = pg.transform.rotate(ci3, 90)
  obs0 = pg.Rect(bg.get_rect().w / 2, 0, ci4.get_rect().w, ci4.get_rect().h)
  obs1 = pg.Rect(0, bg.get_rect().h / 2, ci1.get_rect().w, ci1.get_rect().h)
  obs0.bottom, obs1.right = 0, 0
  cil = [ci1, ci2, ci3, ci4, ci5, ci6]
  ci0 = ci1
  fast, fct, vl = 0, 0, 0
  # escape
  #1025,336
  #1050,360
  esc1 = pg.Rect(1025, 250, 75, 75)
  nesc1 = pg.Rect(0, 0, 950, 700)
  c1, c2, cesc, rc = 0, 0, 0, 0
  escc = 5
  x_or_y = random.randint(0, 7)
while running:
  if pg.event.get(pg.QUIT):
    running = False
  clock.tick(1024)
  #이미지 전환
  if tr < 4:
    tr += 1
  else:
    if pcu == pcr0:
      pcu = pcr
      piu = pci
      tr = 0
    elif pcu == pcr:
      pcu = pcr0
      piu = pci0
      tr = 0
  # add code for the first stage //1스테이지 코드 추가
  # background 배경 draw
  screen.blit(bg, (0, 0))
  # player_mouse pointer tracker
  pcu.centerx, pcu.centery = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
  hb = 0
  if hb == 1:
    pg.draw.rect(screen, (0, 0, 0), pcu)
  screen.blit(piu, (pcu.left, pcu.top))
  # spawn obstacle 장애물(방해물) 생성
  if x_or_y != 0:
    if cil.index(ci0) <= 2:
      ci0 = cil[random.randint(3, 5)]
    if abs(obs0.bottom - pcu.top) >= 2 and vl != 0:
      obs0.bottom += int(abs(obs0.bottom - pcu.top) / 2)
    else:
      obs0.bottom += 30
    if obs0.top >= bg.get_rect().size[1]:
      obs0.bottom = 0
      x_or_y = random.randint(0, 7)
      vl = random.randint(0, 2)
      if random.randint(0, 9) <= 3:
        obs0.centerx = pcu.centerx
      else:
        obs0.centerx = (pcu.centerx + obs0.centerx) / random.randint(2, 3)
    #pg.draw.rect(screen,(233,233,233),obs0)
    screen.blit(ci0, (obs0.left, obs0.top))
    if obs0.colliderect(pcu):
      running = False
      rc = 0
  else:
    # spawn obstacle 장애물(방해물) 생성
    if cil.index(ci0) >= 3:
      ci0 = cil[random.randint(0, 2)]
    if abs(obs1.right - pcu.left) >= 2 and vl != 0:
      obs1.right += int(abs(obs1.right - pcu.left) / 2)
    else:
      obs1.right += 40
    if obs1.left >= bg.get_rect().size[0]:
      obs1.right = 0
      x_or_y = random.randint(0, 7)
      vl = random.randint(0, 3)
      if random.randint(0, 9) <= 3:
        obs1.centery = pcu.centery
      else:
        obs1.centery = (pcu.centery + obs1.centery) / random.randint(2, 3)
    #pg.draw.rect(screen,(233,233,233),obs1)
    screen.blit(ci0, (obs1.left, obs1.top))
    if obs1.colliderect(pcu):
      running = False
      rc = 0
  # escape point 탈출구
  hb = 0
  if hb == 1:
    pg.draw.rect(screen, (0, 0, 0), esc1)
  if cesc == 0 and pcu.colliderect(esc1):
    c1 = time.time()
    cesc = 1
  if cesc == 1 and not pcu.colliderect(esc1):
    c2 = time.time()
    cesc = 0
  if pcu.colliderect(nesc1):
    escc = 5
  if c2 - c1 > 0.2:
    escc -= 1
    c2 = 0
  if escc <= 1 and pcu.colliderect(esc1):
    print("escaped!")
    running = False
    rc = 1
  # render screen
  pg.display.flip()
  print(c1, c2, cesc, escc, pg.mouse.get_pos())

# stage 2
if rc == 0:
  running = True
  rc = 0
  pg.display.set_caption("STAGE 2")
  bg = pg.image.load("./asset/bg/bg2.jpg")
  bg = pg.transform.rotate(bg, -90)
  bg = pg.transform.scale(bg, (1180, 708))
  #배경 회전한거 반영 안될 경우 한 번 써봐
  screen = pg.display.set_mode((1180, 708))
  screen.blit(bg, (0, 0))
  obs2 = pg.Rect(0, 0, int(1180 / 6), int(708 / 4))
  obs2.centerx = random.randint(int(obs2.w / 2), int(1180 - obs2.w / 2))
  obs2l = []
  obs2y = [obs2.h / 2, 708 - obs2.h / 2]
  obs2y2 = [0, 708 - obs2.h]
  obs2i = pg.transform.scale(pg.image.load("./asset/entity/ent1.png"),
                             (int(1180 / 6), int(708 / 4)))
  tr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  for i in range(0, 3):
    obs2l.append(obs2.copy())  #0번은 x고정, 1,2는 y고정(+x방향 움직임)
  obs2l[0].centery = 1180 / 2
  obs2l[0].right = 1180
  for i in obs2l[1:]:
    i.centerx = 1180 - i.w / 2
    i.centery = obs2y[obs2l.index(i) - 1]
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
  clock.tick(1024)
  screen.blit(bg, (0, 0))
  #이미지 전환
  if tr[0] < 4:
    tr[0] += 1
  else:
    if pcu == pcr0:
      pcu = pcr
      piu = pci
      tr[0] = 0
    elif pcu == pcr:
      pcu = pcr0
      piu = pci0
      tr[0] = 0
  pcu.centerx, pcu.centery = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
  hb = 0
  if hb == 1:
    pg.draw.rect(screen, (0, 0, 0), pcu)
  screen.blit(piu, (pcu.left, pcu.top))
  if tr[2] < 2:
    tr[2] += 1
  else:
    tr[2] = 0
    for i in obs2l[1:]:
      i.left -= 10
      if i.left <= 0:
        i.left = 1180
  for i in obs2l:
    screen.blit(pg.transform.scale(obs2i, (i.w, i.h)), (i.left, i.top))
#  for i in obs2y2:
#    screen.blit(obs2i, (1180 - obs2.w, i))
  if tr[1] < 8:
    tr[1] += 1
  else:
    tr[1] = 0
    obs2l[0].centery += (pg.mouse.get_pos()[1] - obs2l[0].centery) / 24
#  screen.blit(pg.transform.scale(obs2i, (obs2.w, obs2.h)),
#              (obs2l[0].left, obs2l[0].top))
#pg.display.update()
  # 충돌판정
  for i in obs2l:
    if pcu.colliderect(i):
      running = False
      rc = 0
  pg.display.flip()
'''# stage 3
if rc == 1:
  running = True
  rc = 0
  pg.display.set_caption("STAGE 3")
  bg = pg.image.load("./asset/bg/bg3.jpg")
  bg = pg.transform.scale(bg, (1180, 708))
  screen = pg.display.set_mode((1180, 708))
  screen.blit(bg, (0, 0))
  '''
