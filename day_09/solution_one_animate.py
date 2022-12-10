import copy
from itertools import product

import pygame

BLACK = (0,0,0)
WHITE = (255, 255, 255)
WINDOW_SIZE = [1024, 1024]

class Rope:
    def __init__(self, path, size=2, start=(0,0)):
        self.path = path
        self.rope = [start] * size
        self.neighbor = lambda x, y: {
            (x+1, y-1), (x+1, y), (x+1,y+1),
            (x, y-1), (x, y), (x, y+1),
            (x-1, y-1), (x-1, y), (x-1, y+1),
        }
        self.deltas = {
            "D": (-1, 0),
            "U": (1, 0),
            "L": (0, -1),
            "R": (0, 1),
        }

    def travel(self):
        rope = copy.deepcopy(self.rope)
        with open(self.path) as f:
            for line in f:
                line = line.strip()
                direction, step = line.split(" ")
                step = int(step)

                for _ in range(step):
                    rope = self.move_rope(direction, rope)
                    yield rope

    def move_rope(self, direction, rope):
        temp = []
        head = rope[0]
        head = self.move_head(head, direction)
        temp.append(head)
        for body in rope[1:]:
            tail = self.move_tail(body, head)
            head = tail
            temp.append(head)
        rope = temp
        return rope



    def move_head(self, position, direction):
        dx, dy = self.deltas[direction]
        x,y = position
        return x + dx, y + dy


    def move_tail(self, tail, head):
        x, y = tail
        neighbor = self.neighbor(x, y)
        if head in neighbor:
            return x, y
        hx, hy = head
        dx = hx - x
        dy = hy - y
        if dx > 0:
            x += 1
        if dx < 0:
            x -= 1

        if dy > 0:
            y += 1
        if dy < 0:
            y -= 1
        return x, y


def flip(points):
    return [(100 - x, 100-y) for x,y in points]


def main():
    # Assume square
    size = 200
    height = 3
    width = 3
    margin = 0
    window_size = [(width+margin) * size, (height+margin) * size]
    pygame.init()
    screen = pygame.display.set_mode(window_size)
    done = False
    ropes = Rope("input_actual",size=9, start=(0,0))
    knot = ropes.travel()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(WHITE)
        occupied = next(knot)
        occupied = flip(occupied)
        for points in product(range(size), range(size)):
            row, col = points

            color = BLACK
            if points in occupied:
                color = WHITE
            pygame.draw.rect(
                screen,
                color,
                [
                    (margin+width) * col + margin,
                    (margin+height) * row + margin,
                    width,
                    height
                ]
            )
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()