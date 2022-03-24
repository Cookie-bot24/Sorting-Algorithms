import pygame
from bubble import *


if __name__ == '__main__':
    pygame.init()
    # TODO fix issues with large ranges
    # Titles the game
    pygame.display.set_caption('Bubble Sort')
    clock = pygame.time.Clock()

    WIDTH = 1920
    HEIGHT = 1080

    gamedisplay = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

    i = list(range(100))
    sh(i)
    bubble = Bubble(i, gamedisplay, HEIGHT, WIDTH)

    FPS = 20
    running = True
    while running:
        clock.tick(FPS)
        # Checking events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                running = False
