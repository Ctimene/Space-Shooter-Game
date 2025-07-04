import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    screen.fill(0, 0, 40)
    

pygame.quit()