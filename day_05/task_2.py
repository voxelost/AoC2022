import re

with open("day_05/resources/input_2.txt") as fptr:
    input_ = list(line.rstrip() for line in fptr.readlines())


class Stack(list):
    def __init__(self, crates: list[str]):
        super().__init__(crates)

    @classmethod
    def parse(cls, *crates: tuple[str]):
        crates_parsed = list(re.match(r'\[([a-zA-Z])\]', crate).group(1) for crate in crates)
        return cls(crates_parsed)

    def push(self, crate: str):
        if match := re.match(r'\[([a-zA-Z])\]', crate):
            crate = match.group(1)
        return self.append(crate)




class Command():
    def __init__(self, amount: int, source_stack: int, dest_stack: int):
        self.amount = amount
        self.source_stack = source_stack
        self.dest_stack = dest_stack

    @classmethod
    def parse(cls, command_raw: str):
        command_parsed = re.match(r'move (\d+) from (\d+) to (\d+)', command_raw)
        return cls(*(int(num) for num in command_parsed.groups()))

    def __repr__(self):
        return f'{self.amount} crates from {self.source_stack} to {self.dest_stack}'


class Crane():
    def __init__(self, stacks: dict[int, Stack], commands: list[Command]):
        self.stacks = stacks
        self.commands = commands

    @classmethod
    def parse(cls, input_raw: list[str]):
        stack_lines = []
        for idx, line in enumerate(input_raw):
            if len(line) < 1:
                break
            stack_lines.append(line)

        stack_matrix = []
        for idx, line in enumerate(stack_lines[:-1]):
            stack_matrix.append([])
            for idy, _ in enumerate(line[::4]):

                slice_ = line[idy*4:idy*4+3]
                if len(slice_.strip()) < 1:
                    elem = None
                else:
                    elem = slice_[:3]
                stack_matrix[idx].append(elem)

        stack_matrix.append(list(element for element in re.split(r'\s+', stack_lines[-1]) if element != ''))
        stack_matrix.reverse()

        stacks = {}
        for idx, num in enumerate(stack_matrix[0]):
            stacks[int(num)] = Stack([])
            for line in stack_matrix[1:]:
                if idx >= len(line) or line[idx] == None:
                    break
                stacks[int(num)].push(line[idx])


        commands = list(Command.parse(raw_command) for raw_command in input_raw[len(stack_matrix)+1:])
        return cls(stacks, commands)


    def _execute_one(self, command: Command):
        for _ in range(command.amount):
            self.stacks[command.dest_stack].append(self.stacks[command.source_stack].pop())

    def execute_all(self):
        for command in self.commands:
            print("before")
            print(self, end='\n\n')
            print(f"command: {command!r}")
            self._execute_one(command)
            print("after")
            print(self, end='\n\n')

    def __str__(self):
        return '\n'.join(f'{no}: {crates}' for (no, crates) in self.stacks.items())

crane = Crane.parse(input_)
crane.execute_all()

print(''.join(crane.stacks[stack_no][-1] for stack_no in sorted(crane.stacks.keys())))
