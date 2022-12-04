#!/usr/bin/env python3
import os

BASE_DIR = os.path.join('.')

FILE_BOILERPLATE = '''with open("{folder_name}/resources/input_1.txt") as fptr:
    input_ = list(line.strip() for line in fptr.readlines())

print(input_)
'''

def ensure_file(name: str, contents: str | None = None) -> None:
    if not os.path.exists(name):
        with open(name, 'w') as fptr:
            if contents:
                fptr.write(contents)


def ensure_dir(name: str | os.PathLike) -> None:
    if not os.path.exists(name):
        os.mkdir(name)


for day_no in range(1, 26):
    folder_name = f'day_{day_no}'
    folder_path = os.path.join(BASE_DIR, folder_name)

    ensure_dir(folder_path)

    subfiles = os.listdir(folder_path)

    for task_no in range(1, 3):
        ensure_file(os.path.join(folder_path, f'task_{task_no}.py'), FILE_BOILERPLATE.format(folder_name=folder_name))
        ensure_dir(os.path.join(folder_path, f'resources'))
        ensure_file(os.path.join(folder_path, f'resources/input_{task_no}.txt'))
