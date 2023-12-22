import pygame
import sys
import random

# Pygame 초기화
pygame.init()

# 화면 크기 및 색상 정의
screen_width = 1300
screen_height = 790
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("학교 탈출 게임")

# 배경 이미지 불러오기
background = pygame.image.load("./asset/bg/classroom.png")  # 배경 이미지 파일이름을 실제 파일 이름으로 바꾸세요

# 거북이 설정
turtle_width = 35   
turtle_height = 35
turtle_x = screen_width // 2 - turtle_width // 2
turtle_y = screen_height // 2 - turtle_height // 2
turtle_speed = 5

# 장애물 설정
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 20
obstacle_frequency = 25  # 장애물이 출현하는 주기

obstacles = []

# 점수
score = 0
font = pygame.font.Font(None, 36)

# 게임 루프
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 거북이 이동
    turtle_rect = pygame.Rect(turtle_x, turtle_y, turtle_width, turtle_height)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    turtle_x += (mouse_x - turtle_x) // 10
    turtle_y += (mouse_y - turtle_y) // 10

    # 장애물 생성
    if random.randint(1, obstacle_frequency) == 1:
        obstacle_x = random.randint(0, screen_width - obstacle_width)
        obstacle_y = -obstacle_height
        obstacles.append([obstacle_x, obstacle_y])

    # 장애물 이동
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

    # 장애물 충돌 체크
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height)
        if turtle_rect.colliderect(obstacle_rect):
            pygame.quit()
            sys.exit()

    # 화면 색 채우기
    screen.blit(background, (0, 0))

    # 거북이 그리기
    pygame.draw.rect(screen, (0, 128, 255), (turtle_x, turtle_y, turtle_width, turtle_height))

    # 장애물 그리기
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    # 점수 표시
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 설정
    clock.tick(100)

    # 점수 증가
    score += 1
