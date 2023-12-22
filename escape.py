import pygame
pygame.init()

screen_width = 1300
screen_height = 790

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("school escape")

background = pygame.image.load("C:/python/game/back.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    pygame.display.update()

pygame.quit()
