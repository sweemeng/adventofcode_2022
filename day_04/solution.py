import re


def get_sets(path):
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            values = re.findall(r"\d+",line)
            values = [int(i) for i in values]
            if values[0] == values[1]:
                set_1 = {values[0]}
            else:
                set_1 = set(range(values[0], values[1]+1))
            if values[2] == values[3]:
                set_2 = {values[2]}
            else:
                set_2 = set(range(values[2], values[3]+1))
            yield set_1, set_2

def solution():
    count = 0
    for set_1, set_2 in get_sets("input_actual"):
        if len(set_1) > len(set_2):
            if set_2.issubset(set_1):

                count += 1
        else:
            if set_1.issubset(set_2):
                count += 1
    print(count)


def solution_2():
    count = 0
    for set_1, set_2 in get_sets("input_actual"):
        if set_1.intersection(set_2):
            count += 1
    print(count)


if __name__ == "__main__":
    solution()
    solution_2()

