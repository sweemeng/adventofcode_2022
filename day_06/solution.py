def marker_finder(line, length=4):
    buffer = []
    count = 0
    stop = False
    for c in line:
        count += 1
        if len(buffer) < length:
            buffer.append(c)
            continue

        buffer.pop(0)
        buffer.append(c)
        if len(set(buffer)) == length:
            stop = True

        if stop:
            break


    return buffer, count


def solution_test():
    test_input = {
        "bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
        "nppdvjthqldpwncqszvftbrmjlhg": 6,
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11
    }
    for key in test_input:
        buffer, test_val = marker_finder(key)
        val = test_input[key]
        if val != test_val:
            print(buffer)
            print("wrong marker", key, val, test_val)
            break


def solution_test_two():
    test_input = {
        "bvwbjplbgvbhsrlpgdmjqwftvncz": 23,
        "nppdvjthqldpwncqszvftbrmjlhg": 23,
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 29,
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 26
    }
    for key in test_input:
        buffer, test_val = marker_finder(key, length=14)
        val = test_input[key]
        if val != test_val:
            print(buffer)
            print("wrong marker", key, val, test_val)
            break


def solution(length=4):

    f = open("input_actual")
    value = f.read()
    buffer, test_val = marker_finder(value, length=length)
    print(test_val)


if __name__ == '__main__':
    solution_test()
    solution_test_two()
    solution()
    solution(14)
