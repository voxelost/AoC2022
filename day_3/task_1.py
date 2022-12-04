from collections import defaultdict

with open("day_3/resources/input_2.txt") as fptr:
    input_ = list(line.strip() for line in fptr.readlines())


def get_priority(chr_: chr) -> int:
    if chr_.islower():
        return ord(chr_) - ord('a') + 1
    return ord(chr_) - ord('A') + 27

priorities = 0
for rucksack in input_:
    items_count = len(rucksack)
    first_comp = rucksack[:items_count // 2]

    sack_items = {}
    for item in first_comp:
        sack_items[item] = True

    second_comp = rucksack[items_count // 2:]
    for item in second_comp:
        if item in sack_items:
            priorities += get_priority(item)
            break

print(priorities)
