with open("day_1/resources/input_2.txt") as fptr:
    input_ = list(line.strip() for line in fptr.readlines())


from collections import defaultdict

cumulative = 0
calorie_packs = defaultdict(int)
for line in input_:
    if len(line) < 1:
        calorie_packs[cumulative] += 1
        cumulative = 0
        continue

    cumulative += int(line)

calorie_sum = 0
for _ in range(3):
    max_ = max(calorie_packs)
    calorie_packs[max_] -= 1
    if calorie_packs[max_] < 1:
        del calorie_packs[max_]

    calorie_sum += max_

print(calorie_sum)
