from collections import defaultdict
from itertools import product


def generate_index(path):
    # list is important for order
    row_index = defaultdict(list)
    col_index = defaultdict(list)
    grid = {}
    with open(path) as f:
        row = 0
        for line in f:
            line = line.strip()
            length = len(line)
            for col in range(length):
                value = int(line[col])
                row_index[row].append((row, col, value))
                col_index[col].append((row, col, value))
                grid[(row, col)] = value
            row += 1
    # row only because we can assume square
    # grid exist for debugging purpose. 
    return row,row_index, col_index, grid


def viewable(items):
    maximum = -1
    for row, col, item in items:
        if item > maximum:
            maximum = item
            yield row, col


def viewable_two(items, current_height):
    for row, col, item in items:
        yield row, col
        if current_height <= item:
            break



def solution(path):
    row, row_index, col_index, grid = generate_index(path)
    viewed = set()
    # Now i am using this as list, bite me
    for values in row_index.values():
        for keys in viewable(values):
            viewed.add(keys)
        for keys in viewable(reversed(values)):
            viewed.add(keys)

    for values in col_index.values():
        for keys in viewable(values):
            viewed.add(keys)
        for keys in viewable(reversed(values)):
            viewed.add(keys)
    print(viewed)
    print(len(viewed))


def solution_two(path):
    rows, row_index, col_index, grid = generate_index(path)
    scores = defaultdict(lambda : 1)
    for points in product(range(rows), range(rows)):
        row, col = points

        row_segment_one, row_segment_two, col_segment_one, col_segment_two = segment_maker(row, col, row_index, col_index)

        left_score = len(list(viewable_two(reversed(row_segment_one), grid[points])))
        if left_score:
            scores[points] = scores[points] * left_score

        right_score = len(list(viewable_two(row_segment_two, grid[points])))
        if right_score:
            scores[points] = scores[points] * right_score

        top_score = len(list(viewable_two(reversed(col_segment_one), grid[points])))
        if top_score:
            scores[points] = scores[points] * top_score

        bottom_score = len(list(viewable_two(col_segment_two, grid[points])))
        if bottom_score:
            scores[points] = scores[points] * bottom_score

    maximum = 0
    max_key = None
    for key in scores:
        value = scores[key]
        if value > maximum:
            max_key = key
            maximum = value

    print(maximum)


def segment_maker(row, col, row_index, col_index):
    row_values = row_index[row]
    # rows segment 1
    row_segment_one = row_values[0:col]
    row_segment_two = row_values[col:]
    row_segment_two.pop(0)

    col_values = col_index[col]
    col_segment_one = col_values[0:row]
    col_segment_two = col_values[row:]
    col_segment_two.pop(0)
    return row_segment_one, row_segment_two, col_segment_one, col_segment_two

if __name__ == '__main__':
    solution("input_test")
    solution("input_actual")
    solution_two("input_test")
    solution_two("input_actual")