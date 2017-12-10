import tests

def search(array, item):
    """
    Return ``tuple(contains, index)``
    if ``item`` not contains in ``list``, return ``(False, -1)``
    """
    for i, j in enumerate(array):
        if isinstance(i, type(item)) and i == item:
            return (True, i)    
    return (False, -1)

