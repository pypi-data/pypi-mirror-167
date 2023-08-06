#!/usr/bin/env python
# encoding: utf-8

import os
import lizard
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count


class Result(dict):
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], dict):
            kwargs.update(args[0])
            args = tuple()
        kwargs = {k: Result(v) if isinstance(v, dict) else v for k, v in kwargs.items()}
        dict.__init__(self, *args, **kwargs)

    @property
    def cyclomatic_complexity(self):
        return self.get("cyclomatic_complexity") or sum(
            file.cyclomatic_complexity for file in self.files.values()
        )

    def __getitem__(self, key):
        self.setdefault(key, Result())
        return self.get(key)

    def __setitem__(self, key, value):
        if isinstance(value, dict) and not isinstance(value, Result):
            value = Result(value)
        dict.__setitem__(self, key, value)

    __getattr__ = __getitem__
    __setattr__ = __setitem__


def process(file):
    info = lizard.analyze_file(file)
    funcs = [
        dict(
            name=func.long_name,
            type="functions",
            cyclomatic_complexity=func.cyclomatic_complexity,
        )
        for func in info.function_list
    ]
    return dict(
        name=file,
        type="file",
        cyclomatic_complexity=sum(func["cyclomatic_complexity"] for func in funcs),
        functions=funcs,
    )


def main(path):
    """analyze source cyclomatic complexity
    path: source file or directory"""
    path = os.path.abspath(path)
    if os.path.isdir(path):
        tasks = [
            p + "/" + name
            for p, _, names in os.walk(path)
            for name in names
            if lizard.get_reader_for(p + "/" + name)
        ]
        root = Result(type="directory")
        with ProcessPoolExecutor(max_workers=cpu_count()) as exe:
            for fullname, res in zip(tasks, exe.map(process, tasks)):
                names = fullname[len(path) :].split("/")
                name = names.pop()
                curr = root
                for dname in filter(None, names):
                    curr = curr.files[dname]
                    curr.type = "directory"
                curr.files[name] = Result(res)
        return root
    return Result(process(path))
