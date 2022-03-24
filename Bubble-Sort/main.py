import pygame
from bubble import *

SEMI_DARK_BLUE = (17, 24, 32)
BLUE = (37, 44, 52)
ORANGE = (243, 170, 78)

if __name__ == '__main__':
    pygame.init()
    # Titles the game
    pygame.display.set_caption('Bubble Sort')
    clock = pygame.time.Clock()

    WIDTH = 1920
    HEIGHT = 1080

    RECT_WIDTH = 50
    DIS_FROM_BOTTOM = 10
    DIS_FROM_TOP = 70
    DIS_FROM_SIDE = 20
    DIS_IN_BETWEEN = 1

    font = pygame.font.SysFont('Cambria', 50)
    quit_pos = (WIDTH / 2 - 100, HEIGHT / 12)
    quit_text = font.render('QUIT', True, ORANGE)

    display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

    num_items = (WIDTH - (DIS_FROM_SIDE * 2)) // (RECT_WIDTH + DIS_IN_BETWEEN)
    print(num_items)
    # (self.width - (DIS_FROM_SIDE * 2) - len(self.items) * DIS_IN_BETWEEN) // len(self.items)
    i = list(range(num_items))
    sh(i)
    bubble = Bubble(i, display, HEIGHT, WIDTH, RECT_WIDTH, DIS_FROM_SIDE, DIS_FROM_BOTTOM, DIS_FROM_TOP, DIS_IN_BETWEEN)

    FPS = 20
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        if quit_pos[0] <= mouse[0] <= quit_pos[0] + 140 and quit_pos[1] <= mouse[1] <= quit_pos[1] + 65:
            pygame.draw.rect(display, BLUE, [quit_pos[0], quit_pos[1], 140, 65])
        else:
            pygame.draw.rect(display, SEMI_DARK_BLUE, [quit_pos[0], quit_pos[1], 140, 65])
        
        clock.tick(FPS)
        # Checking events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if quit_pos[0] <= mouse[0] <= quit_pos[0] + 140 and quit_pos[1] <= mouse[1] <= quit_pos[1] + 65:
                    running = False

        display.blit(quit_text, (quit_pos[0] + 10, quit_pos[1]))
        pygame.display.update()
