#!/bin/python

class NoSuchDir(Exception):
    def __init__(self, dir):
        self.msg = dir
        super().__init__(self.msg)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


class Dir:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.entries = set()

    def mkdir(self, d):
        new_dir = Dir(d)
        new_dir.parent = self
        self.entries.add(new_dir)

    def mkfile(self, f, size):
        self.entries.add(File(f, size))

    def get_size(self):
        size = 0
        for e in self.entries:
            size += e.get_size()
        return size

    def get_dir(self, name):
        if name == "..":
            return self.parent
        for e in self.entries:
            if isinstance(e, Dir):
                if e.name == name:
                    return e
        raise NoSuchDir(name)

    def __repr__(self):
        return self.name

    def ls(self):
        out = ["{}:".format(self.name)]
        for e in self.entries:
            if isinstance(e, Dir):
                out.append("{}/".format(e.name))
            if isinstance(e, File):
                out.append("{} {}".format(e.name, e.size))
        return "\n".join(out)

    def lsR(self, indent=0):
        out = ["{}{}/".format(indent*" ", self.name)]
        for e in self.entries:
            if isinstance(e, Dir):
                out.append(e.lsR(indent=indent+2))
            if isinstance(e, File):
                out.append("{}{} {}".format(indent*" ", e.name, e.size))
        return "\n".join(out)

    def walk_dirs(self):
        for e in self.entries:
            if isinstance(e, Dir):
                yield e
                yield from e.walk_dirs()

fs = Dir("/")
cwd = fs

ls_out = False
with open("input", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith("$"):
            ls_out = False
            cmd = line.split(" ")[1:]
            if cmd[0] == "cd":
                if cmd[1] == "/":
                    cwd = fs
                else:
                    cwd = cwd.get_dir(cmd[1])
            if cmd[0] == "ls":
                ls_out = True
        else:
            if ls_out:
                if line.startswith("dir"):
                    dirname = line.split(" ")[1]
                    cwd.mkdir(dirname)
                else:
                    size, name = line.split(" ")
                    cwd.mkfile(name, int(size))

print(fs.lsR())

total = 0

for dir in fs.walk_dirs():
    size = dir.get_size()
    if size < 100_000:
        total += size

print(total)

    
