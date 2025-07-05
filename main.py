import pygame
from os.path import join

from random import randint

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

surface = pygame.Surface((100, 200))
surface.fill((255, 0, 0))
x = 100
y = 100

player_surface = pygame.image.load('images/player.png')
player_rect = player_surface.get_rect(center = (WINDOW_WIDTH/ 2, WINDOW_HEIGHT - 15))
player_direction = 1

star_surface = pygame.image.load('images/star.png')
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

meteor_surface = pygame.image.load('images/meteor.png')
meteor_rect = meteor_surface.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surface = pygame.image.load('images/laser.png')
laser_rect = laser_surface.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 45))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if pygame.key.get_pressed()[pygame.K_d]:
        x += 5
    if pygame.key.get_pressed()[pygame.K_a]:
        x -= 5
    if pygame.key.get_pressed()[pygame.K_w]:
        y -= 5
    if pygame.key.get_pressed()[pygame.K_s]:
        y += 5

    screen.fill('darkgray')
    for pos in star_positions:
        screen.blit(star_surface, (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
    
    screen.blit(meteor_surface, meteor_rect)
    screen.blit(laser_surface, laser_rect)
    
    player_rect.x += player_direction * 5
    screen.blit(player_surface, player_rect)
    
    pygame.display.update()
    

pygame.quit()