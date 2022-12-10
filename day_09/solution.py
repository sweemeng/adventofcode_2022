from itertools import product


def solution(path, display=True, display_size=6):
    # There's no foot print
    head_print = set()
    tail_print = set()
    head = (0, 0)
    tail = (0, 0)
    # This is for display
    max_x = 0
    max_y = 0
    head_print.add(head)
    tail_print.add(tail)
    display_grid(head, tail, size=6)
    with open(path) as f:
        for line in f:
            line = line.strip()
            direction, step = line.split(" ")
            step = int(step)

            for move in move_head(head, direction, step):
                head = move
                head_print.add(move)
                tail = move_tail(tail, head)
                tail_print.add(tail)
                if display:
                    display_grid(head, tail, size=6)
        print(len(tail_print))


def solution_two(path, start_at=(0,0)):
    head_print = set()
    tail_print = set()
    rope = [start_at] * 10
    head_print.add(rope[0])
    tail_print.add(rope[-1])
    with open(path) as f:
        for line in f:
            line = line.strip()
            direction, step = line.split(" ")
            step = int(step)
            head = rope[0]
            temp = []
            for move in move_head(head, direction, step):
                head = move
                temp.append(head)
                for body in rope[1:]:
                    tail = move_tail(body, head)
                    temp.append(tail)
                    head = tail
                rope = temp
                temp = []
                tail_print.add(rope[-1])
    print(len(tail_print))


def move_head(position, direction, step):
    remain = step
    deltas = {
        "D": (-1, 0),
        "U": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }
    x, y = position
    while remain:
        dx, dy = deltas[direction]
        remain -= 1
        x += dx
        y += dy
        yield x, y


def move_tail(position, head_position):
    x, y = position
    neighbor = {
        (x+1, y-1), (x+1, y), (x+1,y+1),
        (x, y-1), (x, y), (x, y+1),
        (x-1, y-1), (x-1, y), (x-1, y+1),
    }
    if head_position in neighbor:
        return position

    hx, hy = head_position
    dx = hx - x
    dy = hy - y
    if dx > 0:
        x  += 1
    if dx < 0:
        x -=1

    if dy > 0:
        y += 1
    if dy < 0:
        y -= 1
    return x, y


def display_grid(head, tail, size=6):
    print(head)
    print(tail)
    trail = ""
    for point in product(range(size, -1, -1), range(size +1)):
        x, y = point
        if y == 0:
            trail = trail +  "\n"
        s = "."
        if point == tail:
            s="t"
        if point == head:
            s="h"
        trail = trail + s
    print(trail)
    print("")



if __name__ == '__main__':
    solution("input_test")
    solution("input_actual", display=False)
    solution_two("input_test_big", start_at=(5,11))
    solution_two("input_test_big")
    solution_two("input_test")
    solution_two("input_actual")