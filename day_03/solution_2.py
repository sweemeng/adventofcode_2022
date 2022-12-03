import string


def solution():
    with open("input_actual") as f:
        lines = f.readlines()
        begin = 0
        end = 3
        group = lines[begin:end]
        total = 0
        while group:
            print(group)
            sack_1 = set(group[0].strip())
            sack_2 = set(group[1].strip())
            sack_3 = set(group[2].strip())
            subset = sack_1.intersection(sack_2)
            subset = subset.intersection(sack_3)
            begin += 3
            end += 3
            group = lines[begin:end]
            similar = list(subset)
            print(similar[0])
            total += string.ascii_letters.index(similar[0]) + 1
        print(total)



if __name__ == "__main__":
    solution()