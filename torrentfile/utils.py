import os
from pathlib import Path

KIB = 1 << 10
MIB = KIB * KIB
GIB = KIB**3
MIN_BLOCK = 2**14
TOP_SIZE = 2**18


resolve = lambda x: Path(x).resolve()

def get_piece_length(size):
    """
    Calculate the ideal piece length for bittorrent data.

    Args:
        size (int): total bits of all files incluided in .torrent file

    Returns:
        int: the ideal peace length calculated from the size arguement
    """
    exp = 14
    while size / (2**exp) > 50 and exp < 20:
        exp += 1
    if exp == 19 and size / MIB > 2000:
        while size / (2**exp) > 2000 and exp <= 23:
            exp += 1
    return 2**exp

def sortfiles(path):
    filelist = sorted(os.listdir(path),key=str.lower)
    for item in filelist:
        yield os.path.join(path,item)

def dir_files_sizes(path):
    if os.path.isfile(path):
        return [path], os.path.getsize(path)
    filelist, total = [], 0
    if os.path.isdir(path):
        for item in sortfiles(path):
            files, size = dir_files_sizes(item)
            filelist.extend(files)
            total += size
    return filelist, total

def path_size(path):
    """Calculate sum of all filesizes within directory.

    Args:
        path (pathlike): The path to start calculating from.

    Returns:
        int: total sum in bytes
    """
    if os.path.isfile(path):
        return os.path.getsize(path)

    #recursive sum for all files in folder
    elif os.path.isdir(path):
        size = 0
        for name in os.listdir(path):
            fullpath = os.path.join(path,name)
            size += path_size(fullpath)
    return size

def get_file_list(path, sort=False):
    """Search directory tree for files.

    Args:
        path (pathlike): path to file or directory base
        sort (bool, optional): return list sorted. Defaults to False.

    Returns:
        [list]: all file paths within directory tree.
    """
    if os.path.isfile(path): return [path]

    # put all files into filelist within directory
    files = list()
    filelist = os.listdir()

    # optional canonical sort of filelist
    if sort: filelist.sort(key=str.lower)

    # recursive for all folders
    for item in filelist:
        full = os.path.join(path,item)
        files.extend(get_file_list(full,sort=sort))
    return files

def path_stat(path):
    filelist, size = dir_files_sizes(path)
    piece_length = get_piece_length(size)
    return (filelist, size, piece_length)


def do_something():
    pass