#!/usr/bin/env python3

from os import path, makedirs, errno
import shutil

# this script will make a backup of the important configuration files  
# the file paths will be read from the file stored in the variable CONFIG_PATHS
# the file should contain one path foreach line. 

CONFIG_PATHS = path.join('.', 'config_paths.txt')

def backup(config_file: str):
    with open(config_file, 'r') as f:
        # creatint the set of the path (unique)
        paths = set()
        for line in f.readlines():
            line = line.strip('\n')
            line = line.strip('\r')
            p = path.relpath(path=path.expanduser(line), 
                             start=path.expanduser('~'))
            paths.add(p)
        
        # now I have all the paths relative to the home in the paths set
        # I can reproduce the correct directory structure in the files dir
        for p in paths:
            backup_path = path.join('./files/home/$USER/', p) # todo automize
            p = path.join(path.expanduser('~'), p)
            
            # creating the path if it does not exists
            makedirs(path.dirname(backup_path), exist_ok=True)

            # copying the file 
            try:
                shutil.copyfile(p, backup_path)
            except FileNotFoundError:
                print('[WARNING] File:', p, 'not found. Skipping!')

if __name__ == "__main__":
    backup(CONFIG_PATHS)



    
