import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
OLIVE = (128, 128, 0)
git = True

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Smile')


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    screen.fill(GRAY)
    pygame.draw.circle(screen, YELLOW, (400, 300), 220)
    pygame.draw.ellipse(screen, BLACK, ((300, 180), (50, 100)))
    pygame.draw.ellipse(screen, BLACK, ((450, 180), (50, 100)))
    pygame.draw.arc(screen, BLACK, (275, 220, 250, 210), 3.3, -0.1, 15)
    pygame.draw.line(screen, BLACK, (50, 50), (400, 50), 10)
    pygame.display.flip()


