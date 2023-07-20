with open("day_04/resources/input_2.txt") as fptr:
    input_ = list(line.strip() for line in fptr.readlines())


def does_contain(range_one: tuple, range_two: tuple):
    return range_one[0] <= range_two[0] and range_one[1] >= range_two[1]

overlap_counter = 0
for line in input_:
    line_split = line.split(',')

    range_one = tuple(int(elem) for elem in line_split[0].split('-'))
    range_two = tuple(int(elem) for elem in line_split[1].split('-'))

    print(range_one, range_two)

    if does_contain(range_one, range_two) or does_contain(range_two, range_one):
        overlap_counter += 1
print(overlap_counter)
