#! /usr/bin/env python
"""Get all file extensions in the current folder and all its subfolders"""
from pathlib import Path


def get(path):
    extensions = set()
    for subpath in path.iterdir():
        if subpath.is_dir():
            extensions |= get(subpath)
        else:
            extensions.add(subpath.suffix)
    return extensions


if __name__ == '__main__':
    print(sorted(list(get(Path('.')))))
