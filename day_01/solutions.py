def solution(input_file):
    f = open(input_file)
    calories = []
    for line in f:
        if not calories:
            calorie = 0
        line = line.strip()
        if line:
            calorie += int(line)
        else:
            calories.append(calorie)
            calorie = 0
    return sorted(calories, reverse=True)

if __name__ == "__main__":
    results = solution("input_actual")
    print(results[0])
    print(sum(results[:3]))
