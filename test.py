from giterator import giterator

@giterator
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
    
    Returnss
    -------
    TYPE
        Description
    """
    s = x * y * z #some comment
    s = s ** 0.36

    # useless line
    return s


def main():
    dummy_func(1, 2, 3)

if __name__ == '__main__':
    main()