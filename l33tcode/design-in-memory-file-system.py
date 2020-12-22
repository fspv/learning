from typing import Dict, Union, List


class FileSystemUnit:
    pass


class Directory(FileSystemUnit):
    def __init__(self) -> None:
        self.children: Dict[str, Union[Directory, File]] = {}


class File(FileSystemUnit):
    def __init__(self) -> None:
        self.content: List[str] = []

    def append(self, content: str) -> None:
        self.content.extend(content.split("\n"))

    def read(self) -> str:
        return "".join(self.content)


class FileSystem:
    def __init__(self):
        self.root = Directory()

    def _norm_path(self, path: str) -> List[str]:
        return list(filter(bool, path.split("/")))

    def _find_path(
        self, path: List[str], path_pos: int, unit: Union[Directory, File]
    ) -> Union[Directory, File]:
        if path_pos == len(path):
            return unit

        if not isinstance(unit, Directory):
            raise ValueError("We can't dive into non-directory")

        child = unit.children.setdefault(path[path_pos], File())

        return self._find_path(path, path_pos + 1, child)

    def _mkdir(
        self, path: List[str], path_pos: int, unit: Union[Directory, File]
    ) -> None:
        if path_pos == len(path):
            return

        if not isinstance(unit, Directory):
            raise ValueError("We can't dive into non-directory")

        child = unit.children.setdefault(path[path_pos], Directory())

        return self._mkdir(path, path_pos + 1, child)

    def ls(self, path: str) -> List[str]:
        path_norm = self._norm_path(path)
        resolved_path = self._find_path(path_norm, 0, self.root)

        # It is a dir, return its contents
        if isinstance(resolved_path, Directory):
            return list(sorted(resolved_path.children.keys()))

        # It was a file, return its name
        return [path_norm[-1]]

    def mkdir(self, path: str) -> None:
        path_norm = self._norm_path(path)
        self._mkdir(path_norm, 0, self.root)

    def addContentToFile(self, path: str, content: str) -> None:
        path_norm = self._norm_path(path)
        resolved_path = self._find_path(path_norm, 0, self.root)

        if isinstance(resolved_path, Directory):
            raise ValueError("Can't add content to directory")

        resolved_path.append(content)

    def readContentFromFile(self, path: str) -> str:
        path_norm = self._norm_path(path)
        resolved_path = self._find_path(path_norm, 0, self.root)

        if isinstance(resolved_path, Directory):
            raise ValueError("Can't read from directory")

        return resolved_path.read()


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
