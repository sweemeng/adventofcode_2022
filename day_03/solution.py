import string


def solution():
    with open("input_test") as f:
        total = 0
        for line in f:
            line = line.strip()
            length = len(line)
            half = int(length/2)
            first = set(line[:half])
            last = set(line[half:])
            similar = list(first.intersection(last))
            print(similar[0])
            total += string.ascii_letters.index(similar[0]) + 1
        print(total)



if __name__ == "__main__":
    solution()
            