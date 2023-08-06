import os
import pathlib
import shutil

def getwd():
    return os.path.realpath(os.path.abspath(os.getcwd()))

def setwd(path):
    return os.chdir(path)


def dirname(path):
    return os.path.dirname(path)

def basename(path):
    return os.path.basename(path)

def file_ext(path):
    return os.path.splitext(path)[1]


def file_path(*args):
    return os.path.join(*args)

Path = pathlib.Path

def list_dirs(path, pattern = "*", full_names=True, recursive=True):
    pattern = "**" + os.sep + pattern if recursive else pattern
    res = [p for p in pathlib.Path(path).glob(pattern) \
                if os.path.isdir(p)]
    if full_names:
        return res
    else:
        return [basename(p) for p in res]

def list_files(path, pattern="*", full_names = True, recursive=True):
    pattern = "**" + os.sep + pattern if recursive else pattern
    res = [p for p in pathlib.Path(path).glob(pattern) \
                if os.path.isfile(p)]
    if full_names:
        return res
    else:
        return [basename(p) for p in res]
## `pattern` is here not regex pattern, but bash file path pattern of `glob`


def dir_exists(path):
    return os.path.isdir(path)

def file_exists(path):
    return os.path.isfile(path)


def dir_create(path, recursive=True):
    os.makedirs(path, exist_ok=True)
    print(f"Created {path}")

def file_create(path):
    pathlib.Path(path).touch()
    print(f"Created {path}")

def unlink(path):
    os.unlink(path)

def file_copy(_from, _to):
    if dir_exist(_from):
        shutil.copytree(src=_from, dst=_to,
                        symlinks=False, 
                        ignore=None, 
                        copy_function=shutil.copy2, 
                        ignore_dangling_symlinks=False, 
                        dirs_exist_ok=False)
    elif file_exist(_from):
        if dir_exist(_to):
            _to = file_path(_to, basename(_from))
        shutil.copyfile(_from, _to,
                        follow_symlinks=True)
    else:
        raise FileNotFoundError


def move(_from, _to, copy_function=shutil.copy2):
    return shutil.move(src=_from, dst=_to,           
                       copy_function=copy_function)

def file_rename(_from, _to):
    return shutil.move(src=_from, dst=_to)








class FileInfo:
    
    def __init__(self, path):
        self.path = path
        self.size = os.path.getsize(path)
        self.atime = os.path.getatime(path)
        self.ctime = os.path.getctime(path)
        self.mtime = os.path.getmtime(path)
        self.isdir = os.path.isdir(path)
