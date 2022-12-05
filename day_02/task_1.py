import enum

with open("day_02/resources/input_2.txt") as fptr:
    input_ = list(line.strip().split(' ') for line in fptr.readlines())


class Result(enum.Enum):
    Lost = 0
    Draft = 3
    Win = 6


class AliasDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.aliases = {}

    def __getitem__(self, key):
        return dict.__getitem__(self, self.aliases.get(key, key))

    def __setitem__(self, keys, value):
        if len(keys) > 1:
            for key in keys[1:]:
                self.aliases[key] = keys[0]
        return dict.__setitem__(self, self.aliases.get(key, key), value)


def battle_result(shape_enemy: str, shape_ally: str) -> Result:
    if SHAPES[shape_enemy] == SHAPES[shape_ally]:
        return Result.Draft

    if (SHAPES[shape_enemy] - 1 + 4) % 3 == SHAPES[shape_ally] - 1:
        return Result.Win

    return Result.Lost

def count_points(shape_enemy: str, shape_ally: str) -> int:
    return battle_result(shape_enemy, shape_ally).value + SHAPES[shape_ally]


SHAPES = AliasDict()
SHAPES['A', 'X'] = 1
SHAPES['B', 'Y'] = 2
SHAPES['C', 'Z'] = 3

print(sum(count_points(*battle) for battle in input_))

