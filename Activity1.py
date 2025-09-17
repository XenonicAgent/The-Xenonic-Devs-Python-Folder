import pygame
pygame.init()
screen = pygame.display.set_mode((4000, 2000))
clock = pygame.time.clock()
square_pos = pygame.Rect(2950, 1920, 50, 50)
while True:
    if pygame.event.get(pygame.QUIT):break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
    square_pos.y -= 20
    screen.fill("black")
    pygame

