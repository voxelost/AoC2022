with open("day_07/resources/input_2.txt") as fptr:
    input_ = list(line.strip() for line in fptr.readlines())


class UnimplementedError(Exception): ...


class FilePath(list):
    def __init__(self, *args: list[str]):
        if len(args) == 0:
            args = ['/']

        super().__init__(*args)


class FSNode():
    def get_size(self) -> int:
        raise UnimplementedError("implement me!")


class Directory(FSNode):
    def __init__(self, name: str):
        self.name = name
        self.children = {}

    def get_size(self) -> int:
        return sum(node.get_size() for node in self.children.values())

    def __getitem__(self, key: str) -> FSNode:
        return self.children[key]

    def __setitem__(self, key: str, value: FSNode):
        self.children[key] = value


class File(FSNode):
    def __init__(self, size: int, name: str):
        self.size = size
        self.name = name

    def get_size(self) -> int:
        return self.size


class FileSystem(Directory):
    def __init__(self, default_dir: FilePath=FilePath()):
        self.current_directory = default_dir
        self.children = {
            '/': Directory('/') # initialize fs tree
        }

    @classmethod
    def parse(cls, lines: list[str]):
        _filesystem = cls()
        idx = 0
        _idx_range = len(lines)

        while idx < _idx_range:
            line = lines[idx]
            if line.startswith('$'):
                line = line.lstrip('$').lstrip()
                command, *args = line.split()

                output_lines = []
                while idx < _idx_range - 1 and not (line := lines[idx+1]).startswith('$'):
                    output_lines.append(line.split())
                    idx += 1

                _filesystem._command(command, args, output=output_lines)
            idx += 1
        return _filesystem

    def _command(self, command: str, *args, **kwargs):
        return {
            'cd': self.change_directory,
            'ls': self.list_directory
        }[command](*args, **kwargs)

    def get_node(self, path: FilePath) -> FSNode:
        cur_node = self.children
        for path_element in path:
            cur_node = cur_node[path_element]
        return cur_node

    def set_node(self, path: FilePath, node: FSNode) -> None:
        cur_node = self.children
        for path_element in path[:-1]:
            cur_node = cur_node[path_element]
        cur_node[path[-1]][node.name] = node

    def change_directory(self, path: FilePath, **_) -> None:
        if path[0] == '/':
            self._change_directory_absolute(path)
        else:
            self._change_directory_relative(path)

    def _change_directory_relative(self, path: FilePath) -> None:
        if path[0] == '..':
            self.current_directory.pop()
        else:
            self.current_directory.extend(path)

    def _change_directory_absolute(self, path: FilePath) -> None:
        self.current_directory = path

    def list_directory(self, path: FilePath, output: list[FSNode]=[]) -> list[FSNode]:
        if len(path) == 0:
            path = self.current_directory

        for node in output:
            node_obj: FSNode
            if node[0].startswith('dir'):
                node_obj = Directory(node[1])
            else:
                node_obj = File(int(node[0]), node[1])

            self.set_node(path, node_obj)


def scan_fs(fs: FileSystem, path: FilePath=FilePath()):
    current_path = path
    sizes = []

    for k, v in fs.children.items():
        current_path.append(k)
        if isinstance(v, Directory):
            sizes.extend(scan_fs(v, current_path))
            sizes.append(v.get_size())
        current_path.pop()

    return sizes


if __name__ == '__main__':
    TOTAL_FILESYSTEM_SIZE = 70000000
    UPDATE_REQUIRED_SPACE = 30000000
    fs = FileSystem.parse(input_)
    all_sizes = scan_fs(fs)
    total_used_space = max(all_sizes)
    space_available = TOTAL_FILESYSTEM_SIZE - total_used_space
    space_needed = UPDATE_REQUIRED_SPACE - space_available # 8381165

    for dir_size in sorted(all_sizes):
        if dir_size >= space_needed:
            print(dir_size)
            break

