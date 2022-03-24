import pygame, time
from random import shuffle as sh


class Bubble:
    def __init__(self, items, display, height, width):
        self.display = display
        self.height = height
        self.width = width

        self.items = items
        self.sort()

    def sort(self):
        for i in reversed(range(len(self.items))):
            self.draw()
            time.sleep(0.1)
            self.one_pass(i)

    def one_pass(self, num_to_go):
        previous_index = 0
        for index in range(1, num_to_go + 1):
            if self.items[index] < self.items[previous_index]:
                item = self.items[index]
                self.items[index] = self.items[previous_index]
                self.items[previous_index] = item

            previous_index = index

    def draw(self):
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()

        DIS_FROM_BOTTOM = 10
        DIS_FROM_TOP = 70
        DIS_FROM_SIDE = 20

        self.display.fill((0, 0, 0))
        rect_width = (self.width - (DIS_FROM_SIDE * 2) - len(self.items) * 5) // len(self.items)
        height_unit = (self.height - (DIS_FROM_BOTTOM + DIS_FROM_TOP)) // (max(self.items) + 1)
        for item in self.items:
            pygame.draw.rect(self.display, (255, 255, 255), [50 + (rect_width + 5) * self.items.index(item), DIS_FROM_TOP + (max(self.items) - item) * height_unit, rect_width, (item + 1) * height_unit])

        pygame.display.update()
