import inspect
import re


def giterator(func, *args, **kwargs):
    func_string = inspect.getsource(func)
    def wrapper():
        pass
    return wrapper


def dummy_func(x, y, z):
    """Summary
    
    Parameters
    ----------
    x : TYPE
        Description
    y : TYPE
        Description
    z : TYPE
        Description
    
    Returns
    -------
    TYPE
        Description
    """
    s = x * y * z #some comment
    s = s ** 0.33

    # useless line
    return s


def remove_pattern(string, pattern):
    new_string = string.split('\n')
    new_string = [x for x in new_string if re.match(pattern, x) is None]
    return '\n'.join(new_string)

def remove_spacing(string):
    new_string = string.split('\n')
    whitespace = re.compile('^\s*$|^$')
    new_string = [x for x in new_string if re.match(whitespace, x) is None]
    return '\n'.join(new_string)


def remove_comments(string):
    new_string = re.sub('^\s+\"\"\"\.\"\"\"$')
    comments = re.compile('^\s+#')
    return remove_pattern(string, comments)

def remove_human_lines(string):
    whitespace = re.compile('^\s*$|^$')
    comments = re.compile('^\s+#|^\s+\"\"\"')




def main():
    f_str = inspect.getsource(dummy_func)
    print(remove_comments(f_str))


if __name__ == '__main__':
    main()