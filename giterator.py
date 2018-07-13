import inspect
from utils import remove_human_lines, hash_fn, get_func_dir_from_file
import os
import pandas as pd
import joblib
from datetime import datetime



def version_setup(func):
    func_file = inspect.getfile(func)
    func_dir = get_func_dir_from_file(func_file)
    giterator_dir = f'{func_dir}/.giterator'
    if not os.path.isdir(giterator_dir):
        os.mkdir(giterator_dir)
        versions = pd.DataFrame(columns=['function_name', 'contained_in', 
                                         'function_hash', 'version',
                                         'datetime', 'function_text'])
        joblib.dump(versions, f'{giterator_dir}/function_versions.pkl')
    else:
        versions = joblib.load(f'{giterator_dir}/function_versions.pkl')
    return versions


def get_version(func, versions):
    func_text = inspect.getsource(func)
    func_hash = hash_fn(remove_human_lines(func_text))
    func_file = inspect.getfile(func)
    func_dir = get_func_dir_from_file(func_file)

    if '/' in func_file:
        func_file = func_file[func_file.rfind('/'):]

    func_versions = versions[(versions.function_name == func.__name__) |
                             (versions.contained_in == func_file)]
    if func_hash in func_versions.function_hash.values:
        this_version = func_versions.loc[func_versions.function_hash == func_hash,
                                         'version'].values[0]
        return func.__name__, func_file, this_version
    if func_versions.shape[0] == 0:
        this_version = 1
    else:
        this_version = func_versions.version.max() + 1
    versions = versions.append(dict(function_name=func.__name__,
                                    contained_in=func_file,
                                    function_hash=func_hash,
                                    version=this_version,
                                    datetime=datetime.now(),
                                    function_text=func_text),
                               ignore_index=True)
    joblib.dump(versions, f'{func_dir}/.giterator/function_versions.pkl')
    return func.__name__, func_file, this_version

 
def giterator(func):
    versions = version_setup(func)
    func_name, func_dir, func_version = get_version(func, versions)
    
    def wrapper(*args, **kwargs):
        pass
    return wrapper


