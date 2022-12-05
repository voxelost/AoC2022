with open("day_02/resources/input_2.txt") as fptr:
    input_ = list(line.strip().split(' ') for line in fptr.readlines())


SHAPES = {
    'A': 1,
    'B': 2,
    'C': 3,
}

RESULTS = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

def count_points(shape_enemy: str, ally_move: str) -> int:
    if ally_move == 'X':
        return (SHAPES[shape_enemy] + 1) % 3 + 1 + RESULTS[ally_move] # lose
    if ally_move == 'Z':
        return (SHAPES[shape_enemy] + 3) % 3 + 1 + RESULTS[ally_move]  # win
    return SHAPES[shape_enemy] + RESULTS[ally_move]


print(sum(count_points(*battle) for battle in input_))

