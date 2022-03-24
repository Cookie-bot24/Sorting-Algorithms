import pygame, time
from random import shuffle as sh


class Bubble:
    def __init__(self, items, display, h, w, rw, dfs, dfbo, dft, dfbe):
        self.display = display
        self.height = h
        self.width = w
        self.rect_width = rw
        self.dis_from_side = dfs
        self.dis_from_bottom = dfbo
        self.dis_from_top = dft
        self.dis_in_between = dfbe

        self.items = items
        self.sort()

    def sort(self):
        for i in reversed(range(len(self.items))):
            self.draw()
            time.sleep(round(10 / (len(self.items)), 5))
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

        self.display.fill((0, 0, 0))
        height_unit = (self.height - (self.dis_from_bottom + self.dis_from_top)) // (max(self.items) + 1)
        for item in self.items:
            pygame.draw.rect(self.display, (255, 255, 255), [self.dis_from_side + (self.rect_width + self.dis_in_between) * self.items.index(item), self.dis_from_top + (max(self.items) - item) * height_unit, self.rect_width, (item + 1) * height_unit])

        pygame.display.update()
