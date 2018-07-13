import inspect
from utils import remove_human_lines, hash_fn
import os


def setup(func):
    f_file = inspect.getfile(func)
    f_dir = f_file[:f_file.rfind('/')]


def giterator(func):
    func_string = inspect.getsource(func)
    clean_string = remove_human_lines(func_string)
    func_hash = hash_fn(clean_string)
    print(func_hash)
    def wrapper(*args, **kwargs):
        pass
    return wrapper


