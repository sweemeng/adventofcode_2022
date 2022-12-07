import copy
import pprint
import re


def solution(path):
    with open(path) as f:
        shell = SantaShell()
        for line in f:
            shell.parse(line)
        # uncomment to debug
        # pprint.pprint(shell.tree)

    shell.go_walk()
    total_size = 0
    for key in shell.tree_size:
        value = shell.tree_size[key]
        if  value <= 100000:
            total_size += value
    # uncomment to debug
    # pprint.pprint(shell.tree_size)
    print(total_size)


def solution_two(path):
    with open(path) as f:
        shell = SantaShell()
        for line in f:
            shell.parse(line)
        # uncomment to debug
        #pprint.pprint(shell.tree)

    shell.go_walk()
    fs_size = 70000000
    remain = fs_size - shell.tree_size["/"]
    min_size = 30000000 - remain
    to_del = []
    for key in shell.tree_size:
        value = shell.tree_size[key]
        if value >= min_size:
            to_del.append(value)
    print(min(to_del))

class SantaShell:
    def __init__(self):
        self.location = []
        # I am cheating with python dictionary can take in anything
        self.tree = {}
        self.store_mode = False
        self.tree_size = {}

    def cd(self, path):
        self.store_mode = False
        if path == "..":
            self.location.pop(-1)
        else:
            self.location.append(path)

    def ls(self):
        # This is a noop
        self.store_mode = True
        key = self.location[-1]
        terminal = self.tree
        for key in self.location:
            if not key in terminal:
                terminal[key] = {}
            terminal = terminal[key]

    def store(self, col_one, col_two):
        terminal = self.tree
        for node in self.location:
            terminal = terminal[node]
        if col_one == "dir":
            terminal[col_two] = {}
        else:
            terminal[col_two] = int(col_one)

    def parse(self, line):
        group = re.findall(r"[0-9a-zA-B\/\.]+", line)
        if "$" in line:
            if len(group) == 2:
                self.cd(group[1])
            else:
                self.ls()
        else:
            self.store(group[0], group[1])

    def walk(self, tree, keys=[]):
        size = 0
        new_keys = copy.deepcopy(keys)
        for key in tree:
            if type(tree[key]) is dict:
                new_keys.append(key)
                dir_size = self.walk(tree[key], keys=new_keys)
                size += dir_size
                key_str = "/".join(new_keys)
                self.tree_size[key_str] = dir_size
            else:
                size += tree[key]

        return size

    def go_walk(self):
        result = self.walk(self.tree)


if __name__ == "__main__":
    solution("input_test")
    solution("input_actual")
    solution_two("input_test")
    solution_two("input_actual")
