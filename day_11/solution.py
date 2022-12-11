import operator
import re
from math import floor, gcd


class Monkey:
    def __init__(self):
        self.items = []
        self.operations = None
        self.conditions = None
        self.target = {1: None, 0:None}
        self.inspect_count = 0

    def operate(self, item):
        if not self.operations:
            raise Exception("Not Ready")
        a, op, b = self.operations
        if a == "old":
            x = item
        else:
            x = int(a)
        if b == "old":
            y = item
        else:
            y = int(b)
        return op(x, y)

    def send(self, item):
        if item % self.conditions:
            return self.target[1]
        return self.target[0]

    def fetch(self, item):
        self.items.append(item)

    def inspect(self):
        self.inspect_count += 1
        item = self.items.pop(0)
        return item

    def can_play(self):
        if self.items:
            return True
        return False


def parse_maths(line):
    tokens = line.split(" ")
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    return tokens[2], ops[tokens[3]], tokens[4]


def load_monkeys(path):
    current_monkey = None
    monkeys = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if "Monkey" in line:
                _, sid = line.split(" ")
                monkey = Monkey()
                current_monkey = int(sid[:-1])
                monkeys[current_monkey] = monkey
                continue
            if "Starting items" in line:
                _, items_str = line.split(": ")
                items = [int(i) for i in items_str.split(", ")]
                monkeys[current_monkey].items = items
                continue
            if "Operation" in line:
                _, op_str = line.split(": ")
                ops = parse_maths(op_str)
                monkeys[current_monkey].operations = ops
                continue
            if "Test" in line:
                group = re.findall("\d+", line)
                monkeys[current_monkey].conditions = int(group[0])
                continue
            if "If true" in line:
                group = re.findall("\d+", line)
                # 0 because it is divisible
                monkeys[current_monkey].target[0] = int(group[0])
                continue
            if "If false" in line:
                group = re.findall("\d+", line)
                # 0 because it is divisible
                monkeys[current_monkey].target[1] = int(group[0])
                continue
    return monkeys


def solution(path):
    monkeys = load_monkeys(path)

    for _ in range(20):
        play(monkeys)
        for key in monkeys:
            print(monkeys[key].items)
            print(monkeys[key].inspect_count)
    top_monkey = []
    for key in monkeys:
        top_monkey.append(monkeys[key].inspect_count)
    top_monkey.sort(reverse=True)
    print(top_monkey[0], top_monkey[1], top_monkey[0] * top_monkey[1])


def solution_two(path):
    monkeys = load_monkeys(path)
    round_stats = {
        1: None,
        20: None,
    }
    start_count = 1000
    for rounds in range(10000):
        play_no_worry(monkeys)
        stats = {}
        if rounds+1 in round_stats:
            print(rounds + 1)
            for key in monkeys:
                stats[key] = monkeys[key].inspect_count
                print("Monkey ", key, ":", monkeys[key].inspect_count)
            round_stats[rounds+1] = stats
        if rounds + 1 == start_count:
            print(rounds + 1)
            for key in monkeys:
                stats[key] = monkeys[key].inspect_count
                print("Monkey ", key, ":", monkeys[key].inspect_count)
            round_stats[rounds+1] = stats
            start_count += 1000

    top_monkey = []
    for key in monkeys:
        top_monkey.append(monkeys[key].inspect_count)
    top_monkey.sort(reverse=True)
    print(top_monkey[0], top_monkey[1], top_monkey[0] * top_monkey[1])



def play(monkeys):
    num_monkeys = len(monkeys)
    for i in range(num_monkeys):
        monkey = monkeys[i]
        while monkey.can_play():

            item = monkey.inspect()

            value = monkey.operate(item)

            value = value / 3

            value = floor(value)

            next_monkey = monkey.send(value)

            monkeys[next_monkey].fetch(value)
    return monkeys


def play_no_worry(monkeys):
    num_monkeys = len(monkeys)
    prods = 1
    for i in range(num_monkeys):
        # I steal the code from. But essentially, however you add/mul the number.
        # When you mod it, you get the same value. So just make sure that the test number
        # cover the number you will be testing. prods will cap the number. 
        prods *= monkeys[i].conditions

    for i in range(num_monkeys):
        monkey = monkeys[i]
        while monkey.can_play():
            item = monkey.inspect()
            value = monkey.operate(item)
            value = value % prods
            next_monkey = monkey.send(value)
            monkeys[next_monkey].fetch(value)
    return monkeys




if __name__ == '__main__':
    solution("input_test")
    solution("input_actual")
    solution_two("input_test")
    solution_two("input_actual")