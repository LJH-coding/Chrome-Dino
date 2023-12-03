import pygame
import os
import random

pygame.init()

HEIGHT = 600
WIDTH = 1100

window = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

#載入資料
floor_surface = pygame.image.load("./assets/img/Track.png")
floor_x = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill(WHITE)

    if(floor_x <= -WIDTH):
        floor_x = 0
    window.blit(floor_surface, (floor_x, 550))
    window.blit(floor_surface, (floor_x + WIDTH, 550))
    floor_x -= 7

    #更新畫面
    pygame.display.update()
    pygame.time.Clock().tick(60)
