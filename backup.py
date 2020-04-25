#!/usr/bin/env python3

from os import path, makedirs, sep, walk
import errno
from getpass import getuser
from shutil import copyfile

# this script will make a backup of the important configuration files
# the file paths will be read from the file stored in the variable CONFIG_PATHS
# the file should contain one path foreach line.

CONFIG_PATHS = path.join('.', 'config_paths.txt')


def path_set_from_file(config_file: str) -> set:
    with open(config_file, 'r') as f:
        # creatint the set of the path (unique)
        paths = set()
        for line in f.readlines():
            line = line.strip('\n')
            line = line.strip('\r')
            p = path.relpath(path=path.expanduser(line),
                             start=path.expanduser('~'))
            paths.add(p)

    return paths


def backup(paths: set, backup_root=path.join('.', 'files')):
    # I have all the paths relative to the home in the paths set
    # I can reproduce the correct directory structure in the files dir
    for p in paths:
        # getting the path of the home relative from the root
        home = path.expanduser('~')[1:].replace(getuser(), '%USER%')
        backup_path = path.join(backup_root, home, p)
        p = path.join(path.expanduser('~'), p)

        # creating the path if it does not exists
        makedirs(path.dirname(backup_path), exist_ok=True)

        # copying the file
        try:
            copyfile(p, backup_path)
        except FileNotFoundError:
            print('[WARNING] File:', p, 'not found. Skipping!')


def restore(backup_root=path.join('.', 'files'), root_dir=path.abspath(sep)):
    backup_root = path.join(backup_root, '')
    root_dir = path.join(root_dir, '')
    for root, _, files in walk(backup_root):
        for f in files:
            backup_path = path.join(root, f)
            restore_path = backup_path.replace(backup_root, root_dir) \
                                      .replace('%USER%', getuser())

            # try to copy the file
            try:
                makedirs(path.dirname(restore_path), exist_ok=True)
                copyfile(backup_path, restore_path)
            except PermissionError as err:
                print('[warning] cannot restore file',backup_path, end=' ')
                print(err.strerror, '... Skipping!', sep='')


if __name__ == "__main__":
    backup(path_set_from_file(CONFIG_PATHS))
    #restore()
