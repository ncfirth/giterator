from giterator import giterator

@giterator
def dummy_func(x, y, z=5):
    """Summary
    
    Parameters
    ----------
    x : TYPE
        Description
    y : TYPE
        Description
    z : TYPE
        Description
    
    Returnssdsfs;ohwer
    -------
    TYPE
        Description
    """
    s = x * y * z #some comment
    s = s ** 0.33

    # useless line
    return s


def main():
    dummy_func(7, 2, z=3)
    dummy_func(8, 5, z=3)

if __name__ == '__main__':
    main()