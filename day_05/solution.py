import re
from collections import defaultdict


def parse_data(path):
    stacks = defaultdict(list)
    instructions = []
    with open(path) as f:
        for line in f:
            line = line.strip("\n")
            if re.match(r"^move", line):
                pattern = re.match(r"move (?P<amount>\d+) from (?P<from>\d+) to (?P<to>\d+)", line)
                code = {
                    "from": int(pattern.group("from")),
                    "to": int(pattern.group("to")),
                    "amount": int(pattern.group("amount"))
                }
                instructions.append(code)
            elif not line:
                continue
            elif "[" in line:
                layers = parse_line(line)
                for item in range(len(layers)):
                    if layers[item]:
                        stacks[item+1].append(layers[item])
            else:
                continue

        return stacks, instructions


def parse_line(line):
    layer = []
    ptr = 0
    while True:
        if ptr > len(line):
            break
        if line[ptr] == " ":
            ptr += 4
            layer.append("")
            continue
        elif line[ptr] == "[":
            ptr += 1
            continue
        elif line[ptr] == "]":
            ptr += 2
        else:
            layer.append(line[ptr])
            ptr += 1
            continue

    return layer





def solution():
    stacks, instructions = parse_data("input_actual")
    for instruction in instructions:
        for i in range(instruction["amount"]):
            value = stacks[instruction["from"]].pop(0)

            stacks[instruction["to"]].insert(0, value)
    output = []
    for key in sorted(stacks.keys()):
        output.append(stacks[key][0])
    print("".join(output))


def solution2():
    stacks, instructions = parse_data("input_actual")
    for instruction in instructions:
        hold = []
        for i in range(instruction["amount"]):
            value = stacks[instruction["from"]].pop(0)
            hold.append(value)

        stacks[instruction["to"]] = hold + stacks[instruction["to"]]
    output = []
    for key in sorted(stacks.keys()):
        output.append(stacks[key][0])
    print("".join(output))


if __name__ == "__main__":
    solution2()
