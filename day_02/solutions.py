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

def solution():
    f = open("input_actual")
    total = 0
    for line in f:
        line = line.strip()
        a,b = line.split(" ")
        score = SCENARIO[(PIECE[b], PIECE[a])] + PIECE[b]
        total += score
    print(total)


if __name__ == "__main__":
    solution()