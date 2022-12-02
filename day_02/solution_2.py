WIN = 6
DRAW = 3
LOSE = 0
ROCK = 1
PAPER = 2
SCISSOR = 3
PIECE = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSOR,
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSOR
}
SCENARIO = {
    (ROCK, ROCK): DRAW,
    (ROCK, PAPER): LOSE,
    (ROCK, SCISSOR): WIN,
    (PAPER, ROCK): WIN,
    (PAPER, PAPER): DRAW,
    (PAPER, SCISSOR): LOSE,
    (SCISSOR, ROCK): LOSE,
    (SCISSOR, PAPER): WIN,
    (SCISSOR, SCISSOR): DRAW,
}

ENDING = {
    'X': WIN,
    'Y': DRAW,
    'Z': LOSE,
}
MY_ENDING = {
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN,
}

def solution():
    f = open("input_actual")
    total = 0
    for line in f:
        line = line.strip()
        a, b = line.split(" ")
        piece_a = PIECE[a]
        ending = ENDING[b]
        for key in SCENARIO:

            value = SCENARIO[key]
            ta, tb = key
            if ta != piece_a:
                continue
            if value == ending:
                score = MY_ENDING[b] + tb
                total += score
                break
    print(total)


if __name__ == "__main__":
    solution()
