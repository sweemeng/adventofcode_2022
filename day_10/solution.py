def solution(path):
    f = open(path)
    ops = f.readlines()

    x = 1
    ptr = 0
    temp = 0
    cycle = 1
    cycle_check = 20
    check = {}
    score = {}
    while True:
        if ptr >= len(ops) and not temp:
            print(cycle)
            break
        op =ops[ptr]
        op = op.strip()
        if temp:
            x += temp
            temp = 0
            ptr += 1
        else:
            if op == "noop":
                ptr += 1
            else:
                _, temp_ = op.split(" ")
                temp = int(temp_)
        cycle += 1
        if cycle == cycle_check:
            check[cycle] = x
            score[cycle] = cycle * x
            cycle_check += 40


    if check:
        print(cycle)
        print(check)
        print(sum(score.values()))


def make_sprites(x):
    sprites = ["."] * 40
    if x-1 > -1:
        sprites[x - 1] = "#"
    if -1 < x < 40:
        sprites[x] = "#"
    if x+1 < 40:
        sprites[x + 1] = "#"
    return sprites


def solution_two(path):
    f = open(path)
    ops = f.readlines()

    x = 1
    ptr = 0
    temp = 0
    cycle = 0

    pixels = ""

    while True:
        if ptr >= len(ops) and not temp:
            break
        op = ops[ptr]
        op = op.strip()
        sprites = make_sprites(x)
        print("".join(sprites))
        print(cycle)
        print(sprites[cycle])
        pixels = pixels + sprites[cycle]
        if temp:
            x += temp
            temp = 0
            ptr += 1
        else:
            if op == "noop":
                ptr += 1
            else:
                _, temp_ = op.split(" ")
                temp = int(temp_)
        cycle += 1
        if cycle == 40:
            pixels = pixels + "\n"
            cycle = 0


    # Not RBPARAGP
    print(pixels)


if __name__ == '__main__':
    solution("input_test_small")
    solution("input_test_big")
    solution("input_actual")
    solution_two("input_test_big")
    print("")
    solution_two("input_actual")



