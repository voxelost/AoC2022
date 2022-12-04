from collections import defaultdict


with open("day_3/resources/input_2.txt") as fptr:
    input_ = list(line.strip() for line in fptr.readlines())

    groups = []
    for idx in range(0, len(input_) // 3):
        groups.append([])
        for i in range(3):
            groups[idx].append(input_[idx * 3 + i])

def get_priority(chr_: chr) -> int:
    if chr_.islower():
        return ord(chr_) - ord('a') + 1
    return ord(chr_) - ord('A') + 27

def scan_group(group: list[str]):
    get_default = lambda: {
        0: False,
        1: False,
        2: False,
    }

    items = defaultdict(get_default)

    for idx, rucksack in enumerate(group):
        for item in rucksack:
            items[item][idx] = True
            if all(items[item].values()):
                return get_priority(item)
    return 0


priorities_sum = 0
for group in groups:
    priorities_sum += scan_group(group)
print(priorities_sum)
