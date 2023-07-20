with open("day_01/resources/input_2.txt") as fptr:
    input_ = list(line.strip() for line in fptr.readlines())


cumulative = 0
calorie_packs = []
for line in input_:
    if len(line) < 1:
        calorie_packs.append(cumulative)
        cumulative = 0
        continue

    cumulative += int(line)

print(max(calorie_packs))
